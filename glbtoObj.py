import os
import sys
import trimesh

inputFolder = sys.argv[1] if len(sys.argv) > 1 else '3dObjects/newObjec'
outputFolder = sys.argv[2] if len(sys.argv) > 2 else inputFolder

os.makedirs(outputFolder, exist_ok=True)

for folder, subfolders, files in os.walk(inputFolder):  # goes through the folder and every folder inside it
    for file in sorted(files):
        if not file.lower().endswith('.glb'):
            continue
        glbPath = os.path.join(folder, file)
        name = os.path.splitext(file)[0]
        objPath = os.path.join(outputFolder, name + '.obj')

        # force='mesh' merges every part of the .glb scene into one mesh (with its transforms applied)
        mesh = trimesh.load(glbPath, force='mesh')

        # only the shape is needed for contours, so skip textures/materials
        mesh.export(objPath, file_type='obj', include_texture=False)
        print(f'{glbPath} -> {objPath}  ({len(mesh.vertices)} vertices, {len(mesh.faces)} faces)')

print('done')