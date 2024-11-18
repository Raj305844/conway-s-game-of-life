Game of Life Simulation
This Python project is an interactive implementation of Conway's Game of Life, a zero-player game that evolves based on its initial configuration. The game is visualized using the Pygame library.

Features
Interactive Initialization: Use the mouse to create live cells on the grid.
Dynamic Grid Updates: Observe how the cells evolve based on Conway's rules.
Toggle Simulation: Start or stop the simulation using the spacebar.
Colorful Visuals: Watch live cells dynamically change colors when evolving.
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/game-of-life-simulation.git
Navigate to the project directory:
bash
Copy code
cd game-of-life-simulation
Install the required dependencies:
bash
Copy code
pip install pygame numpy
Usage
Run the script:
bash
Copy code
python main.py
Interact with the simulation:
Left-Click: Create live cells at the clicked location.
Spacebar: Start/stop the simulation.
Rules of the Game
The Game of Life follows these rules for cell updates:

Underpopulation: A live cell with fewer than two live neighbors dies.
Overpopulation: A live cell with more than three live neighbors dies.
Survival: A live cell with two or three live neighbors survives.
Reproduction: A dead cell with exactly three live neighbors becomes alive.
Customization
You can customize the grid size, cell size, and colors in the script:

Grid Size: Controlled by the box array dimensions.
Cell Size: Defined by the size parameter in the update function.
Colors: Modify color_bg, color_grid, and color_cell variables.