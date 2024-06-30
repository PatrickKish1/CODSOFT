import React from 'react';
import './styles.css';
import Header from './components/Header';
import About from './components/About';
import Skills from './components/Skills';
import Projects from './components/Projects';
import Recommendations from './components/Recommendation';
import AddRecommendation from './components/AddRecommendation';
import Footer from './components/Footer';

function App() {
    return (
        <div>
            <Header />
            <About />
            <Skills />
            <Projects />
            <Recommendations />
            <AddRecommendation />
            <Footer />
        </div>
    );
}

export default App;
