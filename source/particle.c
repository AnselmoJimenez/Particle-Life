#include "particle.h"

// print particles and their information
void print_particles(particle_t *particles, int num_particles) {
    for (int i = 0; i < num_particles; i++) {
        printf("Particle %d\t->\tlocation: (%f, %f); velocity: (%f, %f); hash: %d; color: {%d, %d, %d}\n", 
            i, 
            particles[i].x_coord, 
            particles[i].y_coord,
            particles[i].x_velocity,
            particles[i].y_velocity,
            particles[i].hash,
            particles[i].color.r, particles[i].color.g, particles[i].color.b
        );
    }
}

// Generates the attraction matrix by generating a random number between -1 and 1 in each slot
float **generate_attraction_matrix(int num_colors) {
    // Seeding the generator
    srand(time(NULL));
    
    float **attractions = malloc(num_colors * sizeof(float *));
    for (int i = 0; i < num_colors; i++) {
        attractions[i] = malloc(num_colors * sizeof(float));

        // Populate the matrix
        for (int j = 0; j < num_colors; j++) {
            int random_number = rand();      // Generate a random number between 0 and RAND_MAX
            double scaled = (double) random_number / RAND_MAX;  // Scale it to the range 0 to 1
            double shifted = scaled * 2.0 - 1.0;                // Shift it to the range -1 to 1

            attractions[i][j] = (float) shifted;
        }
    }

    return attractions;
}

// Generate the colors that will be used for the simulation
Color *generate_color_matrix(int num_colors) {
    srand(time(NULL));

    Color *colors = malloc(num_colors * sizeof(Color *));
    for (int i = 0; i < num_colors; i++) {
        colors[i] = (Color) {
            1 + rand() % 254,   // red
            1 + rand() % 254,   // green
            1 + rand() % 254,   // blue
            255                 // alpha
        };
    }
    return colors;
}

// create an array of all the particles and generate their values
void create_particles(particle_t *particles, int num_particles, int num_colors, int height, int width) {
    // Seeding the generator
    srand(time(NULL));

    Color *colors = generate_color_matrix(num_colors);
    for (int i = 0; i < num_particles; i++) {
        // initialize positions to a random location on screen
        particles[i].x_coord = (float) (rand() % width) / width;
        particles[i].y_coord = (float) (rand() % height) / height;
        
        // initialize velocity to 0
        particles[i].x_velocity = 0.0f;
        particles[i].y_velocity = 0.0f;

        // define their color
        particles[i].hash = i % num_colors;
        particles[i].color = colors[i % num_colors];
    }
}