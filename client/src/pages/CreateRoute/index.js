import React, { useState } from 'react';
import { NavBar } from '../../layout';
import { NewRouteForm, Map } from '../../components';

function CreateRoute() {

    const [routes, setRoutes] = useState();
    const [error, setError] = useState();
    
    return (
        <>
            <NavBar />
            <NewRouteForm setRoutes={ setRoutes } setError={ setError }/>
            {/* <Map /> */}
        </>
    );
}

export default CreateRoute;
