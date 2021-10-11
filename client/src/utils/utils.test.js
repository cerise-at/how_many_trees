import { validate, isAuthenticated } from './utils';

describe('validate', () => {

    it('raises error if passwords do not match', () => {
        expect(() => validate('testPass1', 'testPass2'))
            .toThrow('Passwords do not match');
    });

    it('raises error if password is less than 8 characters long', () => {
        expect(() => validate('short', 'short'))
            .toThrow('Password must be at least 8 characters long');
    });

    it('raises error if password does not contain a number', () => {
        expect(() => validate('password', 'password'))
            .toThrow('Password must contain at least 1 number');
    });

    it('raises error if password does not contain uppercase letters', () => {
        expect(() => validate('password1', 'password1'))
            .toThrow('Password must contain both upper and lowercase letters');
    });

    it('raises error if password does not contain lowercase letters', () => {
        expect(() => validate('PASSWORD1', 'PASSWORD1'))
            .toThrow('Password must contain both upper and lowercase letters');
    });
});
