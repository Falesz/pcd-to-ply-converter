# PCD to PLY converter

A lightweight Python script to grab `xyz` data points from `pcd` files and create matching `ply` files with them. The goal is to make an existing pcd dataset available for importing in MeshLab. This is part of my work in my Autonomous Systems Computer Science Masters programme research.

## Motivation

For my research projects I am using MeshLab v2025.07 as a tool for inspecting 3D data clouds. This version of MeshLab doesn't support importing `pcd` files, however for my tasks an `xyz` feature set should be sufficient, making a simple `ply` format a viable replacement.

## How to use

The program creates a dedicated `inputs` and `outputs` upon first execution. The user must manually populate the `inputs` folder with `pcd` files they wish to convert into `ply` format. Executing the script will convert all `pcd` files in the `inputs` folder.  
After navigating to the location of the script in the commandline the user may execute the script with the command:  
`py pcd_to_ply_converter.py`  
or by double-clicking the script file.

No exception or error handling or input validation is implemented at this time. It is mostly the user's responsibility to use the program correctly and use valid input data.

## Valid PCD file format
A valid `pcd` input format's header looks like the following example:
```
VERSION .7
FIELDS x y z intensity ring time
SIZE 4 4 4 4 2 4
TYPE f f f f u f
COUNT 1 1 1 1 1 1
WIDTH 16
HEIGHT 912
VIEWPOINT 0 0 0 1 0 0 0
POINTS 14592
DATA ascii
```
This must immediately be followed by the data points themselves, looking like the following example:
```
-0.9806066155433655 -14.347158432006836 -1.7605812549591064 24.0 4 -0.049033213406801224 
nan nan nan nan 5 -0.049028605222702026 
-1.082955002784729 -15.565074920654297 -0.8155000805854797 6.0 6 -0.04902399703860283 
-1.5515213012695312 -22.13231658935547 -0.38656899333000183 3.0 7 -0.04901938885450363 
-1.4729121923446655 -22.175765991210938 0.3872321844100952 16.0 8 -0.049049343913793564 
```
The data file may NOT contain any empty lines, including at the very end!