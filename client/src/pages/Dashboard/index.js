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

    // useEffect(() => getDashboard());

    // async function getDashboard() {
    //     const { data } = axios.get(`${process.env.REACT_APP_API_URL}/dashboard`);
    //     // save data to state or redux store
    // }

    // dummy projects
    const data = [
        {project_title: 'Project 1', project_description: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
        {project_title: 'Project 2', project_description: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
        {project_title: 'Project 3', project_description: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."}
    ]

    function renderProjects(data) {
        return data.map((obj, i) =>
            <li key={i} class="list-group-item d-flex justify-content-between align-items-start">
                <div class="ms-2 me-auto">
                    <div class="fw-bold">{obj.project_title}</div>
                    {obj.project_description}
                </div>
            </li>
        )
    }

    return (
        <>
            <NavBar />
            <h1>Welcome, Corporate Ghouls!</h1>
            <main className="container">

                <div className="row">

                    <div className="col-lg">
                        <div>
                            <p className="h3">How many trees...?</p>
                            <p>You need to plant x trees per year to offset the company's CO2 emissions.</p>
                        </div>

                        <div>
                            <p className="h3">Active offsets</p>
                            <ul class="list-group">
                                {renderProjects(data)}
                            </ul>
                        </div>
                    </div>

                    <div className="col-lg">
                        <RoutesList />
                    </div>

                </div>
            </main>
        </>
    );
}

export default Dashboard;
