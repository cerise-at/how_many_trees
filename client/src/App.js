import React from 'react';
import { Route, Switch } from 'react-router-dom';
import { PrivateRoute, AuthRoute } from './components';
import {
    Auth,
    CreateRoute,
    Dashboard,
    Landing,
    Offset,
    Portfolio,
    RouteDetails,
    SelectRoute
} from './pages';

function App() {
    return (
        <Switch>
            <Route exact path='/'><Landing /></Route>

            <AuthRoute path='/auth/:action' Component={Auth}></AuthRoute>

            <PrivateRoute path='/new-route' Component={CreateRoute}></PrivateRoute>

            <PrivateRoute path='/select-route' Component={SelectRoute}></PrivateRoute>

            <PrivateRoute path='/route-details' Component={RouteDetails}></PrivateRoute>

            <PrivateRoute path='/dashboard' Component={Dashboard}></PrivateRoute>

            <PrivateRoute path='/portfolio'Component={Portfolio}></PrivateRoute>

            <PrivateRoute path='/offset' Component={Offset}></PrivateRoute>
        </Switch>
)}

export default App;
