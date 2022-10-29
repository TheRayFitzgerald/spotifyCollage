import { Container } from "./styles/App.styles"
import Cookies from 'js-cookie'
import { SpotifyAuth, Scopes } from 'react-spotify-auth'
import 'react-spotify-auth/dist/index.css'
import React, { useState, useEffect } from 'react';
import { SpotifyAuthContainer, ImageContainer } from "./styles/App.styles"
import axios from "axios";
import { Dots } from 'loading-animations-react';
import Header from "./components/Header";
import Footer from './components/Footer';
import './css/App.scss';


const App = () => {
  const [token, setToken] = React.useState(Cookies.get("spotifyAuthToken"))
  const [collage, setCollage] = useState('');

  const getCollage = () => {
    if (collage === "") {
      console.log('getting collage');
      axios.get(process.env.REACT_APP_DJANGO_API_URL, {
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
          // <h1 className={"font-bold text-" + fontSize}>Hello World</h1>
          <img src={"data:image/png;base64," + collage['collage']['img_str']} alt="collage" style={{ alignSelf: 'center' }} />
          // <img src={collage['collage']['img']} alt="col99age" style={{ alignSelf: 'center' }} />
        ) : (
          // Display the loading dots
          <Dots id="loadingDots" text=""/>
        )}
        </ImageContainer>
      ) : (
        // Display the login page
        <SpotifyAuthContainer>
        <SpotifyAuth
          redirectUri={process.env.REACT_APP_REDIRECT_URI}
          clientID={process.env.REACT_APP_SPOTIFY_CLIENT_ID}
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