import React from 'react';
import { NavLink, useHistory } from 'react-router-dom';
import './style.css';

function NavBar() {

    const history = useHistory();

    const goBack = () => history.goBack();

    const logout = () => localStorage.clear();

    return (
        <nav className="navbar sticky-top navbar-expand-md navbar-light">

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

                        {/*<li className="nav-item dropdown">
                            <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown">Menu</a>

                            <ul className="dropdown-menu" aria-labelledby="navbarDropdown">
                                <li><NavLink className="dropdown-item" to="/dashboard">Dashboard</NavLink></li>
                                <li><NavLink className="dropdown-item" to="/new-route">New Route</NavLink></li>
                                <li><NavLink className="dropdown-item" to="/portfolio">Portfolio</NavLink></li>
                                <li><NavLink className="dropdown-item" to="/offset">Offset Options</NavLink></li>
                            </ul>
                        </li>*/}
                    </ul>

                    <div className="d-flex">
                        <a className="nav-link" href="#" onClick={goBack}>Back</a>

                        <a className="nav-link" href="/" onClick={logout}>Log out</a>
                    </div>
                </div>
            </div>
        </nav>
    )
}

export default NavBar;
