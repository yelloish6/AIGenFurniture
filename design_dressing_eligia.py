from furniture_design.order import Order
from furniture_design.cabinets.Kitchen.kitchen import *
from furniture_design.cabinets.Dressing.dressing import *
from furniture_design.cabinets.elements.board import *
from furniture_design.cabinets.elements.accessory import *
from manufacturing.generate_files import generate_manufacturing_files
import os

order_data = {
    "client": "Eligia Andrica",
    "Client Proficut": "Bogdan Urs",
    "Tel Proficut": "0740472185",
    "Transport": "Da",
    "Adresa": "Mosnita Veche, str. Borsa, Nr. 38",
    "h_bucatarie": 2070,
    "h_faianta_top": 1470,
    "h_faianta_base": 900,
    "depth_base": 500,
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
    "h_rate": 120,
    "discount": 100,
    "nr_electrocasnice": 6,
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
# order = Order()

for i in range(2):
    t1 = CorpCuPicioare("T1", 2500, 700, 550, 850, rules)
    #t1.add_sep_h(664, 0, 950, 1)
    for j in range(4):
        t1.add_pol_2("h", 664, 850 + ((2500-850-36-(4*18))/5 * (j+1)) + 18, 0)
    order.append(t1)

for i in range(2):
    t2 = CorpCuPicioare("T2", 2500, 700, 550, 100, rules)
    t2.add_drawer_b_pal(200, 130)
    t2.add_drawer_b_pal(200, 380)
    t2.add_sep_h(664, 0, 640, 1)
    t2.add_pfl()
    t2.append(Accessory("bara haine dr", 0.7))
    t2.append(Accessory("bara haine dr", 0.7))
    order.append(t2)

t5 = TopCorner("T5", 2500, 1000, 950, rules, 500, 400, "right", 7)
t5.remove_element("front", "T5_1")
t5.remove_element("front", "T5_2")
t5.move_corp("x", 2800)
t5.move_corp("y", -400)
order.append(t5)

t6 = CorpCuPicioare("T6", 2500, 1500, 500, 100, rules)
t6.add_pol(2, 1)
t6.add_pfl()
t6.append(Accessory("bara haine dr", 1.5))
t6.rotate_corp("z")
t6.rotate_corp("z")
t6.move_corp("y", -2000)
t6.move_corp("x", 3800)
order.append(t6)

output_directory = "output"
os.makedirs(output_directory, exist_ok=True)
customer_output_directory = os.path.join(output_directory, str(os.path.basename(__file__)).replace(".py", "_output"))
os.makedirs(customer_output_directory, exist_ok=True)

generate_manufacturing_files(order, customer_output_directory)
