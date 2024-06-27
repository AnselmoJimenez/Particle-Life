#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define RAYGUI_IMPLEMENTATION
#include <raygui.h>
#include <raylib.h>
#undef RAYGUI_IMPLEMENTATION

#include "particle.h"
#include "simulation.h"


// create and update window
void mainloop(void) {
    // Initialization
    const int screen_width = 1280;
    const int screen_height = 720;
    bool button_clicked = false;
    InitWindow(screen_width, screen_height, "Particle-Life");
    SetTargetFPS(60);   // Set our game to run at 60 frames-per-second

    // Main game loop
    while (!WindowShouldClose()) {   // Detect window close button or ESC key
        // Update
        //----------------------------------------------------------------------------------
        
        //----------------------------------------------------------------------------------

        // Draw
        //----------------------------------------------------------------------------------
        BeginDrawing();
        ClearBackground(RAYWHITE);
        
        // Draw button using raygui
        if (GuiButton((Rectangle){ screen_width / 2 - 50, screen_height / 2 - 25, 100, 50 }, "Button")) {
            button_clicked = true;
        }

        // Display message if button is clicked
        if (button_clicked) {
            DrawText("Button clicked!", screen_width / 2 - 100, screen_height / 2 + 50, 20, RED);
        }
        
        EndDrawing();
        //----------------------------------------------------------------------------------
    }

    // De-Initialization
    //--------------------------------------------------------------------------------------
    CloseWindow();        // Close window and OpenGL context
    //--------------------------------------------------------------------------------------
}

int main(void) { 
    mainloop();

    return 0;
}