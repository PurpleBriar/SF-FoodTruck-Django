function validateForm() {
    var latitude = document.forms["Coordinates"]["latitude"].value;
    var longitude = document.forms["Coordinates"]["longitude"].value;

    if (latitude == "") {
        alert("Latitude value is missing");
        return false;
    }

    if (!parseFloat(latitude)) {
        alert("Latitude value is not a number");
        return false;
    }

    if ((parseFloat(latitude) < 37.4) || (parseFloat(latitude) > 38.4)) {
        alert("Latitude value is out of range. Please enter a value between 37.4 and 38.4 for the San Francisco Area");
        return false;
    }
    
    if (longitude == "") {
        alert("Longitude value is missing");
        return false;
    }

    if (!parseFloat(longitude)) {
        alert("Longitude value is not a number");
        return false;
    }

    if ((parseFloat(longitude) < -122.7) || (parseFloat(longitude) > -122.1)) {
        alert("Longitude value is out of range. Please enter a value between -122.7 and -122.1 for the San Francisco Area");
        return false;
    }                       
}