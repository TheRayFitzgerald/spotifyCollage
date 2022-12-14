import React from "react";
import { Box, SocialIconContainer, SignatureContainer, SignatureContainer2 } from "../styles/Footer.styles";
import { SocialIcon } from 'react-social-icons';
// import '../css/Footer.css';
// <SignatureContainer>Developed by <a href="https://twitter.com/rincidium" style={{color:"#1DB954"}}>Ray Fitzgerald</a><br></br></SignatureContainer>
const Footer = () => {
    return (
        <Box>
        <SignatureContainer>Created by <a href="https://twitter.com/rincidium" style={{color:"black"}}>Ray Fitzgerald</a><br></br></SignatureContainer>
        <SignatureContainer2><a href="https://open.spotify.com/user/raynewspotify123?si=c73855c9820c49e0" style={{color:"black"}}>Follow me</a> on Spotify<br></br></SignatureContainer2>
            <SocialIconContainer>
                <SocialIcon url="https://twitter.com/rincidium" style={{ height: 29, width: 30, marginRight: "15px" }} bgColor="white"/>
                <SocialIcon url="https://github.com/TheRayFitzgerald" style={{ height: 30, width: 30, marginRight: "15px" }} bgColor="white"/>
                <SocialIcon url="https://www.linkedin.com/in/ray-fitzgerald-86b451148/" style={{ height: 30, width: 30 }} bgColor="white" />
            </SocialIconContainer>
        </Box>
    );
};
export default Footer;
