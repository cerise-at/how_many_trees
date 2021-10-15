import React from 'react';
import {  Redirect } from 'react-router-dom';


/*
    Higher-order component for the 'Route' component
    Redirects to dashboard page if a logged in user tries to access auth page
*/

function AuthRoute({ Component }) {

    return (
        <> {/*isAuthenticated() ? <Redirect to='/dashboard' /> : <Component />*/} <Component /> </>
    )
}

export default AuthRoute;
