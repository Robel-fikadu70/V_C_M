# Vacuum Cleaner Simulation

A Pygame simulation of a vacuum cleaner agent that cleans a grid environment.

## Features
- 5 by 5 grid with random dirt generation
- Visual agent movement
- Automatic cleaning logic
- Adjustable simulation speed

## Requirements
- Python 3.6+
- Pygame

## Installation
```bash
pip install pygame
```
## Usage

# Run the simulation:
```bash
python vacuumCleaner.py
```
## Controls

    - Automatically runs at 2 FPS

    - Close window to exit

## Customization

# Modify these variables in code:

    - grid_size: Change grid dimensions

    - cell_size: Adjust cell pixel size

    - clock.tick(2): Change simulation speed

## Initialize pygame and grid
### Main game loop:
-  1. Draw grid and agent
-  2. Move agent
-  3. Clean current cell if dirty