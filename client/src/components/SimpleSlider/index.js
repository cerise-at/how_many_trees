import React, { Component } from "react";
import Slider from "react-slick";
import "./style.css";

export default class SimpleSlider extends Component {
  render() {
    const settings = {
      infinite: true,
      speed: 500,
      slidesToShow: 1,
      slidesToScroll: 1,
      accessibility: true,
      autoplay: true,
      arrows: false,
    };
    return (
      <div>
        <h2> </h2>
        <Slider {...settings}>
          <div>
            <h3>To offset my shipping emissions?</h3>
          </div>
          <div>
            <h3>To make my business sustainable?</h3>
            <p></p>
          </div>
          <div>
            <h3>To eat one tonne of co2 a year?</h3>
            <p></p>
          </div>
          <div>
            <h3>To make my breakfast carbon neutral?</h3>
            <p></p>
          </div>
          <div>
            <h3>To accountably deliver to my customers?</h3>
            <p></p>
          </div>
          <div>
            <h3>To take care of the future?</h3>
            <p></p>
          </div>
          <div>
            <h3>Should I plant?</h3>
            <p></p>
          </div>
          <div>
            <h3>To save the Planet?</h3>
            <p></p>
          </div>
          <div>
            <h3>Does it take to change a lightbulb?</h3>
            <p></p>
          </div>
          <div>
            <h3>Crossed the road?</h3>
            <p></p>
          </div>
          <div>
            <h3>Can a woodchuck if a woodchuck could chuck trees?</h3>
            <p></p>
          </div>
        </Slider>
      </div>
    );
  }
}
