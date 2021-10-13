import React, { useState, useEffect } from 'react';
import { NavBar } from '../../layout';
import { RoutesList } from '../../components';
import axios from 'axios';
import './style.css';

function Dashboard() {

    const [username, setUsername] = useState();
    const [routes, setRoutes] = useState();
    const [projects, setProjects] = useState();
    const [trees, setTrees] = useState();

    useEffect(() => getDashboard(), []);

    async function getDashboard() {
        try{
            const email = localStorage.getItem('email');
            const token = localStorage.getItem('token');

            const { data } = await axios.get(
                `${process.env.REACT_APP_API_URL}/dashboard/${email}`,
                { headers: { "Authorization": `Token ${token}` } }
            );

            setUsername(data.first_name);
            setRoutes(data.routes);
            setTrees(data.n_trees);
            setProjects(data.projects);
        } catch (err) {
            console.log(err);
            // TO DO: add error handling
        }
    }

    function renderProjects(projects) {
        // render list of project names with short description

        return projects.map((obj, i) =>
            <li key={i} className="list-group-item d-flex justify-content-between align-items-start">
                <div className="ms-2 me-auto">
                    <div className="fw-bold">{obj.project_title}</div>
                    {obj.project_description}
                </div>
            </li>
        )
    }

    return (
        <>
            <NavBar />
            <h1>Welcome, {username}!</h1>
            <main className="container">

                <div className="row">

                    <div className="col-lg">
                        <div>
                            <p className="h3">How many trees...?</p>
                            <p>You need to plant {trees} trees per year to offset the company's CO<sub>2</sub> emissions.</p>
                        </div>

                        <div>
                            <p className="h3">Active offsets</p>
                            <ul className="list-group">
                                {renderProjects(projects)}
                            </ul>
                        </div>
                    </div>

                    <div className="col-lg">
                        <RoutesList routes={routes}/>
                    </div>

                </div>
            </main>
        </>
    );
}

export default Dashboard;
