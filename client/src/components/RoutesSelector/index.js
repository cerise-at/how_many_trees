import React, { useState } from 'react';

function RoutesSelector({ routesData, setSelectedRoute }) {

    const [sortBy, setSortBy] = useState('duration');

    const selectRoute = (e, id) => {
        e.preventDefault()
        const route = routesData.filter(route => route.route_id === id);
        setSelectedRoute(route[0]);
    }

    const renderRouteOptions = () => {
        routesData.sort((a, b) => a[sortBy] - b[sortBy]);

        return routesData.map(route =>
            <label  key={route.id} className="list-group-item">
                 <input className="form-check-input me-1"
                        type="radio" name="route"
                        onInput={e => selectRoute(e, route.route_id)}/>
                  {route[sortBy]}
            </label>
        )
    }

    const getCorrectMetric = (sortBy) => {
        switch (sortBy) {
            case 'distance':
                return 'km';
            case 'duration':
                return 'hrs';
            case 'emissions':
                return 'CO2e'
            default:
                return ''
        }
    }

    const renderSortOptions = () =>
        [['duration', 'h'], ['distance', 'km'], ['emissions', 'CO2']].map((item, i) =>
            <li>
                <button key={i} className="dropdown-item"
                    type="button" name={item[0]}
                    onClick={e => setSortBy(e.target.name)}>
                    {item[0]} ({item[1]})
                </button>
            </li>
        )

    return (
        <>
            <div className="d-flex justify-content-between align-items-center">
                <h4>Route Alternatives</h4>

                <div className="dropdown">

                    <button className="btn btn-primary dropdown-toggle"
                            type="button" id="dropdownMenu2"
                            data-bs-toggle="dropdown" aria-expanded="false">
                            Sort By
                    </button>

                    <ul className="dropdown-menu" aria-labelledby="dropdownMenu2">
                        { renderSortOptions() }
                    </ul>
                </div>

            </div>

            <div className="list-group">
                { renderRouteOptions() }
            </div>
        </>
    )
}

export default RoutesSelector;
