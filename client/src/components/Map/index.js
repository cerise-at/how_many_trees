import React, { useState, useEffect, useRef } from 'react';
import mapboxgl from 'mapbox-gl';
import 'mapbox-gl/dist/mapbox-gl.css';
import './style.css';


function Map({ selectedRoute }) {

    const mapContainer = useRef(null);
    const [lng, setLng] = useState(-3.0);
    const [lat, setLat] = useState(54.5);
    const [zoom, setZoom] = useState(4.1);
    const [routes, setRoutes] = useState();

    console.log('selected route', selectedRoute);

    mapboxgl.accessToken = process.env.REACT_APP_MAPBOX_TOKEN;

    useEffect(async () => {

        const map = new mapboxgl.Map({
            width: '100%',
            height: '100%',
            container: mapContainer.current,
            style: 'mapbox://styles/mapbox/streets-v11',
            center: [lng, lat],
            zoom: zoom,
            maxZoom: 7
        });

        map.addControl(new mapboxgl.NavigationControl());

        map.once("load", function () {
           map.addSource('route', {
               'type': 'geojson',
               'data': selectedRoute.coordinates
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
                   'line-color': '#38b522',
                   'line-width': 6
               }
           });
       });


   }, [selectedRoute]);

    return (
        <div className="col-lg-8">
            <div ref={mapContainer} className="map-container"></div>
        </div>
    )
}

export default Map;
