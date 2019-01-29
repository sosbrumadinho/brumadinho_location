var app = new Vue({
    el: '#app',
    data: {
        locale: 'eng',
        locales: {
            eng: 'English',
            por: 'Portuguese'
        },
        lat: '-20.135896',
        lng: '-44.123509'
    },
    methods: {
        calculate: calculate
    }
});

// WARNING: doesn't sanitize inputs
function createMarker(name, point) {
    return L.marker(point).bindPopup(
        '<b>' + name + '</b>' +
        '<br/>Latitude:' + point.lat +
        '<br/>Longitude:' + point.lng
    ).addTo(map);
}

function drawVector(pointA, pointB) {
    createMarker('Localização inicial', pointA);
    createMarker('Localização final (estimada)', pointB);

    const line = new L.Polyline([pointA, pointB], {
        color: 'red',
        weight: 3,
        opacity: 0.5,
        smoothFactor: 1
    }).addTo(map);

    L.polylineDecorator(line, {
        patterns: [
            {
                offset: '100%',
                repeat: 0,
                symbol: L.Symbol.arrowHead({
                    pixelSize: 15,
                    polygon: false,
                    pathOptions: {
                        stroke: true,
                        color: 'red',
                        weight: 3,
                        opacity: 0.5,
                        smoothFactor: 1
                    }
                })
            }
        ]
    }).addTo(map);
}

async function calculate() {
    const srcPoint = new L.LatLng(app.lat, app.lng);

    const result = await fetch('/api/calculate', {
        method: 'POST',
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(srcPoint)
    });
    const data = await result.json();
    const destPoint = new L.LatLng(data.lat, data.lng);
    drawVector(srcPoint, destPoint);
}

function initMap() {
    const mbAttr = 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
        '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
        'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        mbUrl = 'https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoiY2F1ZXRoZW5vcmlvIiwiYSI6ImNqcmZlOTVzbDI4MXU0NHA4Y3NnM3Q2dTkifQ.dB1mAnvB0oqVvb-k_ZNbcQ';

    const satelliteLayer = L.tileLayer(mbUrl, {
        id: 'mapbox.satellite',
        attribution: mbAttr
    });

    const map = L.map('map', {
        layers: [satelliteLayer]
    });

    fetch('/static/geodata/hot_area.json').then(function (response) {
        return response.json();
    }).then(function (data) {
        const areaQuenteLayer = L.geoJSON(data);
        map.fitBounds(areaQuenteLayer.getBounds());
        areaQuenteLayer.addTo(map);
    });

    return map
}


document.addEventListener('DOMContentLoaded', function() {
    window.map = initMap();
});
