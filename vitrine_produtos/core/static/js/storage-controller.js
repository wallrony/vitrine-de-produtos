function saveAuthInfo(data) {
    localStorage.setItem('VP@USER', JSON.stringify(data['user']))
    localStorage.setItem('VP@AUTH_TOKEN', data['auth_token'])
}

function getAuthToken() {
    const token = localStorage.getItem('VP@AUTH_TOKEN')

    if (token === null) return undefined

    return token
}

function getUserInfo() {
    let user = localStorage.getItem('VP@USER')

    if (user === null) return undefined

    try {
        user = JSON.parse(user)
    } catch { }

    return user
}
