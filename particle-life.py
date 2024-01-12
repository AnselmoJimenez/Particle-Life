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
        self.width = 1500
        self.height = 1500
        self.number_of_colors = 3
        self.number_of_particles = 100

        self.delta_time = 0.02
        self.friction_force = 0.2

        self.attraction_matrix = self.generate_attraction_matrix()
        self.particles, self.color_dictionary = self.generate_particles()

        self.mainloop()
    
     # Go through each color and give it an attraction based on randomness
    def generate_attraction_matrix(self) -> list[list[int]]:
        matrix = [[] for _ in range(self.number_of_colors)]

        for color in matrix:
            for _ in range(self.number_of_colors):
                color.append(random.uniform(-1, 1))

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
            # may get an index error on the last particle
            try:
                color = colors_index[i // particles_per_color]
            except IndexError as e:
                color = colors_index[i // particles_per_color - 1]

            x = random.random()
            y = random.random()

            particles.append(Particle(x, y, 0, 0, color))

        # turn the colors into a dictionary to index each color
        color_dictionary = {color : index for index, color in enumerate(colors_index)}
        return particles, color_dictionary
    
    # # Go through each particle, compare it against all other particles, update accordingly
    def update_particles(self) -> None:
        # Update accelerations and velocities
        for particle1 in self.particles:
            acceleration_X = 0
            acceleration_Y = 0

            for particle2 in self.particles:
                if particle1 is particle2: continue

                # Calculate distance between the particle
                rx = particle2.x - particle1.x
                ry = particle2.y - particle1.y
                r = math.hypot(rx, ry)

                # Calculate the accelerations of each particle based on the distance to other particles and the attraction matrix
                repulsion_distance = 0.2
                attraction = self.attraction_matrix[self.color_dictionary[particle1.color]][self.color_dictionary[particle2.color]]
                if r < repulsion_distance: 
                    attraction_force = (r / repulsion_distance) - 1
                elif repulsion_distance < r and r < 1: 
                    attraction_force = attraction * (1 - abs(2 * r - 1 - repulsion_distance) / (1 - repulsion_distance))
                else:
                    attraction_force = 0

                # Update accelerations of each particle
                acceleration_X += attraction_force * rx / r
                acceleration_Y += attraction_force * ry / r

            # Update the velocities based on the accelerations of each particle
            particle1.velocityX *= self.friction_force
            particle1.velocityY *= self.friction_force    

            particle1.velocityX += particle1.velocityX + acceleration_X * self.delta_time
            particle1.velocityY += particle1.velocityY + acceleration_Y * self.delta_time

        # Update positions based on velocities
        for particle in self.particles:
            particle.x = (particle.x + particle.velocityX * self.delta_time) % self.width
            particle.y = (particle.y + particle.velocityY * self.delta_time) % self.height

    
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

            # Reset display each update and update the particles
            window.fill((0, 0, 0))

            for particle in self.particles:
                scaled_x = (particle.x * self.width) // 1
                scaled_y = (particle.y * self.height) // 1
                pygame.draw.circle(window, particle.color, (scaled_x, scaled_y), 3, 0)

            self.update_particles()
            pygame.display.update()
            

Simulation()