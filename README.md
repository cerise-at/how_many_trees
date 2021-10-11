# How Many Trees?
# Brief:
askjahsa

# Background and Rationale: 
Why does this exist? 

# The End Result
`gif here`

# Calculator Methodology: 
Our in-house RESTful API used to calculate emissions per km were derived from the European Chemical Transport Association's *Guidelines for Measuring and Managing CO2
 Emission from Freight Transport Operations* report:

> [1] CO2 emissions (g) = Transport volume by transport mode x transport distance by transport mode x average CO2-emission factor per km by transport mode
>
> [2] CO2 emissions in tonnes = (Eqn. 1) / 1000000

Average CO2-emission factor per tonne-km and Transport volume by transport mode were taken from the DVLA Vehicle Enquiry Service API. Transport distance was taken from MapBox API

For our calculations, we have assumed that the transport volume is equal to the vehicles Gross Revenue Weight (GRW) in kilograms, which is defined by the DVLA as:

> *The maximum gross weight: fully laden passengers, luggage, and all.* 

We are assuming the GRW is a constant value across distance travelled. 

## User Experience TODO:
[] Users should ...
[] Minimum 60% test coverage, with an aim of 80%

# Installation & Usage
## Installation

## Usage

## Change Log

# Technologies used:
## Frontend:
- HTML
- CSS
- React
- JSX
- Redux
- Redux-thunk
- Jest
- React-Testing-Library

## Backend:
- Django

# APIs consumed:
## External APIs:
- Google Maps API
-- Google Maps Directions API
- DVLA Vehicle Enquiry Service API

## Internal APIs:
- Django REST 

# Wins, Challenges, and Solutions:
## Wins
- 
## Challenges

## Challenge Solutions
- 
