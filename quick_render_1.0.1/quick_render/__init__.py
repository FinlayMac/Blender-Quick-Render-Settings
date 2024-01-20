# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Quick Render",
    "author" : "Finlay", 
    "description" : "Displays the most common render settings and a big button to press",
    "blender" : (3, 0, 0),
    "version" : (1, 0, 1),
    "location" : "",
    "warning" : "",
    "doc_url": "", 
    "tracker_url": "", 
    "category" : "3D View" 
}


import bpy
import bpy.utils.previews


addon_keymaps = {}
_icons = None
class SNA_PT_QUICK_RENDER_89E27(bpy.types.Panel):
    bl_label = 'Quick Render'
    bl_idname = 'SNA_PT_QUICK_RENDER_89E27'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'Quick Render'
    bl_order = 0
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        row_4BDCA = layout.row(heading='Resolution', align=True)
        row_4BDCA.alert = False
        row_4BDCA.enabled = True
        row_4BDCA.active = True
        row_4BDCA.use_property_split = False
        row_4BDCA.use_property_decorate = False
        row_4BDCA.scale_x = 1.0
        row_4BDCA.scale_y = 1.0
        row_4BDCA.alignment = 'Expand'.upper()
        row_4BDCA.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_4BDCA.prop(bpy.data.scenes['Scene'].render, 'resolution_x', text='', icon_value=0, emboss=True)
        row_4BDCA.prop(bpy.data.scenes['Scene'].render, 'resolution_y', text='', icon_value=0, emboss=True)
        row_F4569 = layout.row(heading='Frame Range', align=False)
        row_F4569.alert = False
        row_F4569.enabled = True
        row_F4569.active = True
        row_F4569.use_property_split = False
        row_F4569.use_property_decorate = False
        row_F4569.scale_x = 1.0
        row_F4569.scale_y = 1.0
        row_F4569.alignment = 'Expand'.upper()
        row_F4569.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_F4569.prop(bpy.data.scenes['Scene'], 'frame_start', text='', icon_value=0, emboss=True)
        row_F4569.prop(bpy.data.scenes['Scene'], 'frame_end', text='', icon_value=0, emboss=True)
        row_5F5BF = layout.row(heading='Location', align=False)
        row_5F5BF.alert = False
        row_5F5BF.enabled = True
        row_5F5BF.active = True
        row_5F5BF.use_property_split = False
        row_5F5BF.use_property_decorate = False
        row_5F5BF.scale_x = 1.0
        row_5F5BF.scale_y = 1.0
        row_5F5BF.alignment = 'Expand'.upper()
        row_5F5BF.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_5F5BF.prop(bpy.data.scenes['Scene'].render, 'filepath', text='', icon_value=0, emboss=True)
        row_89FD8 = layout.row(heading='Format', align=False)
        row_89FD8.alert = False
        row_89FD8.enabled = True
        row_89FD8.active = True
        row_89FD8.use_property_split = False
        row_89FD8.use_property_decorate = False
        row_89FD8.scale_x = 1.0
        row_89FD8.scale_y = 1.0
        row_89FD8.alignment = 'Expand'.upper()
        row_89FD8.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_89FD8.prop(bpy.data.scenes['Scene'].render.image_settings, 'file_format', text='', icon_value=0, emboss=True)
        row_29AE6 = layout.row(heading='Render Camera', align=False)
        row_29AE6.alert = False
        row_29AE6.enabled = True
        row_29AE6.active = True
        row_29AE6.use_property_split = False
        row_29AE6.use_property_decorate = False
        row_29AE6.scale_x = 1.0
        row_29AE6.scale_y = 1.0
        row_29AE6.alignment = 'Expand'.upper()
        row_29AE6.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_29AE6.prop(bpy.context.view_layer.objects, 'active', text='', icon_value=0, emboss=True)
        op = row_29AE6.operator('view3d.object_as_camera', text='Set', icon_value=0, emboss=True, depress=False)
        row_B0C93 = layout.row(heading='Render', align=False)
        row_B0C93.alert = False
        row_B0C93.enabled = True
        row_B0C93.active = True
        row_B0C93.use_property_split = False
        row_B0C93.use_property_decorate = False
        row_B0C93.scale_x = 1.0
        row_B0C93.scale_y = 2.0
        row_B0C93.alignment = 'Expand'.upper()
        row_B0C93.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_B0C93.operator('render.render', text='Render', icon_value=240, emboss=True, depress=False)
        op.animation = True
        op.write_still = True


def register():
    global _icons
    _icons = bpy.utils.previews.new()
    bpy.utils.register_class(SNA_PT_QUICK_RENDER_89E27)


def unregister():
    global _icons
    bpy.utils.previews.remove(_icons)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    for km, kmi in addon_keymaps.values():
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    bpy.utils.unregister_class(SNA_PT_QUICK_RENDER_89E27)
