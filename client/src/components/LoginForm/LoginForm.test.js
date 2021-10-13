import { screen } from '@testing-library/react';
import { act } from 'react-dom/test-utils';
import LoginForm from '.';
import axios from 'axios';

describe('RegisterForm', () => {

    it('renders form with input fields', () => {
        const axiosSpy = jest.spyOn(axios, 'post');
        renderWithReduxAndRouter(<LoginForm login={axiosSpy}/>);

        const email = screen.getByPlaceholderText('Email');
        const password = screen.getByPlaceholderText('Password');

        act(() => {
            userEvent.type(email, 'test@email.com');
            userEvent.type(password, 'Password1{enter}');
        })

        expect(axiosSpy).toBeCalledTimes(1);
    });
});
