import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/admin/Documents/pythonProjects/ML_projects/Bengaluru_House_Data.csv")
print(df.head(5))
print(df.info())
print(df.describe())

# === finding the null values ======
print(df.isnull().sum())
print(df.groupby('area_type')['area_type'].agg('count'))
df.drop(columns=['availability', 'society', 'balcony'], inplace=True)
print(df.head(5))

# ===== treating the null values =====
df2 = df.dropna()
print(df2.isnull().sum())
print(df2['size'].unique())
df2['bhk'] = df2['size'].apply(lambda x: int(x.split(' ')[0]))
print(df2.head(5))
print(df2.bhk.unique())


# ==== handling the unstructured data =====
def is_float(x):
    try:
        float(x)
    except:
        return False
    return True


print(df2[~df2['total_sqft'].apply(is_float)].head(5))


def convert_sqft(x):
    tokens = x.split('-')
    if len(tokens) == 2:
        return (float(tokens[0]) + float(tokens[1])) / 2
    try:
        return float(x)
    except:
        return None


print(convert_sqft('2100 - 2850'))
df3 = df2.copy()
df3['total_sqft'] = df3['total_sqft'].apply(convert_sqft)
print(df3.head(5))
print(df3.loc[1])

# ==== Feature enginering ====
df3['price_per_sqft'] = df3['price'] * 100000 / df3['total_sqft']
print(df3.head(5))

# ====  handling of the location feature=====
loc_count = df3['location'].value_counts()
print(loc_count)
other_loc = loc_count[loc_count <= 10].index
df3['location'] = df3['location'].replace(other_loc, 'Others')
print(df3.head(10))
print(len(df3['location']))
loc_stats = df3.groupby('location')['location'].agg('count').sort_values(ascending=False)
print(loc_stats)
print(len(loc_stats))
print(other_loc)
print(len(other_loc))
print(df3.head(10))

# ==== removing the outliers ======
print(df3[df3['total_sqft'] / df3['bhk'] < 300].head(5))
print(df3.shape)
# removed some outliers#
df4 = df3[~(df3['total_sqft'] / df3['bhk'] < 300)]
print(df4.shape)


def remove_outliers(df):
    df_out = pd.DataFrame()
    for key, subdf in df.groupby('location'):
        m = np.mean(subdf.price_per_sqft)
        st = np.std(subdf.price_per_sqft)
        reduced_df = subdf[(subdf.price_per_sqft > (m - st)) & (subdf.price_per_sqft <= (m + st))]
        df_out = pd.concat([df_out, reduced_df], ignore_index=True)
    return df_out


df5 = remove_outliers(df4)
print(df5.shape)
print(df5.head(5))


# ==== visualizing the plot =====
def plot_scatter_plot(df, location):
    bhk2 = df[(df.location == location) & (df.bhk == 2)]
    bhk3 = df[(df.location == location) & (df.bhk == 3)]
    plt.rcParams['figure.figsize'] = (10, 8)
    plt.scatter(bhk2.total_sqft, bhk2.price_per_sqft, label='bhk2', color='blue', s=50)
    plt.scatter(bhk3.total_sqft, bhk3.price_per_sqft, marker="+", label='bhk3', color='green', s=50)
    plt.xlabel('Total Square Feet Area')
    plt.ylabel('Price per Square Feet')
    plt.title(location)
    plt.legend()
    # plt.show()


pltplot = plot_scatter_plot(df5, 'Rajaji Nagar')
print(pltplot)


def remove_bhk_outliers(df):
    exclude_indices = np.array([])
    for location, location_df in df.groupby('location'):
        bhk_stats = {}
        for bhk, bhk_df in location_df.groupby('bhk'):
            bhk_stats[bhk] = {
                'mean': np.mean(bhk_df.price_per_sqft),
                'std': np.std(bhk_df.price_per_sqft),
                'count': bhk_df.shape[0]
            }
        for bhk, bhk_df, in location_df.groupby('bhk'):
            stats = bhk_stats.get(bhk - 1)
            if stats and stats['count'] > 5:
                exclude_indices = np.append(exclude_indices,
                                            bhk_df[bhk_df.price_per_sqft < (stats['mean'])].index.values)
    return df.drop(exclude_indices, axis="index")


df6 = remove_bhk_outliers(df5)
print(df6.shape)
pltplot2 = plot_scatter_plot(df5, 'Kothanur')
print(pltplot2)

plt.rcParams['figure.figsize'] = (10, 8)
plt.hist(df6.price_per_sqft, rwidth=0.8)
plt.xlabel('Price per sqft')
plt.ylabel('Count')
# plt.show()

# ===== outliers for the Bath =====
print(df6.bath.unique())
print(df6[df6.bath > 10])
plt.hist(df6.bath, rwidth=0.8)
plt.xlabel('No. of Bathrooms')
plt.ylabel('Count')
# plt.show()

print(df6[df6.bath < df6.bhk + 2])
df7 = df6[df6.bath < df6.bhk + 2]
print(df7)
print(df7.shape)

# ===== removing the unnecessary features =====
df8 = df7.drop(columns=['size', 'price_per_sqft', 'area_type'])
print(df8.head(5))
dummy = pd.get_dummies(df8.location, dtype=int)
print(dummy.head(5))
df9 = pd.concat([df8, dummy], axis='columns')
print(df9.head(5))
df10 = df9.drop('location', axis='columns')
print(df10.head(5))

# ===== splitting the features into features and target =====
X = df10.drop(['price'], axis='columns')
y = df10['price']
print(y)
print(X)

# ===== Training the model =======
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(len(X_train))
print(len(y_test))

# ===== buliding the models =====
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
# y_score=lr_model.score(X_test,y_test)
# print(y_score)
# ==== and what does this y_score=lr_model.score(X_test,y_test) actually means =====
y_pred = lr_model.predict(X_test)
score = r2_score(y_test, y_pred)
print(score)

from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_score

cv = ShuffleSplit(n_splits=5, test_size=0.2, random_state=42)
print(cross_val_score(LinearRegression(), X, y, cv=cv))

from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Lasso
from sklearn.tree import DecisionTreeRegressor


def find_best_model(X, y):
    algos = {
        'linear_regression': {
            'model': LinearRegression(),
            'params': {
                'fit_intercept': [True, False],
                'positive': [True, False]
            }
        },
        'lasso': {
            'model': Lasso(),
            'params': {
                'alpha': [1, 2],
                'selection': ['random', 'cyclic']
            }
        },
        'decision tree': {
            'model': DecisionTreeRegressor(),
            'params': {
                'criterion': ['squared_error', 'friedman_mse'],
                'splitter': ['best', 'random']
            }
        }
    }
    scores = []
    cv = ShuffleSplit(n_splits=5, test_size=0.2, random_state=42)
    for algo_name, config in algos.items():
        gs = GridSearchCV(config['model'], config['params'], cv=cv, return_train_score=False)
        gs.fit(X, y)
        scores.append({
            'model': algo_name,
            'best_score': gs.best_score_,
            'best_params': gs.best_params_
        })
    return pd.DataFrame(scores, columns=['model', 'best_score', 'best_params'])


print(find_best_model(X, y))


# ==== predicting the prices =====
def predict_price(location, total_sqft, bath, bhk):
    # loc_index= np.where(X.columns==location)[0][0]
    x = np.zeros(len(X.columns))
    x[0] = total_sqft
    x[1] = bath
    x[2] = bhk
    if location in X.columns:
        loc_index = np.where(X.columns == location)[0][0]
        x[loc_index] = 1
    else:
        print("Location not found!")
    return lr_model.predict([x])[0]


print(predict_price('Whitefield', 1170, 2, 2))
comparison = pd.DataFrame({
    "Actual Price": y_test.values,
    "Predicted Price": y_pred})
print(comparison.head(10))

import pickle

with open('/Users/admin/BHP/model/bangalore_home_prices_model.pickle', 'wb') as f:
    pickle.dump(lr_model, f)

print(X.columns)
import json

columns = {"data_columns": list(X.columns)}
with open("/Users/admin/BHP/model/columns.json", 'w') as f:
    json.dump(columns, f, indent=4)

row = X[
    (X['total_sqft'] == 1170) &
    (X['bhk'] == 2) &
    (X['bath'] == 2) &
    (X['Whitefield'] == 1)
    ]

print(row)