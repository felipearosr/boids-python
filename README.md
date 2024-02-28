# Boids Python

This project is a pixel-based Boids simulation implemented in Python using the Pygame library. It demonstrates the principles of Boid behavior, such as alignment, cohesion, and separation, in a visually appealing pixel array format.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.x
- Pygame
- Numpy

You can install Pygame and Numpy using pip:

```bash
pip install pygame numpy
```
Installation

1.Clone the repository to your local machine:

```bash
git clone https://github.com/felipearosr/boids-python
```
2.Navigate into the project directory:

```bash
cd boids-python
```
3.Run the main file to start the simulation:

```bash
python main.py
```
## Configuration

The simulation can be customized through the settings.py file where you can adjust parameters such as screen size, number of boids, speed, and more.
Files

- `main.py`: The entry point of the application. It sets up the Pygame window and contains the main game loop.
- `boid.py`: Contains the BoidPix class which defines the behavior and properties of each boid.
- `surface.py`: Contains the SurfaceArray class which manages the pixel surface where boids are drawn.
- `settings.py`: Contains all configuration settings for the simulation.
- `vector.py`: Provides vector utilities, notably for rotating vectors.

## Acknowledgments

Nikolaus Stromberg for the original [PixelBoids](https://github.com/Nikorasu/PyNBoids/tree/main) concept and code.