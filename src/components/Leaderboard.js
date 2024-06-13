import React, { useEffect, useState } from 'react';
import { fetchScores } from '../api';

const Leaderboard = () => {
  const [scores, setScores] = useState([]);

  useEffect(() => {
    const getScores = async () => {
      try {
        const { data } = await fetchScores();
        setScores(data);
      } catch (error) {
        console.error('Error fetching scores:', error);
      }
    };

    getScores();
  }, []);

  return (
    <div>
      <h1>Leaderboard</h1>
      <ul>
        {scores.map((score) => (
          <li key={score.id}>{score.user.username} - {score.score}</li>
        ))}
      </ul>
    </div>
  );
};

export default Leaderboard;
