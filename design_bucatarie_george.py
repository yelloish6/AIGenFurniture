from furniture_design.order import Order
from furniture_design.cabinets.Kitchen.kitchen import *
from furniture_design.cabinets.Dressing.dressing import *
from furniture_design.cabinets.elements.board import *
from furniture_design.cabinets.elements.accessory import *
from manufacturing.generate_files import generate_manufacturing_files
import os

order_data = {
    "client": "George Mihes",
    "Client Proficut": "Bogdan Urs",
    "Tel Proficut": "0740472185",
    "Transport": "Da",
    "Adresa": "Mosnita Veche, str. Borsa, Nr. 38",
    "h_bucatarie": 2200,
    "h_faianta_top": 1470,
    "h_faianta_base": 900,
    "depth_base": 600,
    "top_height": 500,
    "top_height_2": 0,
    "top_depth": 400,
    "top_depth_2": 0,
    "blat_height": 880,
    "cuptor_height": 595, #TODO confirm oven dimensions
    "MsV_height_min": 815, #TODO confirm MsV dimsntions
    "MsV_height_max": 875, #TODO confirm MsV dimsntions
    "material_pal": "Alb W962ST2", #TODO confirm materials
    "material_front": "A34R3", #TODO confirm materials
    "material_blat": "Stejar Halifax 600", #TODO confirm materials
    "material_pfl": "Alb", #TODO confirm materials
    "h_rate": 70,
    "h_proiect": 8,
    "discount": 50,
    "nr_electrocasnice": 5,
}

rules = {
    "thick_pal": 18,
    "thick_front": 18,
    "thick_blat": 38,
    "height_legs": 100,
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

base_height = order_data["blat_height"] - rules["thick_blat"] - rules["height_legs"]
base_depth = order_data["depth_base"] - rules["gap_spate"] - rules["gap_fata"]

top_height = order_data["top_height"]
top_depth = order_data["top_depth"]

gen_width = rules["general_width"]

order = Order(order_data)

t1 = Raft("T1", 2000, 600, 600, 0, rules)
t1.add_front([[100,100]],"door")
order.append(t1)

c1 = BaseBox("C1", base_height, gen_width, base_depth, rules)
c1.add_tandem_box("M",0) #TODO punem tandembox sau alte sisteme smechere de sertare?
c1.add_tandem_box("M",300)
c1.add_tandem_box("D",600)
c1.add_front([[40,100],[40,100],[20,100]],"drawer")
c1.remove_element("blat","C1.blat")
order.append(c1)

c2 = BaseCorner("C2", base_height, 900, 900, rules, 300, 300, "right", False)
order.append(c2)

c3 = BaseBox("C3", base_height, gen_width, base_depth, rules)
c3.add_tandem_box("M", 0)
c3.add_pol(2, 1)
c3.add_front([[20,100]],"drawer")
c3.remove_element("blat","C3.blat")
order.append(c3)

c4 = MsVBox("C4", base_height, 450, base_depth, rules)
order.append(c4)

c5 = SinkBox("C5", base_height, 1100, base_depth, rules)
c5.add_front([[100, 50],[100,50]],"door")
c5.remove_element("blat","C5.blat")
order.append(c5)

c6 = JollyBox("C6", base_height, 150, base_depth, rules)
c6.remove_element("blat","C6.blat")
order.append(c6)

s1 = TopBox("S1", top_height, gen_width, top_depth, rules)
s1.add_pol(1,2)
s1.add_front([[100,50],[100,50]],"door")
order.append(s1)

s2 = TopBox("S2", top_height, 300, top_depth, rules)
s2.add_pol(1,2)
s2.add_front([[100,100]],"door")
order.append(s2)

s3 = TopCorner("S3", top_height, 600, 700, rules, 200, 300, "right", 1)
order.append(s3)

s4 = TopBox("S4", top_height, 212, top_depth, rules)
s4.add_front([[100,100]],"door")
order.append(s4)

s5 = TopBox("S5", top_height - 50, gen_width, top_depth, rules)
s5.add_front([[100,50],[100,50]],"door")
order.append(s5)

blat_cabinet = Cabinet("blat", 36, 1500+2600, 600, rules)
blat = Blat("Blat", 1500, 600, 36)
blat2 = Blat("Blat2", 2600, 600, 36)
blat_cabinet.append(blat)
blat_cabinet.append(blat2)
order.append(blat_cabinet)

output_directory = "output"
os.makedirs(output_directory, exist_ok=True)
customer_output_directory = os.path.join(output_directory, str(os.path.basename(__file__)).replace(".py", "_output"))
os.makedirs(customer_output_directory, exist_ok=True)

generate_manufacturing_files(order, customer_output_directory)
