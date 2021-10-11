import React from 'react';
import { useHistory } from 'react-router-dom';
import './style.css';

function RoutesList() {

    const history = useHistory();

    // data passed as props from Dashboard page or loaded from redux store
    // dummy emissions data
    const data = [
        { id: 1, name: 'route 1', emissions: 56 },
        { id: 2, name: 'route 2', emissions: 123 },
        { id: 3, name: 'route 3', emissions: 200 },
        { id: 4, name: 'route 4', emissions: 98 },
        { id: 5, name: 'route 5', emissions: 46 },
        { id: 6, name: 'route 6', emissions: 23 },
        { id: 7, name: 'route 7', emissions: 178 }
    ]

    data.sort((a, b) => b.emissions - a.emissions)

    function renderBars(data) {
        const max = data[0].emissions;
        const norm = (obj, max) => Math.floor(obj.emissions * 100 / max)

        return (
            data.map(obj =>
                <div className="bar-container">

                    <p className="route-info">{obj.name}, {obj.emissions} units</p>

                    <div className="progress"
                        onClick={e => history.push(`/route-details?${obj.id}`)}
                        key={obj.id}>

                        <div className="progress-bar"
                            key={obj.id}
                            style={{width: `${norm(obj, max)}%`}}
                            role="progressbar"
                            aria-valuenow={`${norm(obj, max)}`}
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
            <p className="h3">Active Routes</p>
            {renderBars(data)}
        </div>
    )
}

export default RoutesList;
