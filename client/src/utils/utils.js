function validate(password, passwordConf) {
    if (password !== passwordConf)
        { throw new Error('Passwords do not match') };

    if (password.length < 8)
        { throw new Error('Password must be at least 8 characters long') };

    if (!password.match(/[0-9]/g))
        { throw new Error('Password must contain at least 1 number') };

    if (!password.match(/[A-Z]/g) || !password.match(/[a-z]/g))
        { throw new Error('Password must contain both upper and lowercase letters')};
}

function isAuthenticated() {

    const token = localStorage.getItem('token');
    const isAuth = token ? true : false;
    return isAuth;
}

export { validate, isAuthenticated };
