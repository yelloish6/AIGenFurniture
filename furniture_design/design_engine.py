from furniture_design.cabinets.Kitchen.sink_box import SinkBox
from furniture_design.cabinets.Kitchen.raft import Raft
from .__init__ import rules
from furniture_design.comanda import Comanda

'''
The design_furniture function is the main entry point for designing furniture. It checks the cabinet_type from the 
customer input and calls specific design functions based on the type.
design_kitchen_cabinet and design_wardrobe_cabinet are design functions for specific cabinet types. They extract 
relevant information from the customer input and use it to create instances of the KitchenCabinet and WardrobeCabinet 
classes, respectively.
Make sure to adjust these functions according to the specific attributes and logic you have in your cabinet classes 
and customer input data. Additionally, you might want to add error handling and validation based on your 
project requirements.
'''

from .cabinets.kitchen_cabinet import KitchenCabinet
from .cabinets.wardrobe_cabinet import WardrobeCabinet


def design_furniture(customer_data):
    comanda = Comanda(customer_data)
    # customer_name = customer_data.get("client")
    cabinets_data = customer_data.get("cabinets", [])
    #
    # designed_cabinets = []

    for cabinet_data in cabinets_data:
        cabinet_type = cabinet_data.get("cabinet_type")

        if cabinet_type == "kitchen":
            designed_cabinet = design_kitchen_cabinet(cabinet_data)
        elif cabinet_type == "wardrobe":
            designed_cabinet = design_wardrobe_cabinet(cabinet_data)
        elif cabinet_type == "SinkBox":
            designed_cabinet = design_sink_box(cabinet_data)
        elif cabinet_type == "Raft":
            designed_cabinet = design_raft(cabinet_data)
        else:
            raise ValueError(f"Unsupported cabinet type: {cabinet_type}")

        if "additional_features" in cabinet_data:
            additional_features = cabinet_data.get("additional_features")
            if "front" in additional_features:
                front_param = additional_features.get("front")
                designed_cabinet.add_front(front_param.get("split_list"), front_param.get("front_type"))
            else:
                print("additional feature not found")
        else:
            print("no additional features")

        if "positioning" in cabinet_data:
            positioning = cabinet_data.get("positioning")
            if "move" in positioning:
                move_param = positioning.get("move")
                for i in range(len(move_param)):
                    designed_cabinet.move_corp(move_param[i][0], move_param[i][1])
            else:
                print("does not move")
            if "rotate" in positioning:
                rot_param = positioning.get("rotate")
                for i in range(len(rot_param)):
                    designed_cabinet.rotate_corp(rot_param[i])
            else:
                print("does not rotate")
        else:
            print("no positioning")

        comanda.append(designed_cabinet)

    return comanda

def design_kitchen_cabinet(cabinet_data):
    dimensions = cabinet_data.get("dimensions", {})
    materials = cabinet_data.get("materials", {})
    hardware = cabinet_data.get("hardware", {})
    additional_features = cabinet_data.get("additional_features", [])
    has_sink = cabinet_data.get("has_sink", False)
    has_stove = cabinet_data.get("has_stove", False)

    return KitchenCabinet(dimensions, materials, hardware, additional_features, has_sink, has_stove)

def design_wardrobe_cabinet(cabinet_data):
    dimensions = cabinet_data.get("dimensions", {})
    materials = cabinet_data.get("materials", {})
    hardware = cabinet_data.get("hardware", {})
    additional_features = cabinet_data.get("additional_features", [])
    has_mirror = cabinet_data.get("has_mirror", False)
    has_drawers = cabinet_data.get("has_drawers", False)

    return WardrobeCabinet(dimensions, materials, hardware, additional_features, has_mirror, has_drawers)


def design_sink_box(cabinet_data):
    label = cabinet_data.get("label", {})
    height = cabinet_data.get("height")
    width = cabinet_data.get("width")
    depth = cabinet_data.get("depth")

    return SinkBox(label, height, width, depth, rules)


def design_raft(cabinet_data):
    label = cabinet_data.get("label", {})
    height = cabinet_data.get("height")
    width = cabinet_data.get("width")
    depth = cabinet_data.get("depth")
    shelves = cabinet_data.get("shelves")

    return Raft(label, height, width, depth, shelves, rules)