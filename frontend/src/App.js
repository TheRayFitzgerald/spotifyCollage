import { Container } from "./styles/App.styles"
import Cookies from 'js-cookie'
import { SpotifyAuth, Scopes } from 'react-spotify-auth'
import 'react-spotify-auth/dist/index.css'
import React, { useState, useEffect } from 'react';
import './css/Home.css';
import { ImageContainer } from "./styles/Home.styles"
import axios from "axios";
import { API_URL } from "./constants";
import { Dots } from 'loading-animations-react';
import Header from "./components/Header";
//import { redirect } from "react-router-dom";
import {redirect} from 'react-router';

const App = () => {
  const [token, setToken] = React.useState(Cookies.get("spotifyAuthToken"))
  const [collage, setCollage] = useState('');

  const SPOTIFY_CLIENT_ID = '30a5904c955c4c92b9543e2f9bfb05c7' 
  const REACT_APP_REDIRECT_URI = "http://localhost:3000/"

  const getCollage = () => {
    axios.get(API_URL, {
      params: {
        token: token
      }
    }).then(
      res => setCollage({ collage: res.data })
    );
  };

  useEffect(() => {
    console.log('useEffect');
    getCollage();
  }, [token]);

    
  return (
    <Container>
      <Header></Header>
      {token ? (
        <ImageContainer>
          {collage ? (
          <img src={collage['collage']['img']} alt="collage" style={{ alignSelf: 'center' }} />
        ) : (
          <Dots />
        )}
        </ImageContainer>
      ) : (
        // Display the login page
        <SpotifyAuth
          redirectUri={REACT_APP_REDIRECT_URI}
          clientID={SPOTIFY_CLIENT_ID}
          scopes={[Scopes.userTopRead]} // either style will work
          onAccessToken={(token) => setToken(token)}
        />
      )}
    </Container>
  )
}
export default App

/*
function Home(token) {
  console.log('Home');
  

  useEffect(() => {
    resetState();  
  })
  
  const getCollage = () => {
    // axios.get(API_URL).then(res => setAlbums({ albums: res.data }));
    axios.get(API_URL, {
      params: {
        token: token
      }
    }).then(
      res => setCollage({ collage: res.data })
    );
  };
  
  const resetState = () => {
    getCollage();
  };
  // const img = collage['collage'] ? collage['collage']['img'] : null;

  return (    
      <ImageContainer>
        {collage ? (
        <img src={collage['collage']['img']} alt="collage" style={{ alignSelf: 'center' }} />
      ) : (
        <h2>no image</h2>
      )}
      </ImageContainer>
  );
  */
