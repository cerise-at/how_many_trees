import React, { useState } from 'react';
import { NavBar } from '../../layout';
import { NewRouteForm, Map, RoutesSelector } from '../../components';
import axios from 'axios';

function CreateRoute() {

    const [routesData, setRoutesData] = useState();
    const [error, setError] = useState(null);
    const [selectedRoute, setSelectedRoute] = useState({});

    console.log(selectedRoute);

    async function getDirections(e, url) {
        e.preventDefault();

        try {
            console.log(url);
            const token = localStorage.getItem('token');
            const { data } = axios.get(url, { headers: { "Authorization": `Token ${token}` }});
            setRoutesData(data);
            //set the first route as default
            selectedRoute(data[0]);
        } catch (err) {
            console.log(err);
            setError({ message: 'New route registration failed' });
        }
        // e.target.reset();
    }

    // dummy routesData
    // const routesData = [
    //     {
    //         id: 1,
    //         route_name: 'the first route',
    //         route_start: 'London',
    //         route_end: 'Leeds',
    //         emissions: 234,
    //         duration: 6435,
    //         distance: 123,
    //         geometry: []
    //     },
    //     {
    //         id: 2,
    //         route_name: 'the second route',
    //         route_start: 'London',
    //         route_end: 'Liverpool',
    //         emissions: 543,
    //         duration: 324324,
    //         distance: 43,
    //         geometry: []
    //     },
    //     {
    //         id: 3,
    //         route_name: 'the third route',
    //         route_start: 'London',
    //         route_end: 'Manchester',
    //         emissions: 4534,
    //         duration: 32454,
    //         distance: 676,
    //         geometry: []
    //     }
    // ]

    return (
        <>
            <NavBar />
            { routesData
                ? <>
                    <Map selectedRoute={ selectedRoute }/>
                    <aside>
                        {/*<div>
                            <h4>{selectedRoute.route_name}</h4>
                            <p>From: {selectedRoute.route_start}</p>
                            <p>To: {selectedRoute.route.end}</p>
                        </div>*/}
                        <RoutesSelector routesData={ routesData } setSelectedRoute={ setSelectedRoute }/>
                    </aside>
                </>
                : <NewRouteForm getDirections={ getDirections } error={ error } setError={ setError }/>
            }
        </>
    );
}

export default CreateRoute;
