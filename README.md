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