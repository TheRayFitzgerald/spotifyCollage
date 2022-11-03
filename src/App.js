import React, { useState, useEffect } from 'react';
import { Container } from "./styles/App.styles"
import {Helmet} from "react-helmet";
import Cookies from 'js-cookie'
import { SpotifyAuth, Scopes } from 'react-spotify-auth'
import 'react-spotify-auth/dist/index.css'
import { SpotifyAuthContainer, ImageContainer } from "./styles/App.styles"
import axios from "axios";
import { Dots } from 'loading-animations-react';
import Header from "./components/Header";
import Footer from './components/Footer';
import './css/App.scss';
import { TwitterShareButton, TwitterIcon } from 'react-share';



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
      <Helmet>
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:site" content="@nytimes" />
        <meta name="twitter:creator" content="@SarahMaslinNir" />
        <meta name="twitter:title" content="Parade of Fans for Houston’s Funeral" />
        <meta name="twitter:description" content="NEWARK - The guest list and parade of limousines with celebrities emerging from them seemed more suited to a red carpet event in Hollywood or New York than than a gritty stretch of Sussex Avenue near the former site of the James M. Baxter Terrace public housing project here." />
        <meta name="twitter:image" content="http://graphics8.nytimes.com/images/2012/02/19/us/19whitney-span/19whitney-span-articleLarge.jpg" />
      </Helmet>
      <Header></Header>
      {token ? (
        <ImageContainer>
          {collage ? (
            // Display the collage
            //<h1 className={"font-bold text-" + fontSize}>Hello World</h1>
            // <img src={collage['collage']['img']} alt="col99age" style={{ alignSelf: 'center' }} />
    
            <ImageContainer>
              <img src={"data:image/png;base64," + collage['collage']['img_str']} alt="collage" style={{ alignSelf: 'center' }} />
              
              <div className="tweet-div">
                <a  href="https://twitter.com/intent/tweet?text=Hello%20world">Tweet</a>
              </div>
            </ImageContainer>
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