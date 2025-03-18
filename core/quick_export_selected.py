import bpy
from mathutils import *
import os

D = bpy.data
C = bpy.context


class QuickExport(bpy.types.Operator):
    """Export Selected objects as FBX"""
    bl_idname = "object.export_fbx"
    bl_label = "Export Selected objects as FBX"
    bl_options = {'REGISTER', 'UNDO'}
    
    #@persistent
    def execute(self, context):
        
        if len(bpy.context.selected_objects) < 1:
            return {'Finished'}
        
        name_of_first_object = bpy.context.selected_objects[0]
        
        file_path = bpy.data.filepath
        directory_path = os.path.dirname(file_path)
        
        # Export locations
        export_directory = os.path.join(directory_path, "Exports" + os.path.sep)
        export_file_path = os.path.join(directory_path, "Exports" + os.path.sep + name_of_first_object.name + ".fbx")
        
        if not os.path.exists(export_directory):
            os.mkdir(export_directory)
        
        bpy.ops.export_scene.fbx(filepath=export_file_path, use_selection=True)
        
        print("Successfully exported: " + export_file_path)

        return {'FINISHED'} # Operation was a success!

def menu_func(self, context):
    self.layout.operator(QuickExport.bl_idname)
    
def register():
    print("Register handlers")
    bpy.utils.register_class(QuickExport)
    bpy.types.VIEW3D_MT_object.append(menu_func)  # Adds the new operator to an existing menu.
    
    # Register so that code executes on save
    if not QuickExport.execute in bpy.app.handlers.save_post:
        bpy.app.handlers.save_post.append(QuickExport.execute)

def unregister():
    print("Unregister handlers: ")
    if QuickExport.execute in bpy.app.handlers.save_post:
       bpy.app.handlers.save_post.remove(QuickExport.execute) 
    bpy.utils.unregister_class(QuickExport)
    bpy.types.VIEW3D_MT_object.remove(menu_func)