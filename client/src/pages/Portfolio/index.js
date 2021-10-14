import React, { useState } from 'react';
import { NavBar } from '../../layout';
import { ProjectCards, NewProjectForm } from '../../components'

function Portfolio() {

    const [displayForm, setDisplayForm] = useState();

    return (
        <>
            <NavBar />
            <h1>Projects Portfolio</h1>
            <ProjectCards />
            <div className="d-flex flex-column align-items-center">
                <button className="btn btn-primary" onClick={e => setDisplayForm(prev => !prev)}>Add Project</button>
                { displayForm && <NewProjectForm /> }
            </div>
        </>
    );
}

export default Portfolio;
