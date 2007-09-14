/**
 * $Id$
 *
 * ***** BEGIN GPL/BL DUAL LICENSE BLOCK *****
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version. The Blender
 * Foundation also sells licenses for use in proprietary software under
 * the Blender License.  See http://www.blender.org/BL/ for information
 * about this.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software Foundation,
 * Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
 *
 * The Original Code is Copyright (C) 2001-2002 by NaN Holding BV.
 * All rights reserved.
 *
 * The Original Code is: all of this file.
 *
 * Contributor(s): none yet.
 *
 * ***** END GPL/BL DUAL LICENSE BLOCK *****
 */

struct Mesh;
struct EditMesh;
#define TF_PIN_MASK(id) (TF_PIN1 << id)
#define TF_SEL_MASK(id) (TF_SEL1 << id)

struct Object;

void object_uvs_changed(struct Object *ob);
void object_tface_flags_changed(struct Object *ob, int updateButtons);

int is_uv_tface_editing_allowed(void);
int is_uv_tface_editing_allowed_silent(void);

void get_connected_limit_tface_uv(float *limit);
int minmax_tface_uv(float *min, float *max);

void transform_width_height_tface_uv(int *width, int *height);
void transform_aspect_ratio_tface_uv(float *aspx, float *aspy);

void mouseco_to_cursor_sima(void);
void borderselect_sima(short whichuvs);
void mouseco_to_curtile(void);
void mouse_select_sima(void);
void select_invert_tface_uv(void);
void select_swap_tface_uv(void);
void mirrormenu_tface_uv(void);
void mirror_tface_uv(char mirroraxis);
void hide_tface_uv(int swap);
void reveal_tface_uv(void);
void stitch_uv_tface(int mode);
void unlink_selection(void);
void select_linked_tface_uv(int mode);
void toggle_uv_select(int mode);
void pin_tface_uv(int mode);
void weld_align_menu_tface_uv(void);
void weld_align_tface_uv(char tool);
void be_square_tface_uv(struct EditMesh *em);
void select_pinned_tface_uv(void);

void sima_sample_color(void);

#define UV_SELECT_ALL		1
#define UV_SELECT_PINNED	2

void new_image_sima(void);
void reload_image_sima(void);
void save_image_sima(void);
void save_as_image_sima(void);
void save_image_sequence_sima(void);
void replace_image_sima(short imageselect);
void open_image_sima(short imageselect);
void pack_image_sima(void);

/* checks images for forced updates on frame change */
void BIF_image_update_frame(void);
