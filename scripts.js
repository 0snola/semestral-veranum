function iniciarMapVina(){
    var coord = {lat:-32.984475 ,lng: -71.547783};
    var map = new google.maps.Map(document.getElementById('map'),{
      zoom: 15,
      center: coord
    });
    var marker = new google.maps.Marker({
      position: coord,
      map: map
    });
}

function iniciarMapSantiago(){
  var coord = {lat:-33.445585 ,lng: -70.625780};
  var map = new google.maps.Map(document.getElementById('map'),{
    zoom: 15,
    center: coord
  });
  var marker = new google.maps.Marker({
    position: coord,
    map: map
  });
}