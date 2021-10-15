import { screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import Auth from '.';
import axios from 'axios';

jest.mock('axios');

describe('Auth Page', () => {

    it('renders login form if redirected from login btn', () => {
        renderWithRouter(
            <MemoryRouter initialEntries={['/auth/login']}>
                <Auth />
            </MemoryRouter>
        );
        const loginForm = screen.getByRole('button', {name: /Login/g});
        const email = screen.getByPlaceholderText('Email');
        const password = screen.getByPlaceholderText('Password');

        // userEvent.type(email, 'user@email.com');
        // userEvent.type(password, 'Howmanytrees1{enter}');
        expect(loginForm).toBeInTheDocument();
    });

    it('renders sign up form if redirected from register btn',  () => {
        renderWithRouter(
            <MemoryRouter initialEntries={['/auth/register']}>
                <Auth />
            </MemoryRouter>
        );

        const signUpForm = screen.getByRole('button', {name: /Sign Up/g});
        expect(signUpForm).toBeInTheDocument();
    });
});
