import React from 'react';
import profilePicture from '../assets/default-user.png';

const About = () => {
    return (
        <section id="about">
            <div className="profile-container">
                <img src={profilePicture} alt="Profile" className="profile-image" />
            </div>
            <h1>About Me</h1>
            <p>I'm a passionate web developer with 3 years of experience in creating modern web applications. I love coding and learning new technologies to enhance my skills.</p>
        </section>
    );
}

export default About;
