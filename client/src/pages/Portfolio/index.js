import React from 'react';
import { NavBar } from '../../layout';
import { ProjectCards, NewProjectForm } from '../../components'

function Portfolio() {

    return (
        <>
            <NavBar />
            < NewProjectForm />
            <ProjectCards />
        </>
    );
}

export default Portfolio;
