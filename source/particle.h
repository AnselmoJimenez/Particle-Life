#ifndef PARTICLE_H
#define PARTICLE_H

typedef struct particle {
    float x_coord;
    float y_coord;
    float x_velocity;
    float y_velocity;
    int color[3];
} particle_t;

// Generates the attraction matrix by generating a random number between -1 and 1 in each slot
void define_attraction_matrix(float **matrix, int num_particles);

// create an array of all the particles and generate their values
void create_particles();

#endif