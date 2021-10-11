import { screen } from '@testing-library/react';
import NavBar from '.';

describe('NavBar', () => {

    beforeEach(() => renderWithReduxAndRouter(<NavBar />));

    it('renders navigation bar', () => {
        const navBar = screen.getByRole('navigation');
        const links = screen.getAllByRole('link');

        expect(navBar).toBeInTheDocument();
        expect(links.length).toBe(6);
    });

    // test for each navlink when the respective pages are created
});
