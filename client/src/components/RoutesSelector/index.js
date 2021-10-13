import React, { useState } from 'react';

function RoutesSelector({ routesData, setSelectedRoute }) {

    const [sortBy, setSortBy] = useState('duration');
    // TO DO: implement sorting

    const selectRoute = (e, id) => {
        e.preventDefault()
        const route = routesData.filter(route => route.id === id);
        setSelectedRoute(route[0]);
    }

    const renderRouteOptions = () =>
        routesData.map(route =>
            <label  key={route.id} class="list-group-item">
                 <input class="form-check-input me-1"
                        type="radio" name="route"
                        onInput={e => selectRoute(e, route.id)}/>
                  {route.route_name}
            </label>
        )

    const renderSortOptions = () =>
        ['duration', 'distance', 'emissions'].map((item, i) =>
            <li>
                <button key={i} class="dropdown-item"
                    type="button" name={item}>
                {item}
                </button>
            </li>
        )

    return (
        <>
            <div className="d-flex justify-content-between">
                <h4>Route Alternatives</h4>

                <div class="dropdown">

                    <button class="btn btn-primary dropdown-toggle"
                            type="button" id="dropdownMenu2"
                            data-bs-toggle="dropdown" aria-expanded="false">
                            Sort By
                    </button>
                    
                    <ul class="dropdown-menu" aria-labelledby="dropdownMenu2">
                        { renderSortOptions() }
                    </ul>
                </div>

            </div>

            <div class="list-group">
                { renderRouteOptions() }
            </div>
        </>
    )
}

export default RoutesSelector;