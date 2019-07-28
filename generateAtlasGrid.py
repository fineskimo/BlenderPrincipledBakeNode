import bpy, math

imageResolution  = 2048

bpy.context.scene.render.resolution_y = imageResolution
bpy.context.scene.render.resolution_x = imageResolution

size = len(bpy.data.materials)

mat = bpy.data.materials

squares = 0
for i in range(math.ceil(math.sqrt(size))):
    for j in range(math.ceil(math.sqrt(size))):
        if(squares < size):
            bpy.ops.mesh.primitive_plane_add(size=1, enter_editmode=False, location=(i, j, 0))
            activeObject = bpy.context.active_object #Set active object to variable
            activeObject.data.materials.append(mat[squares]) #add the material to the object
            #bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
        squares += 1;

cameraScale = math.ceil(math.sqrt(size))
cameraPos = cameraScale/2-0.5
bpy.ops.object.camera_add(enter_editmode=False, location=(cameraPos, cameraPos, 1), rotation=(0, -0, 0))
bpy.context.object.data.type = 'ORTHO'
bpy.context.object.data.ortho_scale = cameraScale
activeObject = bpy.context.active_object
bpy.context.scene.camera = activeObject

bpy.ops.render.render(animation=False, write_still=True, use_viewport=False, layer="", scene="")
