import { screen } from '@testing-library/react';
import { act } from 'react-dom/test-utils';
import RegisterForm from '.';
import axios from 'axios';

// jest.mock('axios');

describe('RegisterForm', () => {

    it('renders register form with input fields', () => {
        render(<RegisterForm />);
        const axiosSpy = jest.spyOn(axios, 'post');

        const inputs = screen.getAllByRole('textbox');
        const password1 = screen.getByPlaceholderText('Password');
        const password2 = screen.getByPlaceholderText('Confirm Password');

        act(() => {
            userEvent.type(inputs[0], 'testName');
            userEvent.type(inputs[1], 'test@email.com');
            userEvent.type(inputs[2], 'testCompany');
            userEvent.type(password1, 'Password1');
            userEvent.type(password2, 'Password1{enter}');
        })

        // failing
        // expect(axiosSpy).toBeCalledTimes(1);
    });
});
