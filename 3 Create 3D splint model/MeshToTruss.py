import bpy

# ------------ import external python functions 
import sys
import os
dir = os.path.dirname(bpy.data.filepath)
#print("The work direction is %s" % (dir))
os.chdir(dir) # Set the working directory for python code

if not dir in sys.path:
    sys.path.append(dir)
import imp


# draw cylinder from point x1 to x2
def cylinder_between(x1, x2, r):
    import bpy
    import math
    dx = x2[0] - x1[0]
    dy = x2[1] - x1[1]
    dz = x2[2] - x1[2]    
    dist = math.sqrt(dx**2 + dy**2 + dz**2)
    bpy.ops.mesh.primitive_cylinder_add(
        radius = r, 
        depth = dist,
        location = (dx/2 + x1[0], dy/2 + x1[1], dz/2 + x1[2])   
    )
    
    phi = math.atan2(dy, dx) 
    theta = math.acos(dz/dist) 
    bpy.context.object.rotation_euler[1] = theta 
    bpy.context.object.rotation_euler[2] = phi
    

def drawShpere(x1, r):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=r, enter_editmode=False, location=x1)

    
def boolean_operation (tool, op, apply=True):
    # (Enum): a Boolean operation: {'UNION', 'INTERSECT', 'DIFFERENCE'}
    obj = bpy.context.object
    bpy.ops.object.modifier_add(type='BOOLEAN')#adds new modifier to obj
    mod = obj.modifiers[-1]
    while obj.modifiers[0] != mod:
        bpy.ops.object.modifier_move_up(modifier=mod.name)
    mod.operation = op #set the operation
    mod.object = tool #activate the modifier
    if apply: #applies modifier results to the mesh of the active object (obj):
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier=mod.name)

def remove_duplicates(original):
    unique = []
    [unique.append(n) for n in original if n not in unique]
    return(unique)
# read file
from pathlib import Path
fileName = "TrussStructure.txt"
my_file = Path(fileName)
if my_file.is_file():
    #print("File exsits")    
    # clear the objects
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

    with open(fileName) as f:
        radiusInfo = f.readline()
        linksInfo = f.readlines()
        f.close()
    print(radiusInfo)    
    radiusSplit = radiusInfo.split()
    radius = float(radiusSplit[2])
    print(len(linksInfo))
    i = 0
    points = []
    for links in linksInfo:
        i = i+1
        print('Part 1/2: Draw Cylinder: '+str(i)+" of " +str(len(linksInfo)))
        linksplit = links.split()
        startPoint = [float(linksplit[0]),float(linksplit[1]),float(linksplit[2])]
        endPoint = [float(linksplit[3]),float(linksplit[4]),float(linksplit[5])]
        points.append(startPoint)
        points.append(endPoint)
        cylinder_between(startPoint,endPoint,radius)
        if i%200 == 0:
            bpy.ops.object.select_all(action='SELECT')
            bpy.ops.object.join()
    cylinderNumber = int(len(points)/2)
    points = remove_duplicates(points)    
    i = 0
    for point in points:
        i = i + 1
        print('Part 2/2: Draw Sphere: '+str(i)+" of " +str(len(points)))
        drawShpere(point,radius)
        if i%200 == 0:
            bpy.ops.object.select_all(action='SELECT')
            bpy.ops.object.join()
    
    print("Done!")
    
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.join()    
else:
    print("File does not exsit")





