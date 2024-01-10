import pygame
import random

# Constants
NUM_COLORS = 3
NUM_PARTICLES = 30

class Particle:
    def __init__(self, x: float, y: float, velocityX: float, velocityY: float, color: list[int]) -> None:
        self.x:float = x
        self.y:float = y
        self.velocityX:float = velocityX
        self.velocityY:float = velocityY
        self.color:list[int] = color

    def __str__(self) -> str:
        return f"Particle: {self.color} at Location {self.x, self.y}"


def generate_particles():
    particles = []

    # Determine how many particles are allocated to each color
    particles_per_color = NUM_PARTICLES // NUM_COLORS

    # Generate the colors based on the number of colors and fill with random RGB value
    colors_index = [[] for i in range(NUM_COLORS)]
    for color in colors_index:
        for i in range(3):
            color.append(random.randint(0, 255))

    # Generate all particles and assign color and random location
    for i in range(NUM_PARTICLES):
        color = colors_index[i // particles_per_color]
        x = random.random()
        y = random.random()

        particles.append(Particle(x, y, 0, 0, color))


def main():
    # generate all particles and assign them all a color and location
    particles = generate_particles(particles)

    for p in particles:
        print(p)

if __name__ == "__main__":
    main()