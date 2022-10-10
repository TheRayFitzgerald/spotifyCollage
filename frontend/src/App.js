import Home from "./components/Home";
import { Container } from "./styles/App.styles"
//import React from 'react'
import Cookies from 'js-cookie'

import { SpotifyAuth, Scopes } from 'react-spotify-auth'
import 'react-spotify-auth/dist/index.css'

import React, { useState, useEffect } from 'react';
import './css/Home.css';
import { ImageContainer } from "./styles/Home.styles"


import axios from "axios";

import { API_URL } from "./constants";


const App = () => {
  const [token, setToken] = React.useState(Cookies.get("spotifyAuthToken"))
  const [collage, setCollage] = useState('');

  const SPOTIFY_CLIENT_ID = '30a5904c955c4c92b9543e2f9bfb05c7' 
  const REACT_APP_REDIRECT_URI = "http://localhost:3000/callback"

  useEffect(() => {
    resetState();  
  })

  const getCollage = () => {
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
    
  return (
    <Container>
      {token ? (
        <ImageContainer>
          {collage ? (
          <img src={collage['collage']['img']} alt="collage" style={{ alignSelf: 'center' }} />
        ) : (
          <h2>no image</h2>
        )}
        </ImageContainer>
      ) : (
        // Display the login page
        <SpotifyAuth
          redirectUri={REACT_APP_REDIRECT_URI}
          clientID={SPOTIFY_CLIENT_ID}
          scopes={[Scopes.userReadPrivate, Scopes.userTopRead]} // either style will work
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
