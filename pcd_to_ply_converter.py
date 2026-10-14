from pathlib import Path

# --------------------------------------------------------------------------------------------------------------------------------
# Functions

def read_pcd_header(pcd_path):
    pcd_header = ""
    with open(pcd_path, "r") as pcd_file:
        for line_idx in range(1, 11): # indexing lines from 1 just to be consistent with actual line numberings in files
            pcd_header += pcd_file.readline()
    return pcd_header

def validate_pcd_header(pcd_header):
    raise NotImplementedError("PCD header validation not yet implemented! Please manually make sure your PCD files are in the correct format and valid.")

def read_pcd_content(pcd_path):
    with open(pcd_path, "r") as pcd_file:
        pcd_content = "".join(pcd_file.readlines()[10:]) # The first 10 lines are the header, we skip it when reading for content
    return pcd_content

# A standard PCD header has this format:
# VERSION .7
# FIELDS x y z intensity ring time
# SIZE 4 4 4 4 2 4
# TYPE f f f f u f
# COUNT 1 1 1 1 1 1
# WIDTH 16
# HEIGHT 912
# VIEWPOINT 0 0 0 1 0 0 0
# POINTS 14592
# DATA ascii
def get_points_from_pcd_header(pcd_header):
    pcd_header_data = pcd_header.split("\n") # Tokenize the header into lines
    pcd_points_data = pcd_header_data[8].split(" ") # The 8. line contains the points count
    return int(pcd_points_data[1])

def construct_ply_header(pcd_header):
    ply_header =  "ply\n"
    ply_header += "format ascii 1.0\n"
    ply_header += f"element vertex {get_points_from_pcd_header(pcd_header)}\n"
    ply_header += "property float x\n"
    ply_header += "property float y\n"
    ply_header += "property float z\n"
    ply_header += "end_header\n"
    return ply_header

# It may be prudent to implement a conversion logic that converts the files line-by-line in case inputs and outputs become huge
def construct_ply_content(pcd_content):
    pcd_content_lines = pcd_content.split("\n")
    ply_content = ""
    
    for pcd_content_line in pcd_content_lines:
        # TODO: Implement skipping empty lines! Or write a function that removes such empty lines
        pcd_content_line_data = pcd_content_line.split(" ")
        # idx 0 data: x value, idx 1 data: y value, idx 2 data: z value
        ply_content += f"{pcd_content_line_data[0]} {pcd_content_line_data[1]} {pcd_content_line_data[2]}\n"
    
    return ply_content
    
def convert_pcd_to_ply(pcd_path):
    ply_path = Path(f"outputs/{pcd_path.name[:-4]}.ply")
    with open(ply_path, "w") as ply_file:
        ply_file.write(construct_ply_header(read_pcd_header(pcd_path)))
        ply_file.write(construct_ply_content(read_pcd_content(pcd_path)))

# --------------------------------------------------------------------------------------------------------------------------------
# Main script

input_folder = Path("inputs")
input_folder.mkdir(exist_ok = True)
# It is largely the user's responsibility to keep the inputs folder clean for use!

pcd_files = list(input_folder.glob("*.pcd"))

output_folder = Path("outputs")
output_folder.mkdir(exist_ok = True)
# It is largely the user's responsibility to keep the outputs folder clean for use!

for pcd_file in pcd_files:
    convert_pcd_to_ply(pcd_file)