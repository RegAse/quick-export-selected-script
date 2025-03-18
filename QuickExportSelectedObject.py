bl_info = {
    "name": "Export Selected objects as FBX",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy
import os

class QuickExport(bpy.types.Operator):
    """Export Selected objects as FBX"""
    bl_idname = "object.export_fbx"
    bl_label = "Export Selected objects as FBX"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        name_of_first_object = bpy.context.selected_objects[0]
        
        file_path = bpy.data.filepath
        directory_path = os.path.dirname(file_path)
        
        # Export locations
        export_directory = os.path.join(directory_path, "Exports" + os.path.sep)
        export_file_path = os.path.join(directory_path, "Exports" + os.path.sep + name_of_first_object.name + ".fbx")
        
        if not os.path.exists(export_directory):
            os.mkdir(export_directory)
        
        bpy.ops.export_scene.fbx(filepath=export_file_path, use_selection=True)
        
        print("Successfully exported to: " + export_file_path)

        return {'FINISHED'} # Operation was a success!

def menu_func(self, context):
    self.layout.operator(QuickExport.bl_idname)

def register():
    bpy.utils.register_class(QuickExport)
    bpy.types.VIEW3D_MT_object.append(menu_func)  # Adds the new operator to an existing menu.

def unregister():
    bpy.utils.unregister_class(QuickExport)


# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()