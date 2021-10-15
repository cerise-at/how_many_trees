import { screen } from '@testing-library/react';
import Landing from '.';

describe('Landing', () => {

    it('renders the landing page buttons',  () => {
        renderWithRouter(<Landing />);
        const btns = screen.getAllByRole('button');
        expect(btns.length).toBe(2);
    });
});
