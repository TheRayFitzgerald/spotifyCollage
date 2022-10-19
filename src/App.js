import { Container } from "./styles/App.styles"
import Cookies from 'js-cookie'
import { SpotifyAuth, Scopes } from 'react-spotify-auth'
import 'react-spotify-auth/dist/index.css'
import React, { useState, useEffect } from 'react';
import './css/Home.css';
import { ImageContainer } from "./styles/Home.styles"
import { SpotifyAuthContainer } from "./styles/App.styles"
import axios from "axios";
import { Dots, ProgressBar } from 'loading-animations-react';
import Header from "./components/Header";
import Footer from './components/Footer';
import './css/App.css';

const App = () => {
  const [token, setToken] = React.useState(Cookies.get("spotifyAuthToken"))
  const [collage, setCollage] = useState('');

  const SPOTIFY_CLIENT_ID = '30a5904c955c4c92b9543e2f9bfb05c7' 
  const REACT_APP_REDIRECT_URI = "https://ancient-stream-51201.herokuapp.com"
  // const DJANGO_API_URL = "http://localhost:8000/api/albums/"
  const DJANGO_API_URL = "https://ancient-stream-51201.herokuapp.com/api/albums/"

  const getCollage = () => {
    if (collage === "") {
      console.log('getting collage');
      axios.get(DJANGO_API_URL, {
        params: {
          token: token
        }
      }).then(
        res => setCollage({ collage: res.data })
      );
    }
  };

  useEffect(() => {
    if (token && !collage) {
      console.log('useEffect');
      getCollage();
    }    
  }, [token]);

    
  return (
    <Container>
      <Header></Header>
      {token ? (
        <ImageContainer>
          {collage ? (
          // Display the collage
          <img src={collage['collage']['img']} alt="col99age" style={{ alignSelf: 'center' }} />
        ) : (
          // Display the loading dots
          <Dots id="loadingDots" text=""/>
        )}
        </ImageContainer>
      ) : (
        // Display the login page
        <SpotifyAuthContainer>
        <SpotifyAuth
          redirectUri={REACT_APP_REDIRECT_URI}
          clientID={SPOTIFY_CLIENT_ID}
          scopes={[Scopes.userTopRead]}
          onAccessToken={(token) => setToken(token)}
        />
        </SpotifyAuthContainer>
      )}
    <Footer />
    </Container>
  )
}
export default App