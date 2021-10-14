import React from 'react';
import { NavLink } from 'react-router-dom';
import { NavBar } from '../../layout';

function Offset() {

    return (
        <>
            <NavBar />
            <ComingSoon />
        </>
    );
}


const ComingSoon = () => {
    return (
        <>
            <div className='container vh-100 d-flex justify-content-center align-content-center'>
                <h1>Coming Soon!</h1>
            </div>
        </>
    )
}

export default Offset;
