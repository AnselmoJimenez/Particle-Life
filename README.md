# Particle-Life
> An Interactive Particle-Life Simulation using raylib

Particle life is a computational simulation that models the behavior of particles interacting according to specific rules. This concept is often used in the context of artificial life or digital organisms, where particles can represent simple agents or entities that follow predefined interaction rules to exhibit complex, emergent behavior. The concept is built upon ideas from cellular automata, physics, and biology.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)

## Installation

### Linux

> This installation process follows along with raylib's wiki [Working-on-GNU-Linux](https://github.com/raysan5/raylib/wiki/Working-on-GNU-Linux) but is tailored for this specific project.

#### Building Library

To build this simulator in Linux the raylib repository is necessary.

##### Install Required Tools

You need a gcc (or alternative C99 compiler), **make** and **git** (to download raylib repo).

```bash
sudo apt install build-essential git
```

##### Install Required Libraries

You need to install some required libraries; **ALSA** for audio, **Mesa** for OpenGL accelerated graphics and **X11** for windowing system.

###### Ubuntu

```bash
sudo apt install libasound2-dev libx11-dev libxrandr-dev libxi-dev libgl1-mesa-dev libglu1-mesa-dev libxcursor-dev libxinerama-dev libwayland-dev libxkbcommon-dev
```

###### Fedora

```bash
sudo dnf install alsa-lib-devel mesa-libGL-devel libX11-devel libXrandr-devel libXi-devel libXcursor-devel libXinerama-devel libatomic
```

###### Arch Linux

```bash
sudo pacman -S alsa-lib mesa libx11 libxrandr libxi libxcursor libxinerama
```

#### Build raylib using make

Compile the raylib static library.
Download the raylib repository from [Github](https://github.com/raysan5/raylib) on browser or clone it, then compile it with:

```bash
git clone https://github.com/raysan5/raylib.git raylib
cd raylib/src/
make PLATFORM=PLATFORM_DESKTOP
```

Install the library to the standard directories, ```usr/local/lib``` and ```/usr/local/include```:

```bash
sudo make install
sudo make install RAYLIB_LIBTYPE=SHARED
```

### Windows

> This installation process follows along with raylib's wiki [Working-on-Windows](https://github.com/raysan5/raylib/wiki/Working-on-Windows) but is tailored for this specific project.

#### Compiler

##### MinGW-W64/GCC

An open source C/C++ toolchain that is very lightweight. The best way to get MinGW-W64 and GCC is via the [W64Devkit](https://github.com/skeeto/w64devkit/). Download the w64devkit zip file, unzip it and run W64Devkit.exe. That will give you a terminal that is ready to go.

MinGW-W64 is **required**

#### Manual Setup with W64Devkit

1. Download ```w64devkit-x.xx.x.zip```

> Unzip to c:\w64devkit

2. Download ```raylib-5.0_win64_mingw-w64.zip``` from [Github](https://github.com/raysan5/raylib/releases)

> Unzip `include` and `lib` to `c:\w64devkit\x86_64-w64-mingw32` or your other MinGW-W64 installation (for example in my case, I use msys)

> https://github.com/skeeto/w64devkit?tab=readme-ov-file#library-installation

***This step does not apply to other MinGW-W64 installation***

3. Goto `c:\w64devkit` and run `w64devkit.exe`, which will launch a console

4. Create `raylibhelloworld.c` for testing

```C
#include "raylib.h"

int main() {
  const int screenWidth = 800;
  const int screenHeight = 600;
  InitWindow(screenWidth, screenHeight, "Raylib basic window");
  SetTargetFPS(60);
  while (!WindowShouldClose()) {
    BeginDrawing();
    ClearBackground(RAYWHITE);
    DrawText("It works!", 20, 20, 20, BLACK);
    EndDrawing();
  }
  CloseWindow();
  return 0;
}
```

5. Compile in `w64devkit.exe` console or other terminal for testing:

> gcc -o raylibhelloworld.exe raylibhelloworld.c -lraylib -lgdi32 -lwinmm

6. Run:

> ./raylibhelloworld.exe

### Build Particle-Life

After downloading necessary libraries and building raylib, build and run this project using:

#### Windows

```powershell
.\build-windows.bat
.\particle-life.exe
```

#### Linux

```bash
./build-linux.sh
./particle-life
```

