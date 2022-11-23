import React, { Component } from "react";
import { HeaderContainer } from "../styles/Header.styles"
import { faHome } from "@fortawesome/free-solid-svg-icons";
import { faSpotify } from "@fortawesome/free-brands-svg-icons";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'

import "../css/Header.css"

//<img src={"./public/spotify_icon.png"} alt="not found"></img>
//<img src={require("./spotify_icon.png")} alt="not found"></img>

class Header extends Component {
  render() {
    return (
        <HeaderContainer>
            <h1 style={{ fontWeight: 600 }} ><FontAwesomeIcon icon={faSpotify} size="sm" /> Music Collage</h1>            
            <h6>Create <strong>beautiful collages</strong> of your favorite <strong>Spotify music</strong></h6>
        </HeaderContainer>
    );
  }
}

export default Header;