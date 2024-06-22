import trimesh
import sys
import os

def convert_step_to_stl(input_file, output_file):
    # Rename .stp to .step if necessary
    if input_file.endswith('.stp'):
        renamed_file = input_file.replace('.stp', '.step')
        os.rename(input_file, renamed_file)
        input_file = renamed_file
    # Load the STEP file and generate a mesh using GMSH
    mesh = trimesh.Trimesh(**trimesh.interfaces.gmsh.load_gmsh(file_name=input_file, gmsh_args=[
        ("Mesh.Algorithm", 1),
        ("Mesh.CharacteristicLengthFromCurvature", 50),
        ("General.NumThreads", 10),
        ("Mesh.MinimumCirclePoints", 32)
    ]))
    
    # Export the mesh to STL format in ASCII mode
    mesh.export(output_file, file_type='stl_ascii')

convert_step_to_stl("Tiger.step", "output.stl")

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    convert_step_to_stl(input_file, output_file)
