import React from 'react';
import { BrowserRouter } from 'react-router-dom';
import '@testing-library/jest-dom';
import "@testing-library/jest-dom/extend-expect";
import userEvent from "@testing-library/user-event";
import { render } from '@testing-library/react';

// cutom test wrapper for react router
const TestProviders = () => {

    return ({ children }) => (
        <BrowserRouter>
            { children }
        </BrowserRouter>
    );
};

const renderWithRouter = (uiElement) => {
    const TestWrapper = TestProviders();
    render(uiElement, { wrapper: TestWrapper });
};

const localStorageMock = {
    getItem: jest.fn(),
    setItem: jest.fn(),
    clear: jest.fn(),
};

// mock a mapbox-gl dependency invoked by Auth tests
window.URL.createObjectURL = () => {}

global.renderWithRouter = renderWithRouter
global.React = React;
global.render = render;
global.userEvent = userEvent;
global.localStorage = localStorageMock;
