from furniture_design.order import Order
from furniture_design.cabinets.Kitchen.kitchen import *
from furniture_design.cabinets.Dressing.dressing import *
from furniture_design.cabinets.elements.board import *
from furniture_design.cabinets.elements.accessory import *
from manufacturing.generate_files import generate_manufacturing_files
import os

order_data = {
    "client": "Florarie_Mosnita",
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
    "material_front": "Riflaj Alb",
    "material_blat": "Stejar Halifax 600",
    "material_pfl": "Alb",
    "h_rate": 120,
    "discount": 0,
    "nr_electrocasnice": 1,
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

order = Order(order_data)

c9 = BaseBox("C9", 850, 670, 460, rules)
c9.add_pol(2,2)
c9.remove_all_pfl()
c9.remove_element("blat", "C9.blat")

rifl1 = Front("Riflaj1", 499, 900, 18)
rifl1.rotate("x")
rifl1.move("y", c9.depth + c9.thick_pal + 1)
rifl1.move("z", -50)
c9.append(rifl1)

spate1 = BoardPal("C9.spate1", 2748, 900, 18, 1,1,1,1)
spate1.rotate("x")
spate1.move("y", c9.depth + c9.thick_pal + 1)
spate1.move("x", rifl1.length + 2)
spate1.move("z", -50)
c9.append(spate1)

rifl2 = Front("Riflaj2", 499, 900, 18)
rifl2.rotate("x")
rifl2.move("y", c9.depth + c9.thick_pal + 1)
rifl2.move("x", rifl1.length + spate1.length + 4)
rifl2.move("z", -50)
c9.append(rifl2)

order.append(c9)

placa_int = BoardPal("C8.intermediar", 400, 460, 18, 1,0,0,0)
placa_int.move("z", 500)
cc = Cabinet("dummy", 850, 400, 460, rules)
cc.append(placa_int)
order.append(cc)

c8 = BaseBox("C8", 850, 400, 460, rules)
c8.add_drawer_a_pal(200, 0)
c8.add_drawer_a_pal(200, 300)
c8.add_drawer_a_pal(200, 600)
c8.add_front([[33, 100], [33, 100], [33, 100]], "drawer")
c8.remove_all_pfl()
c8.remove_element("blat", "C8.blat")

order.append(c8)

cc = Cabinet("dummy", 850, 800, 460, rules)
cc.append(Accessory("bara haine dr", 3))
order.append(cc)

c7 = BaseBox("C7", 850, 400, 460, rules)
c7.add_drawer_a_pal(200, 0)
c7.add_drawer_a_pal(200, 300)
c7.add_drawer_a_pal(200, 600)
c7.add_front([[33, 100], [33, 100], [33, 100]], "drawer")
c7.remove_all_pfl()
c7.remove_element("blat", "C7.blat")
order.append(c7)

placa_int = BoardPal("C6.intermediar", 400, 460, 18, 1,0,0,0)
placa_int.move("z", 500)
cc = Cabinet("dummy", 850, 400, 460, rules)
cc.append(placa_int)
order.append(cc)

c6 = BaseBox("C6", 850, 680, 460, rules)
c6.add_pol(2, 2)
c6.remove_all_pfl()
c6.remove_element("blat", "C6.blat")
order.append(c6)

c5 = BaseCornerShelf("C5", 850, 460, 480, 2, rules)
c5.remove_all_pfl()
c5.rotate_corp("z")
c5.rotate_corp("z")
c5.rotate_corp("z")
c5.move_corp("x", c5.depth)
#TODO asta trebe decupat pe curba
order.append(c5)

c4 = BaseBox("C4", 850, 1100, 480, rules)
c4.remove_all_pfl()
c4.add_drawer_b_pal(50, 700)
c4.add_drawer_a_pal(100, 400)
c4.add_drawer_a_pal(200, 20)
c4.add_front([[44, 100], [28, 100]], "drawer")
c4.add_sep_h(c4.width - (2 * c4.thick_pal), 0, 650, 1)
c4.remove_element("blat", "C4.blat")
spate3 = BoardPal("C4.spate", 1100, 900, 18, 1,1,1,1)
spate3.rotate("x")
spate3.move("y", c4.depth + c4.thick_pal + 1)
spate3.move("z", - 50)
c4.append(spate3)
c4.rotate_corp("z")
c4.move_corp("y", -1)
c4.move_corp("x", -c4.depth + c4.thick_pal + 1)

# c4.rotate("z")
# c4.rotate("z")
# c4.rotate("z")
# c4.move("x", -c1.width - (2 * c2.width) - c3.depth)
# c4.move("y", -c4.width)
order.append(c4)

c3 = BaseBox("C3", 850, 580, 480, rules)
c3.add_pol(2, 2)
c3.remove_element("blat", "C3.blat")
# c3.rotate("z")
# c3.move("y", c3.width)
# c3.move("x", -c1.width - (2 * c2.width) - c3.depth)
order.append(c3)

c2 = BaseBox("C2", 850, 1600, 530, rules)
c2.add_pol(2, 2)
# c2.remove_all_pfl()
c2.remove_element("blat", "C2.blat")
# c2.move("x", -c1.width - c2.width)
order.append(c2)

c1 = SinkBox("C1", 850, 900,530, rules)
c1.add_front([[100, 50], [100, 50]], "door")
c1.remove_element("blat", "C1.blat")
c1.remove_all_pfl()
order.append(c1)

cc = Cabinet("dummy", 900, 4000, 600, rules)

blat1 = Blat("blat1", 500, 500, 40)
cc.append(blat1)

blat2 = Blat("blat2", 3750, 500, 40)
blat2.move("z", 100)
cc.append(blat2)

blat3 = Blat("blat3", 3000, 600, 40)
blat3.move("z", 150)
cc.append(blat3)

order.append(cc)

output_directory = "output"
os.makedirs(output_directory, exist_ok=True)
customer_output_directory = os.path.join(output_directory, str(os.path.basename(__file__)).replace(".py", "_output"))
os.makedirs(customer_output_directory, exist_ok=True)

generate_manufacturing_files(order, customer_output_directory)
