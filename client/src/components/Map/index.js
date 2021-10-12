import React, { useState, useEffect, useRef } from 'react';
import mapboxgl from 'mapbox-gl';
import 'mapbox-gl/dist/mapbox-gl.css';
import './style.css';
import axios from 'axios';

function Map() {

    const mapContainer = useRef(null);
    // const map = useRef(null);
    const [lng, setLng] = useState(-3.0);
    const [lat, setLat] = useState(54.0);
    const [zoom, setZoom] = useState(4.1);
    const [routes, setRoutes] = useState();

    mapboxgl.accessToken = process.env.REACT_APP_MAPBOX_TOKEN;

    useEffect(async () => {
        async function getRoutes() {
        try {
            const { data } = await axios.get('https://api.mapbox.com/directions/v5/mapbox/driving/-0.135565%2C51.497452%3B-1.553621125%2C53.806948625000004?alternatives=true&geometries=geojson&steps=true&access_token=pk.eyJ1Ijoiam9uMjM1N3Nub3ciLCJhIjoiY2t1bG0wNnZlMWlvajJxbjZwcHAwNmFrdiJ9.GVXEHdzU73nmvJUXP49_DQ')
            setRoutes(data.routes);
            console.log('routes inside', data.routes);
            return data.routes;
        } catch (err) {
            console.log(err);
        }
    }
        const routesData = await getRoutes();

        const map = new mapboxgl.Map({
            width: '100%',
            height: '100%',
            container: mapContainer.current,
            style: 'mapbox://styles/mapbox/streets-v11',
            center: [lng, lat],
            zoom: zoom
        });

        map.addControl(new mapboxgl.NavigationControl());

        console.log('routes outside', routesData[0].geometry);

        map.once("load", function () {
           map.addSource('route', {
               'type': 'geojson',
               'data': routesData[0].geometry
           });
           map.addLayer({
               'id': 'route',
               'type': 'line',
               'source': 'route',
               'layout': {
                   'line-join': 'round',
                   'line-cap': 'round'
               },
               'paint': {
                   'line-color': '#888',
                   'line-width': 8
               }
           });
       });


    }, []);

    return (
        <div>
            <div ref={mapContainer} className="map-container"></div>
        </div>
    )
}

export default Map;
