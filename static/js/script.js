$(function () {
  $("#us2").locationpicker({
    location: { latitude: -17.783748, longitude: -63.183733 },
    radius: 0,
    inputBinding: {
      latitudeInput: $("#latEmisor"),
      longitudeInput: $("#lngEmisor"),
      locationNameInput: $("#location"),
    },
    enableAutocomplete: true,
    onchanged: function (currentLocation, radius, isMarkerDropped) {
      console.log(currentLocation.latitude, currentLocation.longitude)
    },
  });
});



$(function () {
    $("#us3").locationpicker({
      location: { latitude: -17.783748, longitude: -63.183733 },
      radius: 0,
      inputBinding: {
        latitudeInput: $("#latEntrega"),
        longitudeInput: $("#lngEntrega"),
        locationNameInput: $("#location"),
      },
      enableAutocomplete: true,
      onchanged: function (currentLocation, radius, isMarkerDropped) {
        console.log(currentLocation.latitude, currentLocation.longitude)
      },
    });
  });
  