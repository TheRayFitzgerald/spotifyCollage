import React, { useState, useEffect } from 'react';
import { Col, Container, Row } from "reactstrap";
import '../css/Home.css';
import { ImageContainer } from "../styles/Home.styles"


import axios from "axios";

import { API_URL } from "../constants";

function Home(token) {
  console.log('Home');
  const [collage, setCollage] = useState('');

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

  // detect if the Spotify desktop app is already installed on the user's computer
  // if is set a variable to true
  // if not set a variable to false

  


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

  /*
  return (
    <h3>This is a Functional Component</h3>
  );
  */
  /*
  return (
    <Container style={{ marginTop: "20px" }}>
      <Row>
        <Col>
          {AlbumGrid(albums)}
        </Col>
      </Row>
    </Container>
  );
  */
}







export default Home;



/* 05/10 using collage object not album
function Home(token) {
  console.log('Home');
  const [albums, setAlbums] = useState('');

  useEffect(() => {
    resetState();  
  })
  
  const getAlbums = () => {
    // axios.get(API_URL).then(res => setAlbums({ albums: res.data }));
    axios.get(API_URL, {
      params: {
        token: token
      }
    }).then(
      res => setAlbums({ albums: res.data })
    );
  };
  
  const resetState = () => {
    getAlbums();
  };

  /*
  return (
    <h3>This is a Functional Component</h3>
  );
  */
/*
return (
  <Container style={{ marginTop: "20px" }}>
    <Row>
      <Col>
        {AlbumGrid(albums)}
      </Col>
    </Row>
  </Container>
);
*/






/*
class Home extends Component {
  state = {
    albums: []
  };

  componentDidMount() {
    this.resetState();
  }

  getAlbums = () => {
    axios.get(API_URL).then(res => this.setState({ albums: res.data }));
  };

  resetState = () => {
    this.getAlbums();
  };

  render() {
    return (
      <Container style={{ marginTop: "20px" }}>
        <Row>
          <Col>
            <AlbumGrid
              albums={this.state.albums}
              resetState={this.resetState}
            />
          </Col>
        </Row>
      </Container>
    );
  }
}
*/