import bpy

from .export import ExportSonicPath

bl_info = {
    "name": "SonicPath",
    "description": "Export Path Data",
    "author": "Hedgeturd",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "location": "File > Export",
    "warning": "",
    "wiki_url": "",
    "category": "Export"
}

# Register addon classes
def menu_func_export(self, context):
    self.layout.operator(ExportSonicPath.bl_idname, text="Sonic Path (.path.xml)")

def register():
    bpy.utils.register_class(ExportSonicPath)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)

def unregister():
    bpy.utils.unregister_class(ExportSonicPath)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)

if __name__ == "__main__":
    register()