from furniture_design.order import Order
from furniture_design.cabinets.Kitchen.kitchen import *
from furniture_design.cabinets.Dressing.dressing import *
from furniture_design.cabinets.elements.board import *
from furniture_design.cabinets.elements.accessory import *
from manufacturing.generate_files import generate_manufacturing_files
import os

order_data = {
    "client": "Bogdan Urs",
    "Client Proficut": "Bogdan Urs",
    "Tel Proficut": "0740472185",
    "Transport": "Nu",
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

c = Cabinet("c", 1000, 1000, 1000, rules)
t6_plinta = BoardPal("t6.plinta", 450, 100, 18, 0, 0, 1, 0)
c.append(t6_plinta)

t6_sep_h = BoardPal("t6.sep.h", 480, 478, 18, 1, 0, 0, 0)
t6_sep_h.move("z", 100)
c.append(t6_sep_h)

t6_sep_h_2 = BoardPal("t6.sep.h", 480, 478, 18, 1, 0, 0, 0)
t6_sep_h_2.move("z", 200)
c.append(t6_sep_h_2)

t6_sep_v = BoardPal("t6.sep.v", 1464, 498, 18, 1, 0, 0, 0)
t6_sep_v.move("z", 300)
c.append(t6_sep_v)

t6_sep_v_2 = BoardPal("t6.sep.v", 1464, 498, 18, 1, 0, 0, 0)
t6_sep_v_2.move("z", 400)
c.append(t6_sep_v_2)

t6_sep_h_long = BoardPal("t6.sep.h", 1368, 496, 18, 1, 0, 0, 0)
t6_sep_h_long.move("z", 500)
c.append(t6_sep_h_long)

pol_kalax = BoardPal("pol_kalax", 335, 370, 18, 1, 0, 0, 0)
pol_kalax.move("z", 600)
c.append(pol_kalax)

pol_kalax = BoardPal("pol_kalax", 335, 370, 18, 1, 0, 0, 0)
pol_kalax.move("z", 700)
c.append(pol_kalax)

usa_medeea = BoardPal("usa_med", 500, 1200, 18, 1, 1, 1, 1)
usa_medeea.move("z", 800)
c.append(usa_medeea)

order.append(c)
output_directory = "output"
os.makedirs(output_directory, exist_ok=True)
customer_output_directory = os.path.join(output_directory, str(os.path.basename(__file__)).replace(".py", "_output"))
os.makedirs(customer_output_directory, exist_ok=True)

generate_manufacturing_files(order, customer_output_directory)
