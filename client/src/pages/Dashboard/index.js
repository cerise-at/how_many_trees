import React, { useState, useEffect } from 'react';
import { NavBar } from '../../layout';
import { RoutesList } from '../../components';
import axios from 'axios';
import './style.css';

function Dashboard() {

    const [company, setCompany] = useState();
    const [routes, setRoutes] = useState();
    const [projects, setProjects] = useState();
    const [trees, setTrees] = useState();
    const [error, setError] = useState();

    useEffect( async  () => {
        let comp = await getDashboard();
        getProjects(comp);
        }, []);

    async function getDashboard() {
        try {
            const email = localStorage.getItem('email');
            const token = localStorage.getItem('token');
            
            const { data } = await axios.get(
                `${process.env.REACT_APP_API_URL}/dashboard/${email}`,
                { headers: { "Authorization": `Token ${token}` } }
            )
            localStorage.setItem('company', data.company_name)
            
            setCompany(data.company_name);
            setRoutes(data.routes);
            setTrees(data.n_trees);
            return(data.company_name)

        } catch (err) {
            console.log(err);
            setError('Coud not fetch data');
        }
    }

    
        const getProjects = async (comp) => {
            try{
            // const comp = localStorage.getItem('company')
            const token = localStorage.getItem('token');
            const { data } = await axios.get(
                `${process.env.REACT_APP_API_URL}/projects/user/${comp}`,
                { headers: { "Authorization": `Token ${token}` } }
            );
                console.log('this is data', data)
            for (let i = 0; i < data.length; i++) {
                let str  = new Date(data[i].start_date)
                let start = `${str.getDate()}-${str.getMonth()}-${str.getFullYear()}`
                data[i].start_date = start
    
                let str2  = new Date(data[i].end_date)
                let end = `${str2.getDate()}-${str2.getMonth()}-${str2.getFullYear()}`
                data[i].end_date = end
              }

    
              setProjects(data);
              console.log('thisis', projects)
            }catch(err) {
                console.log(err);
                setError('Coud not fetch projects');

            }
        }
        // render list of project names with short description

        const renderProjects = () => {
            // render list of project names with short description

              return(
                  
                projects.map((obj, i) =>
                    <li key={i} className="list-group-item d-flex justify-content-between align-items-start">
                        <div className="ms-2 me-auto">
                            <div className="fw-bold">{obj.title}</div>
                            {obj.description}
                        </div>
                    </li>
                )
                  
            )}
     
        

    return (
        <>
            <NavBar />
            <div id="hero-image">
            <main className="container">
            <h1>Welcome, {localStorage.getItem('company')}!</h1>

                <div className="row treeContainer">
                    <div className="col-lg d-flex justify-content-center">
                        <div >
                            <p className="h3 container">How many trees...?</p>
                            { (trees >= 0.1)
                                ? <p>You need to plant {trees} trees per year to offset the company's CO<sub>2</sub> emissions.</p>
                                : <p>You don't have any emissions to offset! Woohoo!</p>
                            }
                        </div>
                    </div>
                </div >

                        <div className="row ">
                        <div className="col treeContainer m-1" >
                            <p className="h3">Active offsets</p>
                            <ul className="list-group">
                                { (projects && projects.length >= 1)
                                    ? renderProjects()
                                    : <p>Once you have registered an offset project they will appear here!</p>
                                }
                            </ul>
                        </div>
                        
                    <div className="col treeContainer m-1">
                        { (routes && routes.length >= 1) ? <RoutesList routes={routes} /> : null }
                    </div>
                        </div>

            </main >
            </div>
        </>
    );
}

export default Dashboard;
