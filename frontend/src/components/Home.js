import React, { useState, useEffect } from 'react';
import { Col, Container, Row } from "reactstrap";
import AlbumGrid from "./AlbumGrid";


import axios from "axios";

import { API_URL } from "../constants";

  


function Home() {
  const [albums, setAlbums] = useState('');

  useEffect(() => {
    this.resetState();  
  })

  const getAlbums = () => {
    axios.get(API_URL).then(res => setAlbums({ albums: res.data }));
  };

  const resetState = () => {
    getAlbums();
  };

  return (
    <Container style={{ marginTop: "20px" }}>
      <Row>
        <Col>
          <AlbumGrid
            albums={albums}
            resetState={resetState}
          />
        </Col>
      </Row>
    </Container>
  );
}


export default Home;

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