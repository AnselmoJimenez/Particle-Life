import pygame
import random

class Particle:
    def __init__(self, x: float, y: float, velocityX: float, velocityY: float, color: list[int]) -> None:
        self.x:float = x
        self.y:float = y
        self.velocityX:float = velocityX
        self.velocityY:float = velocityY
        self.color:list[int] = color

    def __str__(self) -> str:
        return f"Particle: {self.color} at Location {self.x, self.y}"


class Simulation:
    number_of_colors = 3
    number_of_particles = 30
    height = 1024
    width = 1024

    def __init__(self) -> None:
        self.particles = self.generate_particles()
        self.mainloop()
        
    def generate_particles(self) -> list[Particle]:
        particles = []

        # Determine how many particles are allocated to each color
        particles_per_color = self.number_of_particles // self.number_of_colors

        # Generate the colors based on the number of colors and fill with random RGB value
        colors_index = [[] for i in range(self.number_of_colors)]
        for color in colors_index:
            for i in range(3):
                color.append(random.randint(0, 255))

        # Generate all particles and assign color and random location
        for i in range(self.number_of_particles):
            color = colors_index[i // particles_per_color]
            x = random.random()
            y = random.random()

            particles.append(Particle(x, y, 0, 0, color))

        return particles
    
    def mainloop(self) -> None:
        # Display the Window
        window = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        pygame.display.set_caption("Particle-Life")

        run = True
        FPS = 60
        clock = pygame.time.Clock()

        while run:
            clock.tick(FPS)

            for particle in self.particles:
                scaled_x = (particle.x * 1024) // 1
                scaled_y = (particle.y * 1024) // 1
                pygame.draw.circle(window, particle.color, (scaled_x, scaled_y), 5, 0)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT: run = False
            

Simulation()