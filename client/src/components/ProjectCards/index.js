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
           

            for (let i = 0; i < data.length; i++) { 
                let str  = new Date(data[i].start_date)
                str.toLocaleDateString()
                let start = `${str.getDate()}-${str.getMonth()}-${str.getFullYear()}`
                data.start_date = start

                let str2  = new Date(data[i].end_date)
                str2.toLocaleDateString()
                let end = `${str2.getDate()}-${str2.getMonth()}-${str2.getFullYear()}`
                data.end_date = end
              }

        } catch (err) {
            console.log(err);
            setError('Coud not fetch data');
        }
    }
    const renderCards = () => {
        return projects && projects.map((obj, i) =>
            <div className="card" style= {{width: "18rem"}}>
                {/* <img class="card-img-top" src="..." alt="Card image cap"> */}
                <div key={i} className="card-body">
                    <h5 className="card-title">{obj.title}</h5>
                    <h6 className="card-subtitle mb-2 text-muted">Start:{obj.start_date}  End:{obj.end_date}</h6>
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
