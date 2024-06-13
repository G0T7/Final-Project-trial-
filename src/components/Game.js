
//Game.js//

import React, { useState, useEffect } from 'react';
import './Game.css';

const Game = () => {
  const [snake, setSnake] = useState([{ x: 10, y: 10 }]);
  const [food, setFood] = useState({ x: 15, y: 15 });
  const [direction, setDirection] = useState('RIGHT');
  const [gameOver, setGameOver] = useState(false);

  useEffect(() => {
    const handleKeyDown = (e) => {
      switch (e.key) {
        case 'ArrowUp':
          setDirection('UP');
          break;
        case 'ArrowDown':
          setDirection('DOWN');
          break;
        case 'ArrowLeft':
          setDirection('LEFT');
          break;
        case 'ArrowRight':
          setDirection('RIGHT');
          break;
        default:
          break;
      }
    };
    document.addEventListener('keydown', handleKeyDown);

    return () => {
      document.removeEventListener('keydown', handleKeyDown);
    };
  }, []);

  useEffect(() => {
    const moveSnake = () => {
      const newSnake = [...snake];
      const head = { ...newSnake[0] };

      switch (direction) {
        case 'UP':
          head.y -= 1;
          break;
        case 'DOWN':
          head.y += 1;
          break;
        case 'LEFT':
          head.x -= 1;
          break;
        case 'RIGHT':
          head.x += 1;
          break;
        default:
          break;
      }

      newSnake.unshift(head);
      newSnake.pop();
      setSnake(newSnake);

      if (head.x === food.x && head.y === food.y) {
        newSnake.push({});
        setFood({
          x: Math.floor(Math.random() * 20),
          y: Math.floor(Math.random() * 20),
        });
      }

      if (
        head.x < 0 ||
        head.x >= 20 ||
        head.y < 0 ||
        head.y >= 20 ||
        newSnake.slice(1).some(segment => segment.x === head.x && segment.y === head.y)
      ) {
        setGameOver(true);
      }
    };

    if (!gameOver) {
      const interval = setInterval(moveSnake, 200);
      return () => clearInterval(interval);
    }
  }, [snake, direction, food, gameOver]);

  return (
    <div className="game-container">
      <h1>Snake Game</h1>
      <div id="game-board">
        {snake.map((segment, index) => (
          <div
            key={index}
            className="snake"
            style={{ top: `${segment.y * 5}%`, left: `${segment.x * 5}%` }}
          />
        ))}
        <div
          className="food"
          style={{ top: `${food.y * 5}%`, left: `${food.x * 5}%` }}
        />
      </div>
      {gameOver && <div className="game-over">Game Over</div>}
    </div>
  );
};

export default Game;