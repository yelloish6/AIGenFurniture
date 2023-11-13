import os
import json
# from furniture_design.cabinets.kitchen_cabinet import KitchenCabinet  # Import specific cabinet type
from furniture_design.design_engine import design_furniture
from manufacturing.generate_files import generate_manufacturing_files

''' 
Loads customer input data from JSON files in the customer_input directory.
Uses the design_furniture function from the design_engine module to create an order based on customer input.
Displays a summary of the order.
Generates manufacturing files using the generate_manufacturing_files function from the manufacturing module.
Saves the manufacturing files in the customer's output directory within the output folder.
'''

def load_customer_input(input_file):
    with open(input_file, 'r') as file:
        return json.load(file)

def main():
    # Assuming your input files are in the customer_input directory
    input_directory = "customer_input"
    output_directory = "output"

    # Create output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    for input_file in os.listdir(input_directory):
        if input_file.endswith(".json"):
            input_path = os.path.join(input_directory, input_file)
            customer_data = load_customer_input(input_path)

            # Design the furniture based on customer input
            comanda = design_furniture(customer_data)

            # Display complete order
            comanda.print_comanda()

            # Generate manufacturing files and save to customer's output directory
            customer_output_directory = os.path.join(output_directory, input_file.replace(".json", "_output"))
            os.makedirs(customer_output_directory, exist_ok=True)

            generate_manufacturing_files(comanda, customer_output_directory)

if __name__ == "__main__":
    main()
