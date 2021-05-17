# Blender Rendering Module

Garment Rendering service for The Fitting Room using Blender

## Organization

[The Fitting Room](https://github.com/TheFittingRoom/)

## Author

[Jose Pereiro](https://github.com/josepereiroml)

## Overview

This module allows importing an .obj file into a .blend file, this file has some previous characteristics that have to be modified in order to be rendered by the camera. Also, the angle and size of the camera are adjusted to allow rendering.

## Changelog

Changelog for the module is maintained through [CHANGELOG.md](docs/CHANGELOG.md)

## Use Cases

- **Scenario 1** - You have a garment (.obj) and you want to produce four rendering images

## Program Flow

In **Scenario 1**, an empty blender scene called input.blend is started in this scene the script will import the .obj through the Blender functions. The file will be called garment in the code. This file is read in Blender and due to its large size and position the 'AXIS_ANGLE' rotation mode is used, in this case the position of the object is changed so that it is close to the camera and can be rendered. The camera must also be rotated. The object is very large compared to the camera and it is scaled (value < 1) so that it fits in the rendering scene. The value 0.118 is used in all coordinates so as not to affect the garment proportion. The scene is read, the device is chosen in this case 'GPU'.
The second part of the script is the one that allows to obtain the four rendered rotation images, these images are obtained by means of another rotation mode known as 'XYZ' in which the rotation angle is chosen (90º) and by means of a iteration produces the four rendered images that will be saved in the output folder.

## Usage

Go to Show Package Contents on Blender and it will show the MacOS folder having the Blender Console.
Copy that directory to the terminal and run ./blender --help to check the Blender console is working.

Copy the blender-docker folder into this folder and run the following command:

`zsh -c "cd /Applications/Blender.app/Contents/MacOS && ./script.sh"`

It will start running and the frames will be stored as PNG files in the output folder.

Copy files from docker container for debug using 
`docker cp 8849b90b89f8:/app/src/output/Frame0.png .`
