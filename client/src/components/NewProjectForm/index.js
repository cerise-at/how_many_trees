import React, { useState } from 'react';
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import axios from 'axios';


function NewProjectForm()
{
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');
    const [offset, setOffset] = useState('');
    const [startDate, setStartDate] = useState('');
    const [endDate, setEndDate] = useState('')
    const [error, setError] = useState('')

    function handleSubmit(e) 
    {
        e.preventDefault();

        const email = localStorage.getItem('email');
        const token = localStorage.getItem('token');
        const company = localStorage.getItem('company');
        let formData;

        const url = `${process.env.REACT_APP_API_URL}/projects/create/?company=${company}&title=${title}&description=${description}&offset_emissions_CO2e=${offset}&start_date=${startDate}&end_date${endDate}/`;
        createProj(e, url)
    }

    async function createProj(e, url) 
    {
        e.preventDefault();

        try {
            const token = localStorage.getItem('token');
            const { formData } = await axios.post(url, { headers: { "Authorization": `Token ${token}` }});
  
        } catch (err) {
            console.log(err);
            setError({ message: 'New project registration failed' });
        }
    }
    return (
        <>
            <h1>Create a New Project</h1>
        <main className="d-flex justify-content-center">
            <form className="container row" id="new-project" onSubmit={e => handleSubmit(e)}>
                <div className="col-lg-6">
                    <div className="row">
                        <p className="h4">Project Title</p>
                            <input type="text"
                                    className="form-control"
                                    onChange={e => setTitle(e.target.value)}
                                    placeholder="Project Title"
                                    required />
                    </div>
                    <div className="row">
                        <p className="h4">Project Description</p>
                        <input type="textarea" maxlength="280"
                                className="form-control"
                                onChange={e => setDescription(e.target.value)}
                                placeholder="Project Description (280 characters or less)" />
                    </div>
                    <div className="row">
                        <p className="h4">Offset Amount</p>
                        <input type="number"
                                className="form-control"
                                onChange={e => setOffset(e.target.value)}
                                placeholder="Metric Tonne Offset (per year)" />
                    </div>
                    <div className="row">
                        <div className="col-sm-6">
                            <p className="h4">Start Date</p>
                            <DatePicker selected={startDate} onChange={(date) => setStartDate(date)} />
                        </div>        
                        <div className="col-sm-6">    
                            <p className="h4">End Date</p>
                            <DatePicker selected={endDate} onChange={(date) => setEndDate(date)} />
                        </div>   
                    </div>
                </div>
                <div className="d-flex justify-content-center">
                    <div className="d-flex flex-column">
                        <input type="submit"
                            className="btn btn-outline-primary"
                            value="Create New Project" />

                        { error && <p role="alert" className="alert alert-danger">{ error.message }</p> }
                    </div>
                </div>
            </form>
        </main>
    </>)
}
export default NewProjectForm;

