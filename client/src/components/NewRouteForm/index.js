import React, { useState } from 'react';

function NewRouteForm() {

    const [isReoccuring, setIsReoccuring] = useState(false);

    const renderOptions = () =>
        ['van', 'lorry', 'pickup'].map((type, i) =>
        <option key={i} value={type}>{type}</option>)

    const renderDates = () => 
        ['day', 'other day', 'week', 'two weeks', 'month'].map((date, i) =>
        <option key={i} value={date}>{date}</option>)

    return (
        <form className="container">
            <div className="address">
                <p className="h5">From:</p>

                <input type="text"
                        className="form-control col-md-12"
                        placeholder="Address"
                        required />

                <div className="row">
                    <input type="text"
                            className="form-control col-md"
                            placeholder="City"
                            required />

                    <input type="text"
                            className="form-control col-md"
                            placeholder="Post Code"
                            required />
                </div>
            </div>

            <div className="address">
                <p className="h5">To:</p>

                <input type="text"
                        className="form-control col-md-12"
                        placeholder="Address"
                        required />

                <div className="row">
                    <input type="text"
                            className="form-control col-md"
                            placeholder="City"
                            required />

                    <input type="text"
                            className="form-control col-md"
                            placeholder="Post Code"
                            required />
                </div>
            </div>

            <div>
                <p className="h5">Vehicle</p>

                <input type="text"
                        className="form-control"
                        placeholder="Registration Number"
                        required />

                <select defaultValue="" className="form-select">
                    <option value="" disabled hidden>Vehicle Class</option>
                    { renderOptions() }
                </select>
            </div>

            <div class="form-check">
                <input className="form-check-input"
                        type="checkbox"
                        value=""
                        id="datesCheckbox"
                        onChange={e => setIsReoccuring(e.target.checked)} />

                <label class="form-check-label" htmlFor="datesCheckbox">Multiple dates</label>
            </div>

            { isReoccuring &&
                <div>
                    <label htmlFor="datePicker">Choose Date:</label>
                    <input type="date" className="form-control"/>

                    <label htmlFor="freqSelector">Re-ocurring every:</label>
                    <select defaultValue="" className="form-select">
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
