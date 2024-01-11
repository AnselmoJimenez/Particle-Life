import pygame
import random
import math

class Particle:
    def __init__(self, x: int, y: int, velocityX: float, velocityY: float, color: list[int]) -> None:
        self.x:float = x
        self.y:float = y
        self.velocityX:float = velocityX
        self.velocityY:float = velocityY
        self.color:list[int] = color

    def __str__(self) -> str:
        return f"Particle: {self.color} at Location {self.x, self.y}"


class Simulation:
    def __init__(self) -> None:
        self.width = 1024
        self.height = 1024
        self.number_of_colors = 3
        self.number_of_particles = 30

        self.delta_time = 0.2
        self.repulsion_distance = 0.3

        self.attraction_matrix = self.generate_attraction_matrix()
        self.particles, self.color_dictionary = self.generate_particles()
        print(self.color_dictionary)
        self.mainloop()
    
     # Go through each color and give it an attraction based on randomness
    def generate_attraction_matrix(self) -> list[list[int]]:
        matrix = [[] for i in range(self.number_of_colors)]

        for color in matrix:
            for i in range(self.number_of_colors):
                color.append(random.random())

        return matrix

    # Generate all particles in the scene
    def generate_particles(self) -> set[list[Particle], dict[int, list[int]]]:
        particles = []

        # Determine how many particles are allocated to each color
        particles_per_color = self.number_of_particles // self.number_of_colors

        # Generate the colors based on the number of colors and fill with random RGB value
        colors_index = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(self.number_of_colors)]

        # Generate all particles and assign color and random location
        for i in range(self.number_of_particles):
            color = colors_index[i // particles_per_color]
            x = random.random()
            y = random.random()

            particles.append(Particle(x, y, 0, 0, color))

        # turn the colors into a dictionary to index each color
        color_dictionary = {color : index for index, color in enumerate(colors_index)}
        return particles, color_dictionary
    
    # # Go through each particle, compare it against all other particles, update accordingly
    def update_particles(self) -> None:
        for particle_0 in self.particles:
            for particle in self.particles:
                if particle_0 is particle: continue

                # Calculate distance between the particle
                rx = (particle.x - particle_0.x)**2
                ry = (particle.y - particle_0.y)**2
                r = math.sqrt(rx + ry)
                if r < self.repulsion_distance: continue

                # Update accelerations of each particle
                attraction = self.attraction_matrix[self.color_dictionary[particle_0.color]]
                acceleration_X = (attraction * rx) / r**3
                acceleration_Y = (attraction * ry) / r**3

                # Update the velocities based on the accelerations of each particle
                particle_0.velocityX = particle_0.velocityX + acceleration_X * self.delta_time
                particle_0.velocityY = particle_0.velocityY + acceleration_Y * self.delta_time

            particle_0.x = particle_0.velocityX * self.delta_time
            particle_0.y = particle_0.velocityY * self.delta_time

    
    def mainloop(self) -> None:
        pygame.init()

        # Display the Window
        window = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        pygame.display.set_caption("Particle-Life")

        run = True
        FPS = 60
        clock = pygame.time.Clock()

        while run:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT: run = False

            # Reset display each update
            window.fill((0, 0, 0))

            for particle in self.particles:
                scaled_x = (particle.x * self.width) // 1
                scaled_y = (particle.y * self.height) // 1
                pygame.draw.circle(window, particle.color, (scaled_x, scaled_y), 5, 0)

            pygame.display.update()
            self.update_particles()
            

Simulation()