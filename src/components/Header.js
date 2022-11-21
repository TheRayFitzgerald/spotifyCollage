import React, { Component } from "react";
import { HeaderContainer } from "../styles/Header.styles"
import "../css/Header.css"


class Header extends Component {
  render() {
    return (
        <HeaderContainer>
            <h1 style={{ fontWeight: 600 }} >🎸 Music Collage 🎺</h1>
            <h6>Create <strong>beautiful collages</strong> of your favorite Spotify music</h6>
        </HeaderContainer>
    );
  }
}

export default Header;