import React from 'react';
import { Link } from 'react-router-dom';
// import { SimpleSlider } from "../../components/";
import './style.css';

function Landing() {

    return (
        <main>
            <div id="hero-image">
                <div className="card">
                    <h1 className="display-1">How Many Trees?</h1>
                    {/* <SimpleSlider /> */}
                    <div className="vw-100">
                        <div id="carouselExampleCaptions" className="carousel slide" data-bs-ride="carousel">
                            <div className="carousel-indicators">
                                <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                                <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
                                <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
                                <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="3" aria-label="Slide 4"></button>
                                <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="4" aria-label="Slide 5"></button>
                                <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="5" aria-label="Slide 6"></button>
                                <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="6" aria-label="Slide 7"></button>
                                <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="7" aria-label="Slide 8"></button>
                                <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="8" aria-label="Slide 9"></button>
                                <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="9" aria-label="Slide 10"></button>
                            </div>
                            <div className="carousel-inner">
                                <div className="carousel-item active">
                                <div className="carousel-caption">
                                    <h5>To offset my shipping emissions?</h5>
                                </div>
                                </div>
                                <div className="carousel-item">
                                <div className="carousel-caption">
                                    <h5>To make my business sustainable?</h5>
                                </div>
                                </div>
                                <div className="carousel-item">
                                <div className="carousel-caption">
                                    <h5>To remove one tonne of co2 from our air a year?</h5>
                                </div>
                                </div>
                                <div className="carousel-item">
                                <div className="carousel-caption">
                                    <h5>To make my breakfast carbon neutral?</h5>
                                </div>
                                </div>
                                <div className="carousel-item">
                                <div className="carousel-caption">
                                    <h5>To accountably deliver to my customers?</h5>
                                </div>
                                </div>
                                <div className="carousel-item">
                                <div className="carousel-caption">
                                    <h5>To take care of the future?</h5>
                                </div>
                                </div>
                                <div className="carousel-item">
                                <div className="carousel-caption">
                                    <h5>Should I plant to save the planet?</h5>
                                </div>
                                </div>
                                <div className="carousel-item">
                                <div className="carousel-caption">
                                    <h5>Does it take to change a lightbulb?</h5>
                                </div>
                                </div>
                                <div className="carousel-item">
                                <div className="carousel-caption">
                                    <h5>Crossed the road?</h5>
                                </div>
                                </div>
                                <div className="carousel-item">
                                <div className="carousel-caption">
                                    <h5>Could a woodchuck if a woodchuck could chuck trees?</h5>
                                </div>
                                </div>
                            </div>
                            </div>
                        </div> 
                    <section id="auth-buttons">
                        <Link to="/auth/login" role="button" className="btn">Login</Link>
                        <Link to="/auth/register" role="button" className="btn">Sign Up</Link>
                    </section>
                </div>
            </div>
        </main>
    );
}

export default Landing;
