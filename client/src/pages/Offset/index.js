import React from 'react';
import { NavLink } from 'react-router-dom';
import { NavBar } from '../../layout';

function Offset() {

    return (
        <>
            <NavBar />
        </>
    );
}


const comingSoon = () => {
    return (
        <>
            <h1>Coming Soon!</h1>
            <NavLink to='dashboard'>Back to Home</NavLink>
        </>
    )
}

export default Offset;
