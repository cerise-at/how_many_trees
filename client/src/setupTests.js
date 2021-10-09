import React from 'react';
import { Provider } from 'react-redux';
import { BrowserRouter } from 'react-router-dom';

import '@testing-library/jest-dom';
import "@testing-library/jest-dom/extend-expect";

import userEvent from "@testing-library/user-event";
import { render } from '@testing-library/react';
import { createStore, applyMiddleware } from 'redux';
import reducer from './redux/reducer'

const TestProviders = ({ initState }, history) => {
    initState ||= {};

    const testReducer = () => reducer(initState, { type: '@@INIT' });
    const testStore = createStore(testReducer);

    return ({ children }) => (
        <Provider store={testStore}>
            <BrowserRouter>
                { children }
            </BrowserRouter>
        </Provider>
    )
}

const renderWithReduxAndRouter = (uiElement, options={}) => {
    let TestWrapper = TestProviders(options)
    render(uiElement, { wrapper: TestWrapper, ...options })
}

const localStorageMock = {
  getItem: jest.fn(),
  setItem: jest.fn(),
  clear: jest.fn(),
};

global.renderWithReduxAndRouter = renderWithReduxAndRouter
global.React = React;
global.render = render;
global.userEvent = userEvent;
global.localStorage = localStorageMock;
