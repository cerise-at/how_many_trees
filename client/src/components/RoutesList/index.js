import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import './style.css';

function RoutesList({ routes }) {

    const [isPerKM, setIsPerKM] = useState(false);
    const history = useHistory();

    function renderBars(routes) {
        // sort the routes by CO2 emissions and return an array of bar elements

        const emissions = isPerKM ? 'emissions_CO2e_km' : 'emissions_CO2e';
        routes.sort((a, b) => b[emissions] - a[emissions]);

        const max = routes[0][emissions];
        const norm = (obj, max) => Math.floor(obj[emissions] * 100 / max);

        return (
            routes.map(obj =>
                <div key={obj.id} className="bar-container">

                    <span className="route-info">{obj.name}, {obj[emissions]}
                        {isPerKM ? <> CO<sub>2</sub>e/km</> : <> CO<sub>2</sub>e</>}
                    </span>

                    <div className="progress"
                        style={{width: `${norm(obj, max)}%`}}
                        onClick={e => history.push(`/route-details?${obj.id}`)}
                        key={obj.id}>

                        <div className="progress-bar w-100"
                            key={obj.id}
                            role="progressbar"
                            aria-valuenow="100"
                            aria-valuemin="0"
                            aria-valuemax="100">
                        </div>
                    </div>
                </div>
            )
        )
    }

    return (
        <div id="routes-window">
            <div className="d-flex align-items-center justify-content-between">

                <span className="h3">Active Routes</span>

                <div className="form-check form-switch">
                    <label className="form-check-label"
                            htmlFor="flexSwitchCheckDefault">
                            CO<sub>2</sub>e/km
                    </label>

                    <input className="form-check-input"
                            type="checkbox"
                            id="flexSwitchCheckDefault"
                            onChange={e => setIsPerKM(e.target.checked)}/>
                </div>
            </div>

            {renderBars(routes)}
        </div>
    )
}

export default RoutesList;
