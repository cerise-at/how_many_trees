import React from 'react';
import { Link } from 'react-router-dom';
import './style.css';

function Landing() {

    return (
        <main>
            <div id="hero-image">
                <div className="card d-flex justify-content-flex-start">
                    <div className="title-container w-100 d-flex justify-content-center">
                        <h1 className="display-1">How Many Trees...</h1>
                    </div>
                    <div className="w-100 d-flex justify-content-center">
                        {/* <hr /> */}
                        <div className="content-slider w-100 d-flex justify-content-center">
                            <div className="slider">
                                <div className="mask">
                                <ul>
                                    <li className="anim1">
                                    <div className="quote">...to offset my shipping emissions?</div>
                                    </li>
                                    <li className="anim2">
                                    <div className="quote">...to deliver sustainability to my customers?</div>
                                    </li>
                                    <li className="anim3">
                                    <div className="quote">...to make my business carbon neutral?</div>
                                    </li>
                                    <li className="anim4">
                                    <div className="quote">...does it take to draw down a tonne of CO2?</div>
                                    </li>
                                    <li className="anim5">
                                    <div className="quote">...to save the planet?</div>
                                    </li>
                                </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                    <section id="auth-buttons" className="w-100 d-flex justify-content-center">
                        <Link to="/auth/login" role="button" className="btn">Login</Link>
                        <Link to="/auth/register" role="button" className="btn">Sign Up</Link>
                    </section>
                </div>
            </div>
        </main>
    );
}

export default Landing;
