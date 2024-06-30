import React from 'react';
import user1 from '../assets/user1.png';
import user2 from '../assets/user2.png';
import user3 from '../assets/user3.png';

const recommendations = [
    {
        img: user1,
        name: 'Jane Smith',
        text: 'Patrick is a highly skilled developer with a great eye for detail. He consistently delivers high-quality work.'
    },
    {
        img: user2,
        name: 'Mike Johnson',
        text: "Patrick's ability to understand and implement complex requirements is impressive. He's a great asset to any team."
    },
    {
        img: user3,
        name: 'Sarah Brown',
        text: 'Patrick is a proactive and dedicated professional. His contributions have been invaluable to our projects.'
    }
];

const Recommendations = () => {
    return (
        <section id="recommendations">
            <h1>Recommendations</h1>
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

export default Recommendations;
