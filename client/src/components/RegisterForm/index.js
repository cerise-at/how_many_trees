import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import axios from 'axios';
import { validate } from '../../utils/utils';
import '../style.css';

function RegisterForm({ login }) {

    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [passwordConf, setPasswordConf] = useState('');
    const [error, setError] = useState();
    const history = useHistory();

    async function register(e) {
        e.preventDefault();

        try {
            validate(password, passwordConf);

            const { data } = await axios.post(
                `${process.env.REACT_APP_API_URL}/register`,
                { username, email, password }
            );
            // check for error msg in response, else login
            data.hasOwnProperty === 'error'
                ? throw new Error(data.error)
                : login(e, {email, password}, setError);

        } catch (err) {
            console.log(err);
            setError(err);
        }

        setEmail('');
        setPassword('');
        setUsername('');
        setPasswordConf('');
    };

    return (
        <section id="register-form" className="d-flex flex-row">

            <form onSubmit={register} className="d-flex flex-column">

                <input type="text"
                        className="form-control-lg mt-3"
                        value={username}
                        onChange={e => setUsername(e.target.value)}
                        placeholder="Username"
                        required />

                <input type="email"
                        className="form-control-lg mt-3"
                        value={email}
                        onChange={e => setEmail(e.target.value)}
                        placeholder="Email"
                        required />

                <input type="password"
                        className="form-control-lg mt-3"
                        value={password}
                        onChange={e => setPassword(e.target.value)}
                        placeholder="Password"
                        required />

                <input type="password"
                        className="form-control-lg mt-3"
                        value={passwordConf}
                        onChange={e => setPasswordConf(e.target.value)}
                        placeholder="Confirm Password"
                        required />

                <input type="submit"
                        className="btn btn-outline-primary btn-lg col-12"
                        value="Sign Up" />

                { error && <span role="alert" className="alert alert-danger">{ error.message }</span> }

            </form>
        </section>
    )
}

export default RegisterForm;