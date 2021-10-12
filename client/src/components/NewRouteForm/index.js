import React, { useState } from 'react';
import axios from 'axios';

function NewRouteForm({ setRoutes, setError }) {

    const [address1, setAddress1] = useState('');
    const [city1, setCity1] = useState('');
    const [postcode1, setPostcode1] = useState('');
    const [address2, setAddress2] = useState('');
    const [city2, setCity2] = useState('');
    const [postcode2, setPostcode2] = useState('');
    const [vClass, setVClass] = useState();
    const [regNum, setRegNum] = useState('');
    const [isReoccuring, setIsReoccuring] = useState(false);
    const [date, setDate] = useState();
    const [freq, setFreq] = useState();

    const renderOptions = () =>
        ['van', 'lorry', 'pickup'].map((type, i) =>
        <option key={i} value={type}>{type}</option>)

    const renderDates = () =>
        ['day', 'other day', 'week', 'two weeks', 'month'].map((date, i) =>
        <option key={i} value={date}>{date}</option>)

    async function getDirections(e) {
        e.preventDefault();

        try {
            const email = localStorage.getItem('email');
            const token = localStorage.getItem('token');

            const url = `${process.env.REACT_APP_API_URL}/directions/?email=${email}&address1=${address1},${city1},${postcode1}&address2=${address2},${city2},${postcode2}&vehicle_class=${vClass}&registration_no=${regNum}`;
            console.log(url);

            //const { data } = axios.get(url, { headers: { "Authorization": token }});
            // setRoutes(data.routes);
        } catch (err) {
            console.log(err);
            setError(true);
        }
    }

    function handle(e) {
        e.preventDefault();
        console.log(e.target);
    }

    return (
        <form className="container" onSubmit={e => getDirections(e)}>
            <div className="address">
                <p className="h5">From:</p>

                <input type="text"
                        className="form-control col-md-12"
                        onChange={e => setAddress1(e.target.value)}
                        placeholder="Address" />

                <div className="row">
                    <input type="text"
                            className="form-control col-md"
                            onChange={e => setCity1(e.target.value)}
                            placeholder="City"
                            required />

                    <input type="text"
                            className="form-control col-md"
                            onChange={e => setPostcode1(e.target.value)}
                            placeholder="Post Code"
                            required />
                </div>
            </div>

            <div className="address">
                <p className="h5">To:</p>

                <input type="text"
                        className="form-control col-md-12"
                        onChange={e => setAddress2(e.target.value)}
                        placeholder="Address"
                        required />

                <div className="row">
                    <input type="text"
                            className="form-control col-md"
                            onChange={e => setCity2(e.target.value)}
                            placeholder="City"
                            required />

                    <input type="text"
                            className="form-control col-md"
                            onChange={e => setPostcode2(e.target.value)}
                            placeholder="Post Code"
                            required />
                </div>
            </div>

            <div>
                <p className="h5">Vehicle</p>

                <input type="text"
                        className="form-control"
                        placeholder="Registration Number"
                        onChange={e => setRegNum(e.target.value)}
                        required />

                <select defaultValue=""
                        className="form-select"
                        onChange={e => setVClass(e.target.value)}>

                    <option value="" disabled hidden>Vehicle Class</option>
                    { renderOptions() }
                </select>
            </div>

            <div className="form-check">
                <input className="form-check-input"
                        type="checkbox"
                        value=""
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
                    <select defaultValue="" className="form-select" onChange={e => setFreq(e.target.value)}>
                        { renderDates() }
                    </select>
                </div>
            }

            <input type="submit"
                    className="btn btn-outline-primary"
                    value="Create New Route" />
        </form>
    )
}

export default NewRouteForm;
