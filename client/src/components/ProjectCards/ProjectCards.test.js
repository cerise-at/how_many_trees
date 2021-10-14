import { screen } from '@testing-library/react';
import { act } from 'react-dom/test-utils';
import ProjectCards from '.';
import axios from 'axios';

jest.mock('axios');
// jest.mock('axios');
const mockRes = { data: 
    {
        title: 'testTitle1',
        startDate: 'testName',
        endDate: 'testName',
        description: 'this is a very valid description for project 1',
        offset: 40
    }, data2: {
        title: 'testTitle2',
        startDate: 'testName',
        endDate: 'testName',
        description: 'this is a very valid description for project 2',
        offset: 40
    }

    
}
describe('ProjectCards', () => {
        it('renders project cards', () => {
            jest.spyOn(axios, 'get').mockResolvedValue(mockRes)
            act(() =>{
            render(<ProjectCards />);
            });
            
            const heading = screen.getByRole('heading');
            expect(heading).toBeInTheDocument();
    });
});
