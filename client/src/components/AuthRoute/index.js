import React from 'react';
import { Route, Redirect } from 'react-router-dom';
import { isAuthenticated } from '../../utils/utils';

/*
    Higher-order component for the 'Route' component
    Redirects to dashboard page if a logged in user tries to access auth page
*/

function AuthRoute({ Component }) {

    return (
        <> isAuthenticated() ? <Redirect to='/dashboard' /> : <Component /> </>
    )
}

export default AuthRoute;
