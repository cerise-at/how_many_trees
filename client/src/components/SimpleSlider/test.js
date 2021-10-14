import { screen, render } from "@testing-library/react";
import SimpleSlider from '.';

describe('Slider', () => {
    beforeEach(() => {
        render(<SimpleSlider />);
    })

    test('renders a carousel', () => {
        const crsl = screen.getByRole(<SimpleSlider/>)
        expect(crsl.textContent).toContain('Quiz With Your Friends');
    })
})