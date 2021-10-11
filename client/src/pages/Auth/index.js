import React from 'react';
import { useHistory, useLocation } from 'react-router-dom';
import { LoginForm, RegisterForm } from '../../components';
import axios from 'axios';

function Auth() {

    const history = useHistory();
    const location = useLocation();
    const action = location.pathname.split('/')[2];

    async function login(e, userData, setError, setFuncs=null) {
        e.preventDefault();

        try {
            const { data } = await axios.post(`${process.env.REACT_APP_API_URL}/rest-auth/login/`, userData);
            console.log(data);
            if (data.hasOwnProperty !== 'token') { throw new Error(data.error) };

            localStorage.setItem('token', data.token);
            localStorage.setItem('email', data.email);
            history.push('/dashboard');
        } catch (err) {
            console.log(err);
            setError(err);
        }

        if (setFuncs) { setFuncs.forEach(func => func('')) };
    }

    if (action === 'login') { return <LoginForm login={login} /> }
    if (action === 'register') { return <RegisterForm login={login} /> }
}

export default Auth;
