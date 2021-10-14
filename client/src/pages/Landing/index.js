import React from 'react';
import { Link } from 'react-router-dom';
// import { SimpleSlider } from "../../components/";
import './style.css';

function Landing() {

    return (
        <main>
            <div id="hero-image">
                <h1 className="display-1">How Many Trees?</h1>
                {/* <SimpleSlider /> */}
                <section id="auth-buttons">
                    <div>
                        <Link to="/auth/login" role="button" className="btn">Login</Link>
                        <Link to="/auth/register" role="button" className="btn">Sign Up</Link>
                    </div>
                    </section>
            </div>
        </main>
    );
}

export default Landing;
