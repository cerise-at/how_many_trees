import React, { useState } from 'react';
import axios from 'axios';
import './style.css';

function NewRouteForm({ getDirections, error, setError }) {

    const [address1, setAddress1] = useState('');
    const [city1, setCity1] = useState('');
    const [postcode1, setPostcode1] = useState('');
    const [address2, setAddress2] = useState('');
    const [city2, setCity2] = useState('');
    const [postcode2, setPostcode2] = useState('');
    const [routeName, setRouteName] = useState('');
    const [vClass, setVClass] = useState();
    const [regNum, setRegNum] = useState('');
    const [isReoccuring, setIsReoccuring] = useState(false);
    const [date, setDate] = useState();
    const [freq, setFreq] = useState();

    const renderVehicleOptions = () =>
        ['van', 'lorry', 'pickup'].map((type, i) =>
        <option key={i} value={type}>{type}</option>)

    const renderFreqOptions = () =>
        ['day', 'other day', 'week', 'two weeks', 'month'].map((date, i) =>
        <option key={i} value={date}>{date}</option>)

    function handleSubmit(e) {
        e.preventDefault();

        const email = localStorage.getItem('email');
        const token = localStorage.getItem('token');
        let vehicleData;

        // check if user provided only the registration number or the vehicle class
        if ((!vClass && !regNum) || (vClass && regNum)) {
            setError({ message: 'You must provide either the registration number or vehicle class' });
            return;
        } else if (vClass){
            vehicleData = `vehicle_class=${vClass}`;
        } else if (regNum) {
            vehicleData = `registration_no=${regNum}`;
        }

        const url = `${process.env.REACT_APP_API_URL}/routes/directions/?email=${email}&route_name=${routeName}&address1=${address1},${city1},${postcode1}&address2=${address2},${city2},${postcode2}&${vehicleData}/`;
        getDirections(e, url)
    }

    return (
        <>
        <h1>Create a New Route</h1>
        <main className="d-flex justify-content-center">
            <form className="container row" id="new-route" onSubmit={e => handleSubmit(e)}>
                <div className="address col-lg-6">

                    <p className="h4">Address</p>
                    <p className="h5">From:</p>

                    <input type="text"
                            className="form-control"
                            onChange={e => setAddress1(e.target.value)}
                            placeholder="Street" />

                    <div className="container p-0">
                        <div className="row">

                            <div className="col-sm-8">
                                <input type="text"
                                        className="form-control"
                                        onChange={e => setCity1(e.target.value)}
                                        placeholder="City"
                                        required />
                            </div>

                            <div className="col-sm-4">
                                <input type="text"
                                        className="form-control"
                                        onChange={e => setPostcode1(e.target.value)}
                                        placeholder="Post Code"
                                        required />
                            </div>
                        </div>
                    </div>

                    <p className="h5">To:</p>

                    <input type="text"
                            className="form-control"
                            onChange={e => setAddress2(e.target.value)}
                            placeholder="Street"
                            required />

                    <div className="container p-0">
                        <div className="row">

                            <div className="col-sm-8">
                                <input type="text"
                                        className="form-control"
                                        onChange={e => setCity2(e.target.value)}
                                        placeholder="City"
                                        required />
                            </div>

                            <div className="col-sm-4">
                                <input type="text"
                                        className="form-control"
                                        onChange={e => setPostcode2(e.target.value)}
                                        placeholder="Post Code"
                                        required />
                            </div>
                        </div>
                    </div>
                </div>

                <div className="col-lg-6">
                    <div>
                        <p className="h4">Route Name</p>
                            <input type="text"
                                    className="form-control"
                                    onChange={e => setRouteName(e.target.value)}
                                    required />

                        <p className="h4">Vehicle</p>
                        <p>If you know the vehicle registration number, enter it below. Otherwise, select a generic vehicle class.</p>

                        <input type="text"
                                className="form-control"
                                onChange={e => setRegNum(e.target.value)}
                                placeholder="Registration Number" />

                        <select defaultValue=""
                                className="form-select"
                                onChange={e => setVClass(e.target.value)}>

                            <option value="" disabled hidden>Vehicle Class</option>
                            { renderVehicleOptions() }
                        </select>
                    </div>

                    <div className="form-check">
                        <input className="form-check-input"
                                type="checkbox" value=""
                                id="datesCheckbox"
                                onChange={e => setIsReoccuring(e.target.checked)} />

                        <label className="form-check-label" htmlFor="datesCheckbox">Multiple dates</label>
                    </div>

                    { isReoccuring &&
                        <div>
                            <label htmlFor="datePicker">Choose Date:</label>
                            <input type="date"
                                    className="form-control"
                                    onChange={e => setDate(e.target.value)}/>

                            <label htmlFor="freqSelector">Re-ocurring every:</label>
                            <select defaultValue="" className="form-select"
                                onChange={e => setFreq(e.target.value)}>
                                { renderFreqOptions() }
                            </select>
                        </div>
                    }
                </div>

                <div className="d-flex justify-content-center">
                    <div className="d-flex flex-column">
                        <input type="submit"
                            className="btn btn-outline-primary"
                            value="Create New Route" />

                        { error && <p role="alert" className="alert alert-danger">{ error.message }</p> }
                    </div>
                </div>
            </form>
        </main>
        </>
    )
}

export default NewRouteForm;
