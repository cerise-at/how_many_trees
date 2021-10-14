import React, { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import axios from 'axios';

function ProjectCards() {

    const [projects, setProjects] = useState();
    const [error, setError] = useState();
    useEffect(() => getProjects(), []);
    async function getProjects() {
        try {
            const company = localStorage.getItem('company');
            const token = localStorage.getItem('token');

            const { data } = await axios.get(
                `${process.env.REACT_APP_API_URL}/projects/user/${company}`,
                { headers: { "Authorization": `Token ${token}` } }
            );
            console.log(data)
            setProjects(data)
            console.log(projects)

        } catch (err) {
            console.log(err);
            setError('Coud not fetch data');
        }
    }
    const renderCards = () => {
        return projects && projects.map((obj, i) =>
            <div class="card" style="width: 18rem;">
                {/* <img class="card-img-top" src="..." alt="Card image cap"> */}
                <div key={i} class="card-body">
                    <h5 className="card-title">{obj.title}</h5>
                    <h6 className="card-subtitle mb-2 text-muted">{obj.start_date}{obj.end_date}</h6>
                    <p className="card-text">{obj.description}</p>
                    <p className="card-text">{obj.offset_emissions_CO2e}</p>

                </div>
            </div>)
    }

    return (<>
        <div className="card-group">{renderCards()}</div>

    </>)
}



export default ProjectCards;
