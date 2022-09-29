import React from "react"
import { LoginButton, LoginLink } from "../styles/Login.styles"

//const SOCIAL_AUTH_SPOTIFY_SECRET = '885d1d474fe4434688e8ff5049ff8df3'

const Login = () => {
    console.log('Login');
    const SPOTIFY_CLIENT_ID = '30a5904c955c4c92b9543e2f9bfb05c7' 
    const REACT_APP_REDIRECT_URI = "http://localhost:3000"
    const AUTH_URL = `https://accounts.spotify.com/authorize?client_id=${SPOTIFY_CLIENT_ID}&response_type=code&redirect_uri=${REACT_APP_REDIRECT_URI}&scope=streaming%20user-read-email%20user-read-private%20user-library-read%20user-library-modify%20user-read-playback-state%20user-modify-playback-state`

    return (
        <LoginButton>
            <LoginLink href={AUTH_URL}>Login with Spotify</LoginLink>
        </LoginButton>
    );
}

export default Login