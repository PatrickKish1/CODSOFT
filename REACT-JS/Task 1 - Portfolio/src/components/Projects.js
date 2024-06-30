import React, { useState } from 'react';
import project1 from '../assets/project1.png';
import project2 from '../assets/project2.png';
import project3 from '../assets/project3.png';

const projects = {
    project1: {
        title: 'Project 1: E-commerce Website',
        description: 'Developed a fully functional e-commerce website with a shopping cart and payment gateway integration.'
    },
    project2: {
        title: 'Project 2: Portfolio Website',
        description: 'Created a responsive portfolio website to showcase my projects and skills.'
    },
    project3: {
        title: 'Project 3: Blogging Platform',
        description: 'Built a blogging platform with user authentication and content management features.'
    }
};

const Projects = () => {
    const [selectedProject, setSelectedProject] = useState(null);

    const showProjectDetails = (projectId) => {
        setSelectedProject(projects[projectId]);
    };

    return (
        <section id="projects">
            <h1>Projects</h1>
            <div className="projects-container">
                <div className="project card" onClick={() => showProjectDetails('project1')}>
                    <img src={project1} alt="Project 1" />
                    <h2>Project 1: E-commerce Website</h2>
                </div>
                <div className="project card" onClick={() => showProjectDetails('project2')}>
                    <img src={project2} alt="Project 2" />
                    <h2>Project 2: Portfolio Website</h2>
                </div>
                <div className="project card" onClick={() => showProjectDetails('project3')}>
                    <img src={project3} alt="Project 3" />
                    <h2>Project 3: Blogging Platform</h2>
                </div>
            </div>
            {selectedProject && (
                <div id="project-details" className="project-details">
                    <h2>{selectedProject.title}</h2>
                    <p>{selectedProject.description}</p>
                </div>
            )}
        </section>
    );
}

export default Projects;
