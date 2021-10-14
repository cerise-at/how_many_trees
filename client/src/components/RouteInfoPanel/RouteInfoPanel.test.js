import { screen } from '@testing-library/react';
import RouteInfoPanel from '.';

const mockRouteDetails = {
    name: 'testRoute',
    distance_km: 234,
    emissions: 234,
    start_address: 'start address',
    end_address: 'end address'
}

describe('RouteInfoPanel', () => {

    it('renders panel with route details', () => {
        renderWithRouter(<RouteInfoPanel routeDetails={ mockRouteDetails }/>);
        const heading = screen.getByRole('heading');

        expect(heading.textContent).toBe('testRoute');
    })
})
