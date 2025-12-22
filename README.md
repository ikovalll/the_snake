🐍 Snake Game (Python + Pygame)

A simple implementation of the classic Snake Game, built with Python and Pygame.

🎮 About

Control the snake, eat apples 🍎, and avoid colliding with your own body.
Each apple makes the snake longer — if you crash into yourself, the game restarts.

⚙️ Features

Clean, object-oriented architecture
(separate classes for Snake, Apple, and GameObject)

Smooth movement with keyboard controls

Random apple placement

Screen wrapping
(the snake reappears on the opposite side of the screen)

🚀 Installation & Run
1️⃣ Clone the repository or download the project
git clone https://github.com/your-username/snake-game.git
cd snake-game


Or download the archive and extract it manually.

2️⃣ Create and activate a virtual environment (recommended)

macOS / Linux:

python3 -m venv venv
source venv/bin/activate


Windows:

python -m venv venv
venv\Scripts\activate


After activation, (venv) should appear in your terminal.

3️⃣ Install dependencies

If requirements.txt exists:

pip install -r requirements.txt


Or install Pygame manually:

pip install pygame

4️⃣ Run the game
python the_snake.py


Use the arrow keys ⬆️⬇️⬅️➡️ to control the snake.

🧩 Dependencies

Python 3.8+

Pygame

💡 Notes

Using a virtual environment is recommended because it:

isolates project dependencies

avoids conflicts with other Python projects

makes development and future improvements easier

🔮 Future Improvements

Score tracking

Sound effects and menu system

Difficulty levels

Game over screen instead of instant restart

🛠️ Built With

Python 🐍

Pygame 🎮
