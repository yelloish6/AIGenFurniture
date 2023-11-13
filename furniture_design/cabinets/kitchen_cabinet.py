from .base_cabinet import BaseCabinet
import os

class KitchenCabinet(BaseCabinet):
    def __init__(self, dimensions, materials, hardware, additional_features=None, has_sink=False, has_stove=False):
        super().__init__(dimensions, materials, hardware, additional_features)
        self.has_sink = has_sink
        self.has_stove = has_stove

    def display_summary(self):
        super().display_summary()
        print(f"Kitchen Specifics: Sink - {self.has_sink}, Stove - {self.has_stove}")

    def generate_manufacturing_files(self, output_path):
        # Implement the logic to generate manufacturing files specific to a kitchen cabinet
        # You may use the base class method for common manufacturing file generation
        super().generate_manufacturing_files(output_path)

        # Add additional logic for kitchen cabinet manufacturing files
        # For example, generate files related to sink and stove installation
        sink_file_path = os.path.join(output_path, "sink_installation.txt")
        with open(sink_file_path, 'w') as sink_file:
            sink_file.write("Sink installation instructions.")

        stove_file_path = os.path.join(output_path, "stove_installation.txt")
        with open(stove_file_path, 'w') as stove_file:
            stove_file.write("Stove installation instructions.")
