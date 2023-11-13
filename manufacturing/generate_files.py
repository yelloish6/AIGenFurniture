import os
from manufacturing.export_for_proficut import export_pal_for_proficut
from manufacturing.export_csv import export_csv
from manufacturing.export_stl import export_stl_comanda


def generate_manufacturing_files(comanda, output_path):
    '''
    generate_manufacturing_files is a function that takes a cabinet object and an output_path as arguments.
    The function creates the output directory if it doesn't exist.
    It generates a summary file (design_summary.txt) containing information about the cabinet's dimensions, materials,
    hardware, and additional features.
    You can customize this function to include additional logic for generating specific manufacturing files based on
    the type of cabinet.
    Adjust the code according to the specific manufacturing files you need for your project and the structure of your
    cabinet classes.
    '''

    # Create the output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)

    # Generate a summary file
    # summary_file_path = os.path.join(output_path, "design_summary.txt")
    # with open(summary_file_path, 'w') as summary_file:
    #     summary_file.write("Manufacturing Summary:\n")
    #     summary_file.write(f"Dimensions: {cabinet.dimensions}\n")
    #     summary_file.write(f"Materials: {cabinet.materials}\n")
    #     summary_file.write(f"Hardware: {cabinet.hardware}\n")
    #     summary_file.write(f"Additional Features: {', '.join(cabinet.additional_features)}\n")

    # You can add more logic here to generate additional manufacturing files based on cabinet type
    # For example, cutting diagrams, assembly instructions, etc.
    export_pal_for_proficut(comanda, output_path)
    export_csv(comanda, output_path)
    export_stl_comanda(comanda, output_path)
    print(f"Manufacturing files generated in: {output_path}")

