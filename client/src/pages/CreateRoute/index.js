import React, { useState } from 'react';
import { NavBar } from '../../layout';
import { useHistory } from 'react-router-dom';
import { NewRouteForm, Map, RoutesSelector } from '../../components';
import axios from 'axios';

function CreateRoute() {

    const [routesData, setRoutesData] = useState();
    const [error, setError] = useState(null);
    const [selectedRoute, setSelectedRoute] = useState({});
    const history = useHistory();

    async function getDirections(e, url) {
        e.preventDefault();

        try {
            const token = localStorage.getItem('token');
            const { data } = await axios.get(url, { headers: { "Authorization": `Token ${token}` }});

            //set the first route as default
            setSelectedRoute(data.routes[0]);
            setRoutesData(data.routes);
        } catch (err) {
            console.log(err);
            setError({ message: 'New route registration failed' });
        }
        // e.target.reset();
    }

    async function sendRoute(e) {
        e.preventDefault();

        try {
            const token = localStorage.getItem('token');
            const email = localStorage.getItem('email');
            const flatCoords = selectedRoute.coordinates.coordinates.flat();

            const n = localStorage.getItem('routeName');
            console.log(n);
            console.log('value', n.name);

            const data = { ...selectedRoute, email, coords: flatCoords, distance_km: selectedRoute.distance, name: 'route name' }
            console.log(data);

            await axios.post(`${process.env.REACT_APP_API_URL}/routes/create/`,
                data,
                { headers: { "Authorization": `Token ${token}` }}
            );

            // history.push('/dashboard');
        } catch (err) {
            console.log(err);
            setError(err);
        }
    }

    console.log(selectedRoute);
    console.log(routesData);

    return (
        <>
            <NavBar />
            { routesData
                ? <>
                    <h1>Select a Route</h1>
                    <main className="container row">

                        <Map selectedRoute={ selectedRoute }/>

                        <aside className="col-lg-4">
                            <h4>{selectedRoute.route_name}</h4>
                            <RoutesSelector routesData={ routesData } setSelectedRoute={ setSelectedRoute }/>

                        <button className="btn btn-primary" onClick={ e => sendRoute(e) }>Save Route</button>

                        { error && <p role="alert" className="alert alert-danger">{ error.message }</p> }
                        </aside>
                    </main>
                </>
                : <NewRouteForm getDirections={ getDirections } error={ error } setError={ setError } />
            }
        </>
    );
}

export default CreateRoute;
