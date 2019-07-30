import bpy, math

# an idea I had... just in case
# from bpy.app.handlers import persistent


# @persistent
# def update_material(scene):
#    print("Material Updated")

# bpy.app.handlers.render_complete.append(update_material)

bl_info = {
    'name': 'PBR Baker',
    'description': '',
    'author': '',
    'version': (0, 0, 1),
    'blender': (2, 80, 0),
    'location': 'View3D > Properties  > PBR Baker',
    'warning': '',
    'wiki_url': '',
    'tracker_url': '',
    'category': '3D View'
}

bpy.types.Scene.PBR_Imagesize = bpy.props.IntProperty(
    name="resolution",
    description="Final Texture Resolution",
    min=256,
    max=10240,
    default=2048)


class PBR_PT_panel(bpy.types.Panel):
    bl_category = "PBR Baker"
    bl_label = "Magic Button Here"
    bl_idname = "PBR_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Texture Resolution:")
        row.prop(bpy.context.scene, "PBR_Imagesize", text="")
        row = layout.row()
        row.operator("pbr_baker.magicbutton", emboss=True, text="Magic Button")


class PBR_OT_magicbutton(bpy.types.Operator):
    '''CLick Magic Button'''
    bl_idname = "pbr_baker.magicbutton"
    bl_label = "Magic Button"

    @classmethod
    def poll(self, context):
        if context.mode != 'OBJECT':
            return False
        else:
            return getattr(context.active_object, 'type', False) == 'MESH'


    def execute(self, context):
        ac_ob = context.active_object
        arm = ac_ob.data

        imageResolution = bpy.context.scene.PBR_Imagesize

        bpy.context.scene.render.resolution_y = imageResolution
        bpy.context.scene.render.resolution_x = imageResolution

        size = len(bpy.data.materials)

        mat = bpy.data.materials

        squares = 0

        for i in range(math.ceil(math.sqrt(size))):
            for j in range(math.ceil(math.sqrt(size))):
                if(squares < size):
                    bpy.ops.mesh.primitive_plane_add(size=1, enter_editmode=False, location=(i, j, 0))
                    activeObject = bpy.context.active_object  # Set active object to variable
                    activeObject.data.materials.append(mat[squares])  # add the material to the object
                    #  bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
                squares += 1

        cameraScale = math.ceil(math.sqrt(size))
        cameraPos = cameraScale / 2 - 0.5
        bpy.ops.object.camera_add(enter_editmode=False, location=(cameraPos, cameraPos, 1), rotation=(0, -0, 0))
        bpy.context.object.data.type = 'ORTHO'
        bpy.context.object.data.ortho_scale = cameraScale
        activeObject = bpy.context.active_object
        bpy.context.scene.camera = activeObject

        bpy.ops.render.render(animation=False, write_still=True, use_viewport=False, layer="", scene="")

        return {'FINISHED'}

classes = (
    PBR_PT_panel,
    PBR_OT_magicbutton,

)

register, unregister = bpy.utils.register_classes_factory(classes)
