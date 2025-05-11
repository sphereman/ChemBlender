# Copyright (C) 2023 Blender Foundation. <https://blender.org>

# ------------------------------- ChemBlender -------------------------------- #
# ------------------------------ version alpha ------------------------------- #
#                                                                              #
#     Professional Visualization of Molecules for Scientists and Artists.      #
#                                                                              #
#                              Author: Li Haodong                              #
#                University of Science and Technology of China                 #
#                                 (2024-2025)                                  #
#                           http://asrc.ustc.edu.cn/                           #
#                                                                              #
# ############################################################################ #


bl_info = {
    "name": "ChemBlender",
    "author": "Li Haodong - USTC",
    "version": ("α", 0, 0),
    "blender": (4, 0, 1),
    "location": "View_3D -> UI",
    "description": "Professional Visualization of Molecules for Scientists and Artiests.",
    "warning": "",
    "doc_url": "http://asrc.ustc.edu.cn/",
    "category": "Add Mesh",
}

import bpy
from . import auto_Load
from .Panel import Mol3DSettings, MOL3D_PT_Build, MOL3D_PT_TOOLS, CRYSTAL_PT_TOOLS
from .node_assets import Mol3D_node_menu


classes = auto_Load.init()
panel_cls = [MOL3D_PT_Build,
             MOL3D_PT_TOOLS,
             CRYSTAL_PT_TOOLS,
             ]
for cls in panel_cls:
    classes.remove(cls)


def register():
    for cls in panel_cls:
        bpy.utils.register_class(cls)
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.NODE_MT_geometry_node_add_all.append(Mol3D_node_menu)
    bpy.types.Scene.sel_order = bpy.props.StringProperty()
    bpy.types.Scene.my_tool = bpy.props.PointerProperty(type=Mol3DSettings)
    

def unregister():
    bpy.types.NODE_MT_geometry_node_add_all.remove(Mol3D_node_menu)
    for cls in panel_cls:
        bpy.utils.unregister_class(cls)
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.my_tool
    del bpy.types.Scene.sel_order
