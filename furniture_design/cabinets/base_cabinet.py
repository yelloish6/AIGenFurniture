class BaseCabinet:
    def __init__(self, dimensions, materials, hardware, additional_features=None):
        self.dimensions = dimensions
        self.materials = materials
        self.hardware = hardware
        self.additional_features = additional_features or []

    def display_summary(self):
        print("Cabinet Summary:")
        print(f"Dimensions: {self.dimensions}")
        print(f"Materials: {self.materials}")
        print(f"Hardware: {self.hardware}")
        print(f"Additional Features: {', '.join(self.additional_features)}")

    def generate_manufacturing_files(self, output_path):
        # Implement the logic to generate manufacturing files based on the cabinet specifications
        pass
