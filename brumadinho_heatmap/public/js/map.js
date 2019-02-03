var mapData;

mapboxgl.accessToken = 'pk.eyJ1Ijoiam9zZWJlemVycmEiLCJhIjoiY2pyazVtdDA5MDE5czQ0cmdsNnFjZjVsdiJ9.g3x0Z17jXKFjfYEc2ivxsg';

var request = new XMLHttpRequest();

request.open('GET', 'https://brumadinho-api.herokuapp.com/api/all_places', true);

request.onload = function () {
    if (request.status >= 200 && request.status < 400) {
        mapData = JSON.parse(this.response);

    } else {
        console.log('error');
    }
}

request.send();

var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/satellite-streets-v9',
    // Long - Lat
    center: [-44.1227885, -20.1214628],
    zoom: 14
});

map.on('load', function () {
    map.addSource('earthquakes', {
        "type": "geojson",
        // "data": "./misc/coords.geojson"
        "data": mapData
    });

    map.addLayer({
        "id": "earthquakes-heat",
        "type": "heatmap",
        "source": "earthquakes",
        "paint": {
            'heatmap-radius': 5,
            "heatmap-weight": {
                "type": "identity",
                "property": "point_count"
            }
        }
    }, 'waterway-label');

});

map.on('mousemove', function (e) {
    let long = e.lngLat.lng
    let lat = e.lngLat.lat
    document.getElementById('info').innerHTML = "Latitude: "+lat+" Longitude: "+long
});