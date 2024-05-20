#include "window.h"

// create and update window
void mainloop(void) {
    // Initialization
    InitWindow(WIDTH, HEIGHT, "Particle-Life");
    SetTargetFPS(60);   // Set our game to run at 60 frames-per-second

    // generate all particles and their locations
    particle_t *particles = malloc(NUM_PARTICLES * sizeof(particle_t));
    create_particles(particles, NUM_PARTICLES, NUM_COLORS, HEIGHT, WIDTH);
    
    // generate the attraction matrix to track how much each particle is attracted to each other
    float **attractions = generate_attraction_matrix(NUM_COLORS);

    // Main game loop
    while (!WindowShouldClose()) {   // Detect window close button or ESC key
        // Update
        //----------------------------------------------------------------------------------
        for (int i = 0; i < NUM_PARTICLES; i++) {
            float acceleration_x = 0.0f;
            float acceleration_y = 0.0f;

            for (int j = 0; j < NUM_PARTICLES; j++) {
                if (i == j) continue;

                // Calculating the distance between particles
                float rx = particles[j].x_coord - particles[i].x_coord;
                float ry = particles[j].y_coord - particles[i].y_coord;
                float r = hypotf(rx, ry);
                if (r == 0.0f) continue;

                // Calculate the accelerations of each particle based on the distance to other particles and the attraction matrix
                float repulsion_distance = 0.1f;
                float pull = attractions[particles[i].hash][particles[j].hash];

                float pull_force = 0.0f;
                if (r < repulsion_distance) {
                    pull_force = (r / repulsion_distance) - 1.0f;
                } else if (repulsion_distance < r && r < 1) {
                    pull_force = (pull / MAX_PULL_RADIUS) * (1 - abs(2 * r - 1 - repulsion_distance) / (1 - repulsion_distance));
                } else {
                    pull_force = 0.0f;
                }

                acceleration_x += pull_force * rx / r;
                acceleration_y += pull_force * ry / r;
            }

            // Update velocities based on accelerations
            particles[i].x_velocity += acceleration_x * DELTA_TIME;
            particles[i].y_velocity += acceleration_y * DELTA_TIME;

            // Apply friction to the velocity
            particles[i].x_velocity *= FRICTION;
            particles[i].y_velocity *= FRICTION;
        }

        // Update positions based on velocities
        for (int i = 0; i < NUM_PARTICLES; i++) {
            particles[i].x_coord += particles[i].x_velocity * DELTA_TIME;
            particles[i].y_coord += particles[i].y_velocity * DELTA_TIME;
        }
        //----------------------------------------------------------------------------------

        // Draw
        //----------------------------------------------------------------------------------
        BeginDrawing();
        ClearBackground(RAYWHITE);
        for (int i = 0; i < NUM_PARTICLES; i++) {
            DrawCircle(particles[i].x_coord * WIDTH, particles[i].y_coord * HEIGHT, 5, particles[i].color);
        }
        
        EndDrawing();
        //----------------------------------------------------------------------------------
    }

    // De-Initialization
    //--------------------------------------------------------------------------------------
    CloseWindow();        // Close window and OpenGL context
    //--------------------------------------------------------------------------------------

    free(particles);
    free(attractions);

}

int main(void) { 
    mainloop();

    return 0;
}