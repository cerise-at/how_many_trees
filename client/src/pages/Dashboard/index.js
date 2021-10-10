import React from 'react';
import { NavBar } from '../../layout';
import { RoutesList } from '../../components';

function Dashboard() {

    return (
        <>
            <NavBar />
            <div className="d-flex justify-content-center">
                <RoutesList />
            </div>
        </>
    );
}

export default Dashboard;
