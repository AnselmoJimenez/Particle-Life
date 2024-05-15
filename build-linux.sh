#!/bin/bash

# Function to handle failures
failure() {
    echo "COMPILATION FAILED"
    exit 1
}

# Trap any error and call the failure function
trap failure ERR

# Exit immediately if a command exits with a non-zero status
set -e

# Create build directory if it does not exist
echo "Setting build directory..."
build_dir="build"
mkdir -p "$build_dir"

# Source files and object files
source_files="source/*.c"

# Compiler and compiler flags
cc="gcc"
cflags="-Wall -Wextra"
lflags="-lraylib -lGL -lm -lpthread -ldl -lrt -lX11"

echo "Compiling source files..."
object_files=""
for file in $source_files; do
    # Extract the base name without directory and suffix
    base_name=$(basename "$file" .c)
    # Logging
    echo "  $cc -c $file $cflags -o $build_dir/$base_name.o"
    $cc -c "$file" $cflags -o "$build_dir/$base_name.o"
    object_files="$object_files $build_dir/$base_name.o"
done
echo "Compilation Successful"

# Link all object files
echo "Linking object files..."
echo "  $cc $object_files $lflags -o particle-life"
$cc $object_files $lflags -o particle-life
echo "Linking successful"

echo "COMPILATION SUCCESSFUL"
