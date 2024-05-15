#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "particle.h"

// Generates the attraction matrix by generating a random number between -1 and 1 in each slot
void define_attraction_matrix(float **matrix, int num_particles) {
    // Seeding the generator
    srand(time(NULL));
    
    // Populating the matrix
    for (int i = 0; i < num_particles; i++) {
        for (int j = 0; j < num_particles; j++) {
            int random_number = rand();      // Generate a random number between 0 and RAND_MAX
            double scaled = (double) random_number / RAND_MAX;  // Scale it to the range 0 to 1
            double shifted = scaled * 2.0 - 1.0;                // Shift it to the range -1 to 1

            matrix[i][j] = (float) shifted;
        }
    }
}

// create an array of all the particles and generate their values
void create_particles(particle_t *particles, int num_particles, int resolution[2], int num_colors) {
    // Seeding the generator
    srand(time(NULL));

    for (int i = 0; i < num_particles; i++) {
        // initialize positions to a random location on screen
        particles[i].x_coord = rand() % resolution[1];
        particles[i].y_coord = rand() % resolution[0];
        
        // initialize velocity to 0
        particles[i].x_velocity = 0.0f;
        particles[i].y_velocity = 0.0f;

        // define their color
        
    }
}