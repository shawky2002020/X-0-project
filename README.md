Tic Tac Toe Game
A 7x7 Tic Tac Toe game implemented using Angular, featuring various gameplay modes and AI difficulty levels.

Features
Game Modes:

Human vs. Human
Human vs. AI
AI vs. AI
Difficulty Levels:

Adjustable AI difficulty for both players.
At maximum difficulty, the AI is designed to win every time.
AI Implementation:

Utilizes Alpha-Beta Pruning with Iterative Deepening for decision-making.
Includes a time limit for the AI's move to enhance responsiveness.
User Interface:

Four main pages:
Start Page: Introduction and navigation options.
Mode Select: Choose the game mode.
Difficulty Select: Adjust the AI difficulty.
Game Board: Play the game with visual updates.
Installation
Prerequisites
Node.js (v14 or later)
Angular CLI (v15 or later)
Clone the Repository
bash
git clone https://github.com/shawky2002020/X-0-project.git
cd X-0-project
Install Dependencies
bash
npm install
Run the Application
bash
ng serve
Open your browser and navigate to http://localhost:4200 to play the game.

Usage
Start Page: Begin by selecting a game mode.
Mode Select: Choose between Human vs. Human, Human vs. AI, or AI vs. AI.
Difficulty Select: Set the difficulty level of the AI.
Game Board: Interact with the game board to make moves and view game status.
Contributing
Fork the repository.
Create a new branch (git checkout -b feature/your-feature-name).
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature/your-feature-name).
Create a new Pull Request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Angular - Framework used for building the application.
Alpha-Beta Pruning - Algorithm used for AI decision-making.
