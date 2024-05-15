#include <stdio.h>
#include <stdlib.h>
#include <raylib.h>

#include "window.h"
#include "simulation.h"

// create and update window
void mainloop(void) {
    // Initialization
    InitWindow(WIDTH, HEIGHT, "Particle-Life");
    SetTargetFPS(60);   // Set our game to run at 60 frames-per-second
    // define attraction matrix
    // generate all particles and locations

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
        DrawCircle(100, 100, 5, BLUE);
        EndDrawing();
        //----------------------------------------------------------------------------------
    }

    // De-Initialization
    //--------------------------------------------------------------------------------------
    CloseWindow();        // Close window and OpenGL context
    //--------------------------------------------------------------------------------------

    return 0;
}

int main(void) {  }