#ifndef PARTICLE_H
#define PARTICLE_H

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <raylib.h>

typedef struct particle {
    float x_coord;
    float y_coord;
    float x_velocity;
    float y_velocity;
    int hash;
    Color color;
} particle_t;

// print particles and their information
void print_particles(particle_t *particles, int num_particles);

// Generates the attraction matrix by generating a random number between -1 and 1 in each slot
float **generate_attraction_matrix(int num_colors);

// Generate the colors that will be used for the simulation
Color *generate_color_matrix(int num_colors);

// create an array of all the particles and generate their values
void create_particles(particle_t *particles, int num_particles, int num_colors, int height, int width);

#endif