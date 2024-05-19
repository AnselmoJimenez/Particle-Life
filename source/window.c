#include "window.h"

// create and update window
void mainloop(void) {
    // Initialization
    InitWindow(WIDTH, HEIGHT, "Particle-Life");
    SetTargetFPS(60);   // Set our game to run at 60 frames-per-second

    // generate all particles and their locations
    particle_t *particles = malloc(NUM_PARTICLES * sizeof(particle_t));
    create_particles(particles, NUM_PARTICLES, NUM_COLORS, HEIGHT, WIDTH);
    print_particles(particles, NUM_PARTICLES);
    
    // generate the attraction matrix to track how much each particle is attracted to each other
    float **attractions = generate_attraction_matrix(NUM_COLORS);

    // Main game loop
    while (!WindowShouldClose())    // Detect window close button or ESC key
    {
        // Update
        //----------------------------------------------------------------------------------
        
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