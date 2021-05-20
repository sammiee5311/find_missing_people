

let map;
let markers = [];
let infoWindow;

function initMap() {
    const haightAshbury = { lat: 37.769, lng: -122.446 };
  
    infoWindow = new google.maps.InfoWindow();
    map = new google.maps.Map(document.getElementById('map'), {
      zoom: 11,
      center: haightAshbury
    });
    
    setMarkers();
}
  
const addMarkers = (location, title, id, i) => {
    const marker = new google.maps.Marker({
      position: location,
      map: map,
      title: `${title}`.link(`http://localhost:8000/listings/${id}`),
      label: `${i + 1}`,
    });
    marker.addListener("click", () => {
      infoWindow.close();
      infoWindow.setContent(marker.getTitle());
      infoWindow.open(marker.getMap(), marker);
    });
    markers.push(marker);
}
  
const setMarkers = () => {
    for (let i = 0; i < markers.length; i++){
      markers[i].setMap(map);
    }
  }
  
  const clearMarkers = () => {
    setMarkers(null);
    markers = [];
}
  
const searchMissingPeople = (missingPeopleData, btn) => {
    const city = btn.parentNode.querySelector('[name=city]').value;
    const stateData = btn.parentNode.querySelector('[name=state]');
    const state = stateData.options[stateData.selectedIndex].value.replace(" ","");
    const list = JSON.parse(missingPeopleData);
  
    clearMarkers();
  
    list.forEach((info,i) => {
      if(info.fields.state == state)
        addMarkers({lat: parseFloat(info.fields.lat), lng: parseFloat(info.fields.lng)}, info.fields.name, info.pk, i);
    });
}