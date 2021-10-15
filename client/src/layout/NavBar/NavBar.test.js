import { screen } from '@testing-library/react';
import NavBar from '.';
import {createMemoryHistory} from 'history'

describe('NavBar', () => {

    it('renders navigation bar with 4 nav links', () => {
        renderWithRouter(<NavBar />);

        const navBar = screen.getByRole('navigation');
        const links = screen.getAllByRole('link');

        expect(navBar).toBeInTheDocument();
        expect(links.length).toBe(4);
    });
});
