from furniture_design.order import Order
from furniture_design.cabinets.Kitchen.kitchen import *
from furniture_design.cabinets.Dressing.dressing import *
from furniture_design.cabinets.elements.board import *
from furniture_design.cabinets.elements.accessory import *
from manufacturing.generate_files import generate_manufacturing_files
import os

order_data = {
    "client": "Costi Macritchi",
    "Client Proficut": "Bogdan Urs",
    "Tel Proficut": "0740472185",
    "Transport": "Da",
    "Adresa": "Mosnita Veche, str. Borsa, Nr. 38",
    "h_bucatarie": 2200,
    "h_faianta_top": 1470,
    "h_faianta_base": 900,
    "depth_base": 600,
    "top_height": 600,
    "top_height_2": 400,
    "top_depth": 600,
    "top_depth_2": 500,
    "blat_height": 850,
    "cuptor_height": 595,
    "MsV_height_min": 815,
    "MsV_height_max": 875,
    "material_pal": "Alb W962ST2",
    "material_front": "A34R3",
    "material_blat": "Stejar Alpin Keindl",
    "material_pfl": "Alb",
    "h_rate": 70,
    "discount": 100,
    "nr_electrocasnice": 3,
}

rules = {
    "thick_pal": 18,
    "thick_front": 18,
    "thick_blat": 38,
    "height_legs": 50,
    "general_width": 600,
    "width_blat": 600,
    "gap_spate": 50,
    "gap_fata": 50,
    "gap_front": 2,
    "cant_general": 1,
    "cant_pol": 2,
    "cant_separator": 1,
    "pol_depth": 20
}

order = Order(order_data)


c1 = MsVBox("C1", 800, 600, 550, rules)
# c1.add_front([[100, 100]], "door")
c1.move_corp("z", rules["height_legs"])
# c1.remove_element("blat", "C1.blat")
order.append(c1)

c2 = SinkBox("C2", 800, 600, 550, rules)
c2.add_front([[100, 100]], "door")
c2.move_corp("z", rules["height_legs"])
c2.remove_element("blat", "C2.blat")
order.append(c2)

c3 = BaseBox("C3", 800, 600, 550, rules)
c3.add_front([[20, 100]], "door")
c3.add_sep_h(600-36, 0, 130, 0)
c3.add_drawer_a_pfl(100, 25)
c3.move_corp("z", rules["height_legs"])
c3.remove_element("blat", "C3.blat")
c3.remove_element("pfl", "C3.pfl")
order.append(c3)

blat_cabinet = Cabinet("blat", 36, 1800, 600, rules)
blat = Blat("Blat", 1800, 600, 36)
blat_cabinet.append(blat)
blat_cabinet.move_corp("x", -1800)
blat_cabinet.move_corp("z", c1.height + rules["height_legs"])
blat_cabinet.move_corp("y", -20)
order.append(blat_cabinet)

c4 = TopBox("C4", 950, 600, 300, rules)
c4.add_front([[100, 47]], "door")
c4.add_front_lateral("left")
placa_fata = BoardPal("C4_fata", c4.height, c4.width/2 + c4.thick_pal, c4.thick_pal, 2,2,2,2)
placa_fata.rotate("x")
placa_fata.rotate("y")
placa_fata.move("x", c4.width)
c4.append(placa_fata)
c4.rotate_corp("z")
c4.rotate_corp("z")
c4.rotate_corp("z")
c4.move_corp("x", -c1.width-c2.width-c3.width-blat.length)
# c4.move_corp("y", 300)
c4.move_corp("z", order_data["h_bucatarie"] - c4.height)
c4.move_corp("x", c4.depth)
c4.remove_all_pfl()
order.append(c4)

position_top_cabinets = -c1.width-c2.width-c3.width-blat.length-c4.width+c4.depth+c4.thick_pal

c5 = TopBox("C5", 400, 541, 300, rules)
c5.add_front([[100, 50], [100, 50]], "door")
c5.add_pol(1, 2)
c5.move_corp("x", position_top_cabinets)
c5.move_corp("z", order_data["h_bucatarie"] - c5.height)
c5.move_corp("y", c4.width - c5.depth)
order.append(c5)

c6 = TopBox("C6", 400, 541, 300, rules)
c6.add_front([[100, 50], [100, 50]], "door")
c6.add_pol(1, 2)
c6.move_corp("x", position_top_cabinets)
c6.move_corp("z", order_data["h_bucatarie"] - c6.height)
c6.move_corp("y", c4.width - c6.depth)
order.append(c6)

c7 = TopBox("C7", 950, 400, 400, rules)
c7.add_front([[100, 100]], "door")
c7.add_pol(4, 2)
c7.move_corp("x", position_top_cabinets)
c7.move_corp("z", order_data["h_bucatarie"] - c7.height)
c7.move_corp("y", c4.width - c7.depth)
order.append(c7)



output_directory = "output"
os.makedirs(output_directory, exist_ok=True)
customer_output_directory = os.path.join(output_directory, str(os.path.basename(__file__)).replace(".py", "_output"))
os.makedirs(customer_output_directory, exist_ok=True)

generate_manufacturing_files(order, customer_output_directory)
