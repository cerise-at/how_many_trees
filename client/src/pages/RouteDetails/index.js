import React, { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';
import { NavBar } from '../../layout';
import { Map, RouteInfoPanel } from '../../components';
import axios from 'axios';

function RouteDetails() {

    const [routeDetails, setRouteDetails] = useState();
    const [error, setError] = useState(true);
    const location = useLocation();
    const route_id = location.pathname.split('/')[2];

    useEffect(() =>  getRouteDetails(), []);

    async function getRouteDetails() {
        try {
            const email = localStorage.getItem('email');
            const token = localStorage.getItem('token');

            const { data } = await axios.get(`${process.env.REACT_APP_API_URL}/routes/${route_id}`,
                { headers: { "Authorization": `Token ${token}` } }
            );

            console.log(data);

            setRouteDetails(data);
        } catch (err) {
            console.log(err);
            setError(true);
        }
    }

    return (
        <>
            <NavBar />
            {
                routeDetails
                ? <>
                    <h1>Route Details</h1>
                    <main className="container row">

                        {/*<Map selectedRoute={ routeDetails }/> */}
                        <aside className="col-lg-4">
                            <RouteInfoPanel routeDetails={ routeDetails } />
                        </aside>
                    </main>
                </>
                : <p className="alert" role="alert alert-danger">Could not retrieve data</p>
            }
        </>
    );
}

export default RouteDetails;
