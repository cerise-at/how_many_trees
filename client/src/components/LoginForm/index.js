import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import '../style.css';

function LoginForm({ login }) {

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState();
    const history = useHistory();

    return (
        <div id="hero-image" className='container d-flex vh-100 justify-content-center align-items-center'>
            <section id="login-form" className="d-flex flex-row">

                <form onSubmit={e => login(e, { email, password }, setError, [setEmail, setPassword])}
                    className="d-flex flex-column">

                    <input type="email"
                        name="email"
                        className="form-control mt-3"
                        value={email}
                        onChange={e => setEmail(e.target.value)}
                        placeholder="Email"
                        required />

                    <input type="password"
                        name="password"
                        className="form-control mt-3"
                        value={password}
                        onChange={e => setPassword(e.target.value)}
                        placeholder="Password"
                        required />

                    <input type="submit"
                        className="btn btn-outline-primary btn col-12"
                        value="Login" />

                    {error && <span role="alert" className="alert alert-danger">{error.message}</span>}

                </form>
            </section>

        </div>
    )
}

export default LoginForm;
