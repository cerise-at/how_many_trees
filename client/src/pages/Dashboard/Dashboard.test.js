import { screen } from '@testing-library/react';
import { act } from 'react-dom/test-utils';
import Dashboard from '.';
import axios from 'axios';

jest.mock('axios');

const mockRes = { data: {
    first_name: 'testName',
    n_trees: 34,
    projects: [
        {
            project_title: 'testTitle',
            project_description: 'testDescription'
        }
    ],
    routes: [
        {
            id: 1,
            name: 'testRoute',
            emissions: 234,
            emissions_CO2e: 3445,
            emissions_CO2e_km: 5654

        }
    ]
}};


describe('Dashboard', () => {

    it('renders dashboard', () => {
        jest.spyOn(axios, 'get').mockResolvedValue(mockRes)
        act(() =>{
        renderWithRouter(<Dashboard />);
        });
        
        const heading = screen.getByRole('heading');
        expect(heading).toBeInTheDocument();
    });
});
