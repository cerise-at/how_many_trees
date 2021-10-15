import React from 'react';
import { Route, Redirect } from 'react-router-dom';
import { isAuthenticated } from '../../utils/utils';

/*
    Higher-order component for the 'Route' component
    Redirects to a protected route if user is logged in, else redirects to the landing page
*/

function PrivateRoute({ Component }) {

    return (
        <> isAuthenticated() ? <Component /> : <Redirect to='/' /> </>
    );
};

export default PrivateRoute;
