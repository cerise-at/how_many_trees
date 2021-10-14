import React from 'react';
import { NavBar } from '../../layout';
import { ProjectCards, NewProjectForm } from '../../components'

function Portfolio() {

    return (
        <>
            <NavBar />
            <ProjectCards/>
            <NewProjectForm/>
        </>
    );
}

export default Portfolio;
