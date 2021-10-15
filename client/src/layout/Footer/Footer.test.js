import { screen } from '@testing-library/react';
import Footer from '.';

describe('Footer', () => {

    it('renders footer', () => {
        render(<Footer />);
        const footer = screen.getByRole('contentinfo');
        expect(footer.textContent)
            .toBe('Created by Cerise Abel-Thompson, Owen Jenkins, Simon Allan & Mariusz Las');
    });
});
