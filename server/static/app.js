window.onload = function () {

    loadLocations();

};

function loadLocations() {

    fetch("http://127.0.0.1:5000/get_location_names")

        .then(response => response.json())

        .then(data => {

            const select = document.getElementById("uiLocations");

            select.innerHTML = "";

            const defaultOption = document.createElement("option");
            defaultOption.text = "Select Location";
            defaultOption.value = "";
            select.appendChild(defaultOption);

            data.location_names.forEach(function(location){

                const option = document.createElement("option");
                option.text = location;
                option.value = location;

                select.appendChild(option);

            });

        })

        .catch(error => {

            console.log("Server not ready. Retrying in 2 seconds...");

            setTimeout(loadLocations, 2000);

        });

}

function onClickedEstimatePrice() {

    var sqft = document.getElementById("uiSqft").value;
    var bhk = document.getElementById("uiBHK").value;
    var bath = document.getElementById("uiBathrooms").value;
    var location = document.getElementById("uiLocations").value;

    fetch("http://127.0.0.1:5000/get_prediction_price", {

        method: "POST",

        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },

        body:
            "total_sqft=" + sqft +
            "&bhk=" + bhk +
            "&bath=" + bath +
            "&location=" + encodeURIComponent(location)

    })

    .then(response => response.json())

    .then(data => {

        document.getElementById("uiEstimatedPrice").innerHTML =
            "₹ " + data.predicted_price + " Lakhs";

    })

    .catch(error => {

        console.log(error);

    });

}