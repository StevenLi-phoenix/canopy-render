"""Run: blender --background Canopy.blend --python render_scene.py -- ./frames

Render the editable scene at its delivery settings. Encode the resulting PNGs:
ffmpeg -framerate 24 -start_number 1 -i frames/%04d.png -c:v libx264 -crf 14 -preset slow -pix_fmt yuv420p -movflags +faststart Canopy.mp4
"""
from pathlib import Path
import sys
import bpy

args = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else []
destination = Path(args[0] if args else './frames').resolve()
destination.mkdir(parents=True, exist_ok=True)
scene = bpy.context.scene
scene.render.resolution_x = 3840
scene.render.resolution_y = 1608
scene.render.resolution_percentage = 100
scene.render.fps = 24
scene.render.image_settings.file_format = 'PNG'
scene.render.image_settings.color_mode = 'RGB'
scene.render.image_settings.color_depth = '8'
for frame in range(1, 337):
    scene.frame_set(frame)
    scene.render.filepath = str(destination / f'{frame:04d}.png')
    bpy.ops.render.render(write_still=True)
