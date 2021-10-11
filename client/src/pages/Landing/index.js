import React from 'react';
import { Link } from 'react-router-dom';
import './style.css';

function Landing() {

    return (
        <main>
            <div className="p-5 bg-primary text-white">
                <h1 className="display-1">How Many Trees?</h1>
                <p className="">Under title</p>
            </div>

            <section id="auth-buttons">
                <div>
                    <Link to="/auth/login" role="button" className="btn btn-outline-primary">Login</Link>
                    <Link to="/auth/register" role="button" className="btn btn-outline-primary">Sign Up</Link>
                </div>
            </section>
        </main>
    );
}

export default Landing;
