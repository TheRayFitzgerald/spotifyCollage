import React, { Component } from "react";
import { HeaderContainer } from "../styles/Header.styles"
import "../css/Header.css"


class Header extends Component {
  render() {
    return (
        <HeaderContainer>
            <h1 style={{ fontWeight: 600 }} >🎸 Spotify Collage 🎺</h1>
            <h5>Generate beautiful collages of your favorite music</h5>
        </HeaderContainer>
    );
  }
}

export default Header;