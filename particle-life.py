import pygame
import tkinter
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


class Simulation (tkinter.Canvas):
    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, **kwargs)

        self.width = 1500
        self.height = 1500
        self.number_of_colors = 3
        self.number_of_particles = 150

        self.delta_time = 0.005
        self.friction_force = 0.2
        self.maximum_radius = 0.1

        self.attraction_matrix = self.generate_attraction_matrix()
        self.particles, self.color_dictionary = self.generate_particles()

        self.draw_particles()
    
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
    
    # # Go through each particle, compare it against all other particles, update positions and velocities accordingly
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
                if r == 0: continue

                # Calculate the accelerations of each particle based on the distance to other particles and the attraction matrix
                repulsion_distance = 0.1
                attraction = self.attraction_matrix[self.color_dictionary[particle1.color]][self.color_dictionary[particle2.color]]
                if r < repulsion_distance: 
                    attraction_force = (r / repulsion_distance) - 1
                elif repulsion_distance < r and r < 1: 
                    attraction_force = (attraction / self.maximum_radius) * (1 - abs(2 * r - 1 - repulsion_distance) / (1 - repulsion_distance))
                else:
                    attraction_force = 0

                # Update accelerations of each particle
                acceleration_X += attraction_force * rx / r
                acceleration_Y += attraction_force * ry / r

            # Update the velocities based on the accelerations of each particle
            particle1.velocityX *= self.maximum_radius
            particle1.velocityY *= self.maximum_radius

            particle1.velocityX *= self.friction_force
            particle1.velocityY *= self.friction_force    

            particle1.velocityX += acceleration_X * self.delta_time
            particle1.velocityY += acceleration_Y * self.delta_time

        # Update positions based on velocities
        for particle in self.particles:
            particle.x += particle.velocityX * self.delta_time
            particle.y += particle.velocityY * self.delta_time
    
    def draw_particles(self) -> None:
        self.update_particles()

        self.delete("all") # Clear the screen
        self.create_rectangle(0, 0, self.winfo_reqwidth(), self.winfo_reqheight(), fill="black", outline="black")

        # Redraw all particles
        for particle in self.particles:
            radius = 5
            scaled_x = particle.x * self.width
            scaled_y = particle.y * self.height
            rgb_color = "#{:02x}{:02x}{:02x}".format(particle.color[0], particle.color[1], particle.color[2])

            self.create_oval(scaled_x - radius, scaled_y - radius, scaled_x + radius, scaled_y + radius, fill=rgb_color)
        
        self.after(1, self.draw_particles)


def main():
    root = tkinter.Tk()
    root.title("Particle Life")
    root.geometry(f"1500x1500")
    root.resizable(True, True)

    # Editing Frame 
    editing_frame = tkinter.Frame(root, width=100, bg="gray")
    editing_frame.pack_propagate(False)
    editing_frame.pack(side="left", fill="y", expand=False, anchor="w")

    # Configuring the frame
    label = tkinter.Label(editing_frame, text="Particle Life Simulation")
    label.grid(row=0, column=0, pady=3)

    # Configuring the Canvas
    canvas = Simulation(root, bg="black")
    canvas.pack(side="right", fill="both", expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()