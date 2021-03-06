import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import axios from 'axios';
import { validate } from '../../utils/utils';
import '../style.css';

function RegisterForm({ login }) {

    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [company, setCompany] = useState('');
    const [password1, setPassword1] = useState('');
    const [password2, setPassword2] = useState('');
    const [error, setError] = useState();
    const history = useHistory();

    async function register(e) {
        e.preventDefault();

        try {
            validate(password1, password2);

            const { data } = await axios.post(
                `${process.env.REACT_APP_API_URL}/rest-auth/registration/`,
                { name, email, company, password1, password2 }
            );

            history.push('/auth/login');
        } catch (err) {
            setError(err);
            console.log(err);
        }

        setEmail('');
        setPassword1('');
        setCompany('');
        setName('');
        setPassword2('');
    };

    return (
        <section id="hero-image" className="d-flex vh-100 justify-content-center align-items-center">

            <form id="register-form" onSubmit={register} className="d-flex flex-column">

                <input type="text"
                        className="form-control mt-3"
                        value={name}
                        onChange={e => setName(e.target.value)}
                        placeholder="First Name"
                        required />

                <input type="email"
                        className="form-control mt-3"
                        value={email}
                        onChange={e => setEmail(e.target.value)}
                        placeholder="Email"
                        required />

                <input type="text"
                        className="form-control mt-3"
                        value={company}
                        onChange={e => setCompany(e.target.value)}
                        placeholder="Company"
                        required />

                <input type="password"
                        className="form-control mt-3"
                        value={password1}
                        onChange={e => setPassword1(e.target.value)}
                        placeholder="Password"
                        required />

                <span id="password-info">Use 8 or more characters with a mix of upper and lowercase letters & numbers</span>

                <input type="password"
                        className="form-control mt-3"
                        value={password2}
                        onChange={e => setPassword2(e.target.value)}
                        placeholder="Confirm Password"
                        required />

                <input type="submit"
                        className="btn btn-outline-primary btn col-12"
                        value="Sign Up" />

                { error && <span role="alert" className="alert alert-danger">
                    Registration failed. Try different email or password.</span> }

            </form>
        </section>
    )
}

export default RegisterForm;
