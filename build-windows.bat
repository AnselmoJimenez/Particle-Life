@echo off
setlocal enabledelayedexpansion

rem Create build directory if it does not exist
echo Setting build directory...
set build_dir=build
if not exist "%build_dir%" mkdir "%build_dir%"

rem Source files and object files
set source_files=source\*.c

rem Compiler and compiler flags
set cc=gcc
set cflags=-Wall -Wextra
set lflags=-lraylib -lgdi32 -lwinmm

echo Compiling source files...
set object_files=
for %%f in (%source_files%) do (
    rem Extract the base name without directory and suffix
    set base_name=%%~nf
    rem Logging
    echo %cc% -c %%f %cflags% -o %build_dir%\!base_name!.o
    %cc% -c %%f %cflags% -o %build_dir%\!base_name!.o
    if errorlevel 1 (
        echo Compilation failed for %%f
        echo COMPILATION FAILED
        exit /b 1
    )
    set object_files=!object_files! %build_dir%\!base_name!.o
)
echo Compilation Successful

rem Link all object files
echo Linking object files...
set link_command=%cc% %object_files% %lflags% -o particle-life
echo %link_command%
%link_command%
if errorlevel 1 (
    echo Linking failed
    echo COMPILATION FAILED
    exit /b 1
)
echo Linking successful

echo COMPILATION SUCCESSFUL
exit /b 0