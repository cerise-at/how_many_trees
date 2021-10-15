import React, { useState, useEffect } from 'react';
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

            const parseDate = (dateString)=> {
                let dateObject = new Date(dateString)
                return `${dateObject.getDate()}-${dateObject.getMonth()}-${dateObject.getFullYear()}`
            }
            for (let i = 0; i < data.length; i++) {
                data[i].start_date = parseDate(data[i].start_date)
                data[i].end_date = parseDate(data[i].end_date)
              }

              setProjects(data);
        } catch (err) {
            console.log(err);
            setError('Coud not fetch data');
        }
    }
    const renderCards = () =>
        projects.map((obj, i) =>
            <div className="card-component">
                {/* <img class="card-img-top" src="..." alt="Card image cap"> */}
                <div key={i} className="card-body">
                    <h5 className="card-title">{obj.title}</h5>
                    <h6 className="card-subtitle mb-">Start:{obj.start_date}  End:{obj.end_date}</h6>
                    <p className="card-text">{obj.description}</p>
                    <p className="card-text">{obj.offset_emissions_CO2e}</p>

                </div>
            </div>)

    return (
        <>
            <div className="d-flex flex-wrap flex-row justify-content-center">{projects && renderCards()}</div>
        </>
    )
}



export default ProjectCards;
