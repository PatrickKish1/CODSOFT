import React from 'react';
import html5 from '../assets/html5.png';
import css3 from '../assets/css3.png';
import javascript from '../assets/javascript.png';

const Skills = () => {
    return (
        <section id="skills">
            <h1>Skills</h1>
            <div className="skills-container">
                <div className="skill card">
                    <img src={html5} alt="HTML5" />
                    <p>HTML5</p>
                </div>
                <div className="skill card">
                    <img src={css3} alt="CSS3" />
                    <p>CSS3</p>
                </div>
                <div className="skill card">
                    <img src={javascript} alt="JavaScript" />
                    <p>JavaScript</p>
                </div>
                <div className="skill card">
                    <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftactless7.github.io%2Fcv%2Fimg%2Ficons%2Freact_logo_2.png&f=1&nofb=1&ipt=6db4a193b03ed97ae9248b9d288af7ee2e8a7d59ae0038e5470bfa51ea8c73b3&ipo=images" alt="React" />
                    <p>React</p>
                </div>
            </div>
        </section>
    );
}

export default Skills;
