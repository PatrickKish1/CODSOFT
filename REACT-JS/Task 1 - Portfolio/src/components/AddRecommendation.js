import React, { useState } from 'react';
import defaultUser from '../assets/default-user.png';

const AddRecommendation = () => {
    const [recommendations, setRecommendations] = useState([]);
    const [recommendationText, setRecommendationText] = useState('');
    const [recommenderName, setRecommenderName] = useState('');

    const addRecommendation = () => {
        if (recommendationText && recommenderName) {
            const newRecommendation = {
                img: defaultUser,
                name: recommenderName,
                text: recommendationText
            };

            setRecommendations([...recommendations, newRecommendation]);
            setRecommendationText('');
            setRecommenderName('');
        } else {
            alert('Please enter both a recommendation and a name.');
        }
    };

    return (
        <section id="add-recommendation">
            <h1>Add a Recommendation</h1>
            <form id="recommendation-form">
                <textarea
                    id="new-recommendation"
                    placeholder="Enter your recommendation here..."
                    value={recommendationText}
                    onChange={(e) => setRecommendationText(e.target.value)}
                ></textarea>
                <input
                    type="text"
                    id="recommender-name"
                    placeholder="Your Name"
                    value={recommenderName}
                    onChange={(e) => setRecommenderName(e.target.value)}
                />
                <button type="button" onClick={addRecommendation}>Add Recommendation</button>
            </form>
            <div className="recommendations-container">
                {recommendations.map((rec, index) => (
                    <div key={index} className="recommendation card">
                        <div className="profile-pic">
                            <img src={rec.img} alt={`User ${index + 1}`} />
                        </div>
                        <div className="recommendation-content">
                            <span className="username">{rec.name}</span>
                            <p>"{rec.text}"</p>
                        </div>
                    </div>
                ))}
            </div>
        </section>
    );
}

export default AddRecommendation;
