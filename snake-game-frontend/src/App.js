
//App.js

import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import Game from './components/Game';
import Leaderboard from './components/Leaderboard';
import Login from './components/Login';
import Signup from './components/Signup';
import './App.css';

function App() {
  const [gameStarted, setGameStarted] = useState(false);

  const handleStartClick = () => {
    setGameStarted(true);
  };

  return (
    <div className="App">
      <Router>
        <Navbar />
        {!gameStarted ? (
          <div className="start-screen">
            <h1>Welcome to Snake Game</h1>
            <button onClick={handleStartClick} className="start-button">
              Press Start
            </button>
          </div>
        ) : (
          <Routes>
            <Route path="/" element={<Game />} />
            <Route path="/leaderboard" element={<Leaderboard />} />
            <Route path="/login" element={<Login />} />
            <Route path="/signup" element={<Signup />} />
          </Routes>
        )}
      </Router>
    </div>
  );
}

export default App;
