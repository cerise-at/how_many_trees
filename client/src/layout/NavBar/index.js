import React from 'react';
import { NavLink, useHistory } from 'react-router-dom';
import axios from 'axios';
import './style.css';

function NavBar() {

    const history = useHistory();

    async function logout() {
        try {
            // Is email or password needed to logout ???
            await axios.post(`${process.env.REACT_APP_API_URL}/rest-auth/logout/`);
        } catch (err) {
            console.log(err);
        }
        localStorage.clear();
        history.push('/');
    }

    return (
        <nav className="navbar sticky-top navbar-expand-md navbar-light p-0">

            <div className="container-fluid">

                <button className="navbar-toggler"
                        data-bs-toggle="collapse"
                        data-bs-target="#navbarSupportedContent"
                        aria-label="Toggle navigation">

                    <span className="navbar-toggler-icon"></span>
                </button>

                <span className="navbar-brand">How Many Trees?</span>

                <div className="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul className="navbar-nav me-auto mb-2 mb-lg-0">

                        <li className="nav-item">
                            <NavLink className="nav-link" to="/dashboard">Dashboard</NavLink>
                        </li>

                        <li className="nav-item">
                            <NavLink className="nav-link" to="/new-route">New Route</NavLink>
                        </li>

                        <li className="nav-item">
                            <NavLink className="nav-link" to="/portfolio">Portfolio</NavLink>
                        </li>

                        <li className="nav-item">
                            <NavLink className="nav-link" to="/offset">Offset Options</NavLink>
                        </li>
                    </ul>

                    <div className="d-flex">
                        <button className="btn" onClick={e => history.goBack()}>Back</button>

                        <button className="btn" onClick={logout}>Log out</button>
                    </div>
                </div>
            </div>
        </nav>
    )
}

export default NavBar;
