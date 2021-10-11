# How Many Trees?
# Brief:
askjahsa

# Background and Rationale: 
Why does this exist? 

# The End Result
`gif here`

# Calculator Methodology: 
### Emissions in Metric Tonnes: 
Our in-house RESTful API used to calculate emissions per km were derived from the European Chemical Transport Association's *Guidelines for Measuring and Managing CO2
 Emission from Freight Transport Operations* report:

> `[1] CO2 emissions = Transport volume by transport mode (metric tonnes) x transport distance by transport mode (km) x average CO2-emissions per tonne-km by transport mode (g)`
>
> `[2] CO2 emissions in metric tonnes = (Eqn. 1) / 1000000`

Average CO2-emission factor per tonne-km and Transport volume by transport mode were taken from the DVLA Vehicle Enquiry Service API. Transport distance was taken from MapBox API. For our calculations, we have assumed that the transport volume is equal to the vehicles Gross Revenue Weight (GRW) in kilograms, which is defined by the DVLA as:

> *The maximum gross weight: fully laden passengers, luggage, and all.* 

We are assuming the GRW is a constant value across distance travelled. To ensure consistency in our calculations, we converted GRW into metric tonnes by dividing GRW by 1000

### How Many Trees: 
The calculation for converting CO2 in metric tonnes into a 'Tree Equivalent' is based on the average mature tree absorbing 21kg of CO2 per year. For simplicity sake, we are assuming all trees are average, all trees are mature, and all trees are eternal (hail trees). 

For a metric tonnage of CO2, 'Tree Equivalent' is calculated using Equn. 3 below:

> `[3] Tree Equivalent = (Eqn. 2) / 0.021`

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
