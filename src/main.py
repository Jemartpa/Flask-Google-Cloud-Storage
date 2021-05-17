import bpy
import math 
from mathutils import Euler
import os
import subprocess

file_loc = './src/garment/0040401_FLORAL_PRINT_FLARED_SKIRT_Colorway_1.obj'


imported_object = bpy.ops.import_scene.obj(filepath=file_loc)
obj_object = bpy.context.selected_objects[0] ####<--Fix
obj_object.name = "garment"
print(obj_object.name)

obj = bpy.data.objects["garment"]

obj.rotation_mode = 'AXIS_ANGLE'
obj.rotation_axis_angle[0]  = math.pi
obj_loc = bpy.data.objects["garment"].location

obj_loc[0] = 7.85959 
obj_loc[1] = 6.1475
obj_loc[2] = -8.25092

cam = bpy.data.objects["Camera"]
cam.rotation_mode = 'AXIS_ANGLE'

cam.rotation_axis_angle[1]  = 1.0
cam.rotation_axis_angle[2]  = 0.0
cam.rotation_axis_angle[3]  = 0.0

obj_scale = bpy.data.objects["garment"].scale
obj_scale[0] = 0.118
obj_scale[1] = 0.118
obj_scale[2]= 0.118

scene = bpy.context.scene

scene.render.film_transparent=True


scene.cycles.device = 'GPU'

obj.rotation_mode = 'XYZ'

rotate_by = 90   #How many degrees to rotate the knob for every step
start_angle = 0     #What angle to start from



for x in range(0,4):
    angle = (start_angle * (math.pi/180)) + (x*-1) * (rotate_by * (math.pi/180))
    obj.rotation_euler = ( -math.pi, 0, angle )

    bpy.context.scene.render.filepath = "./src/output/Frame%d.png" % (x)
        
    bpy.ops.render.render(write_still=True)#, use_viewport=True)


from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'