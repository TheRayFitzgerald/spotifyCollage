import React from "react";
import { Box, SocialIconContainer, SignatureContainer } from "../styles/Footer.styles";
import { SocialIcon } from 'react-social-icons';
import '../css/Footer.css';

const Footer = () => {
return (
	<Box>
        <SignatureContainer>Developed by <a href="https://twitter.com/rincidium" style={{color:"#1DB954"}}>Ray Fitzgerald</a> 2022.<br></br></SignatureContainer>
        <SocialIconContainer>
            <SocialIcon url="https://twitter.com/rincidium" style={{ height: 30, width: 30 }} bgColor="white"/>
            <SocialIcon url="https://github.com/TheRayFitzgerald" style={{ height: 30, width: 30 }} bgColor="white"/>
            <SocialIcon url="https://www.linkedin.com/in/ray-fitzgerald-86b451148/" style={{ height: 30, width: 30 }} bgColor="white" />
        </SocialIconContainer>
	</Box>
);
};
export default Footer;
