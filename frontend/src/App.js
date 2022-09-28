import Home from "./components/Home";
import Login from "./components/Login";
import { Container } from "./styles/App.styles"

// const code = new URLSearchParams(window.location.search).get("code")
/*
function App() {

  return Home();
};
*/



import React from 'react'
import Cookies from 'js-cookie'

import { SpotifyAuth, Scopes } from 'react-spotify-auth'
import 'react-spotify-auth/dist/index.css'

const App = () => {
    const [token, setToken] = React.useState(Cookies.get("spotifyAuthToken"))
    console.log("token");
    console.log(token);

    const SPOTIFY_CLIENT_ID = '30a5904c955c4c92b9543e2f9bfb05c7' 
    const REACT_APP_REDIRECT_URI = "http://localhost:3000"
    
  return (
    <Container>
      {token ? (
        Home(token)
      ) : (
        // Display the login page
        <SpotifyAuth
          redirectUri={REACT_APP_REDIRECT_URI}
          clientID={SPOTIFY_CLIENT_ID}
          scopes={[Scopes.userReadPrivate, 'user-top-read']} // either style will work
          onAccessToken={(token) => setToken(token)}
        />
      )}
    </Container>
  )
}
export default App