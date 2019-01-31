
mapboxgl.accessToken = 'pk.eyJ1Ijoiam9zZWJlemVycmEiLCJhIjoiY2pyazVtdDA5MDE5czQ0cmdsNnFjZjVsdiJ9.g3x0Z17jXKFjfYEc2ivxsg';

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
        "data": "./misc/coords.geojson"
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

// var marker = new mapboxgl.Marker({
//     draggable: true
// })
//     .setLngLat([0, 0])
//     .addTo(map);

// function onDragEnd() {
//     var lngLat = marker.getLngLat();
//     coordinates.style.display = 'block';
//     // coordinates.innerHTML = 'Longitude: ' + lngLat.lng + '<br />Latitude: ' + lngLat.lat;
// }

// marker.on('dragend', onDragEnd);
