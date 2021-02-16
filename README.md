# 3D-printed-splints-demo-tutorial

2021-3D-Printed-Splints
V 0.0.1-alpha

Create 3D printable splint models using free and open-source software, including Meshmixer 3.5, Python 3.7, and Blender 2.8. The video demo to create a 3D printable wrist model is published on YouTube (https://www.youtube.com/playlist?list=PLaEzUCLiIDZa7U0yNojkRk8dKdgbiMrrL).

The link to Meshmixer 3.5: http://www.meshmixer.com/download.html

The link to Blender 2.8: https://www.blender.org/download/releases/2-80/

The link to Python 3.7: https://www.python.org/downloads/release/python-370/

There are total five steps to create a 3D printable splint:

Create Draft splint strcture using Meshmixer 3.5.
Optimize the structure of the splint. The optimization code has been packed into a software: TrussStructureOptimization.exe in the folder of "2 3D printed splints optimization". The structure file must be an OBJ file and the name must be "input.obj". Put the "input.obj" file and the software inside a folder and run the software. You will get the optimized structure as "TrussStructure.txt". The raduis of the 3D splint model can be edited in the first line of the "TrussStructure.txt". The unit of a splint model should be determined by users.
Create a 3D splint model using Blender and Python API. A blender project is included in side the folder "3 Create 3D splint model". The 3D splint model will be created based on the structure information in the file "TrussStructure.txt".
Attach blocks to the 3D splint model created in the previously step.
Seperate the splint model with blocks into two pieces.
Note: the process can be used for creating other splint models. The software is free for non-commercial purpose.

© 2021 maxSIMhealth. All rights reserved.
