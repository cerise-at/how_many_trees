import React, { useState } from 'react';
import axios from 'axios';

function RouteInfoPanel({ routeDetails }) {

    const [update, setUpdate] = useState(false);
    const [error, setError] = useState();

    async function sendUpdate(e) {
        e.preventDefault();

        try {
            const email = localStorage.getItem('email');
            const token = localStorage.getItem('token');

            axios.put(`${process.env.REACT_APP_API_URL}/`, {},
                { headers: { 'Authorization': `Token ${token}`}}
            ) // endpoint needed
            // what happens now???
        } catch (err) {
            console.log(err);
            setError({ message: 'Update failed'})
        }
    }

    return (
        <>
            <h4>{routeDetails.name}</h4>
            <p>Distance: {(routeDetails.distance_km/1000).toFixed(2)} km</p>
            <p>Emissions: {routeDetails.emissions}</p>
            <p>From: {routeDetails.start_address}</p>
            <p>To: {routeDetails.end_address}</p>

            <button className="btn btn-primary"
                onClick={e => setUpdate(prev => !prev)}>
                Update Vehicle Details
            </button>

            {/* form needed */}

            { error && <p role="alert" className="alert alert-danger">{ error.message }</p> }
        </>
    )
}

export default RouteInfoPanel;
