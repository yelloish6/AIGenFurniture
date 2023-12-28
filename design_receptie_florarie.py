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
    "material_front": "Alb Riflat A356R3",
    "material_blat": "Stejar Halifax 600",
    "material_pfl": "Alb",
    "h_rate": 110,
    "discount": 0,
    "nr_electrocasnice": 1,
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

c9 = BaseBox("C9", 900 - rules["thick_blat"] - rules["height_legs"], 670, 460, rules)
c9.add_pol(2,2)
c9.remove_all_pfl()
c9.remove_element("blat", "C9.blat")

rifl1 = Front("Riflaj1", 499, c9.height, 18)
rifl1.rotate("x")
rifl1.move("y", c9.depth + c9.thick_pal + 1)
rifl1.move("z", 2)
c9.append(rifl1)

spate1 = BoardPal("C9.spate1", 2748, c9.height, 18, 1,1,1,1)
spate1.rotate("x")
spate1.move("y", c9.depth + c9.thick_pal + 1)
spate1.move("x", rifl1.length + 2)
spate1.move("z", 2)
c9.append(spate1)

rifl2 = Front("Riflaj2", 499, c9.height, 18)
rifl2.rotate("x")
rifl2.move("y", c9.depth + c9.thick_pal + 1)
rifl2.move("x", rifl1.length + spate1.length + 4)
rifl2.move("z", 2)
c9.append(rifl2)

order.append(c9)

placa_int = BoardPal("C9.intermediar", 400, 460, 18, 1,0,0,0)
placa_int.move("z", 500)
cc = Cabinet("dummy", 900 - rules["thick_blat"] - rules["height_legs"], 400, 460, rules)
cc.append(placa_int)
order.append(cc)

c8 = BaseBox("C8", 900 - rules["thick_blat"] - rules["height_legs"], 400, 460, rules)
c8.add_drawer_a_pal(150, 20)
c8.add_drawer_a_pal(150, 250)
c8.add_drawer_a_pal(150, 500)
for i in range(3):
    front_pal = BoardPal("C8.front", c8.width - 4, int((c8.height - 8)/3) - 50, c8.thick_pal, 2, 2, 2, 2)
    front_pal.rotate("x")
    front_pal.move("x",2)
    front_pal.move("z",2 + i * (front_pal.width + 50))
    c8.append(front_pal)

# front_pal.move("z", front_pal.length + 2)
# c8.append(front_pal)
# front_pal.move("z", front_pal.length + 2)
# c8.append(front_pal)
# c8.add_front([[33, 100], [33, 100], [33, 100]], "drawer")
c8.remove_all_pfl()
c8.remove_element("blat", "C8.blat")

order.append(c8)

cc = Cabinet("dummy", 900 - rules["thick_blat"] - rules["height_legs"], 800, 460, rules)
cc.append(Accessory("bara haine dr", 3))
order.append(cc)

c7 = BaseBox("C7", 900 - rules["thick_blat"] - rules["height_legs"], 400, 460, rules)
c7.add_drawer_a_pal(150, 20)
c7.add_drawer_a_pal(150, 250)
c7.add_drawer_a_pal(150, 500)
for i in range(3):
    front_pal = BoardPal("C7.front", c8.width - 4, int((c8.height - 8)/3) - 50, c8.thick_pal, 2, 2, 2, 2)
    front_pal.rotate("x")
    front_pal.move("x", 2)
    front_pal.move("z", 2 + i * (front_pal.width + 50))
    c7.append(front_pal)
# c7.add_front([[33, 100], [33, 100], [33, 100]], "drawer")
c7.remove_all_pfl()
c7.remove_element("blat", "C7.blat")
order.append(c7)

placa_int = BoardPal("C6.intermediar", 400, 460, 18, 1,0,0,0)
placa_int.move("z", 500)
cc = Cabinet("dummy", 900 - rules["thick_blat"] - rules["height_legs"], 400, 460, rules)
cc.append(placa_int)
order.append(cc)

c6 = BaseBox("C6", 900 - rules["thick_blat"] - rules["height_legs"], 680, 460, rules)
c6.add_pol(2, 2)
c6.remove_all_pfl()
c6.remove_element("blat", "C6.blat")
order.append(c6)

c5 = BaseCornerShelf("C5", 900 - rules["thick_blat"] - rules["height_legs"], 460, 480, 2, rules, rounded=True)
c5.remove_all_pfl()
c5.rotate_corp("z")
c5.rotate_corp("z")
c5.rotate_corp("z")
c5.move_corp("x", c5.depth)
#TODO asta trebe decupat pe curba
order.append(c5)

c4 = BaseBox("C4", 900 - rules["thick_blat"] - rules["height_legs"], 1100, 480, rules)
c4.remove_all_pfl()
c4.add_drawer_a_pal(50, 650)
c4.add_drawer_a_pal(100, 400)
c4.add_drawer_a_pal(200, 20)

front_pal1 = BoardPal("C4.front1", c4.width - 4, 396 - 50, c4.thick_pal, 2, 2, 2, 2)
front_pal1.rotate("x")
front_pal1.move("x", 2)
front_pal1.move("z", 2)
c4.append(front_pal1)

front_pal2 = BoardPal("C4.front2", c4.width - 4, 246 - 50, c4.thick_pal, 2, 2, 2, 2)
front_pal2.rotate("x")
front_pal2.move("x", 2)
front_pal2.move("z", 2 + 400)
c4.append(front_pal2)

# c4.add_front([[44, 100], [28, 100]], "drawer")
c4.add_sep_h(c4.width - (2 * c4.thick_pal), 0, 600, 1)
c4.remove_element("blat", "C4.blat")
spate3 = BoardPal("C4.spate", 1100, c4.height, 18, 1,1,1,1)
spate3.rotate("x")
spate3.move("y", c4.depth + c4.thick_pal + 1)
spate3.move("z", 2)
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

c3 = BaseBox("C3", 900 - rules["thick_blat"] - rules["height_legs"], 580, 480, rules)
c3.add_pol(2, 2)
c3.remove_element("blat", "C3.blat")
c3.rotate_corp("z")
c3.rotate_corp("z")
c3.rotate_corp("z")
c3.move_corp("y", - c4.width - c5.width - 122)
c3.move_corp("x", -c4.width + c4.thick_pal)
order.append(c3)

c2 = BaseBox("C2", 900 - rules["thick_blat"] - rules["height_legs"], 1600, 530, rules)
c2.add_pol(2, 2)
# c2.remove_all_pfl()
c2.remove_element("blat", "C2.blat")
c2.rotate_corp("z")
c2.rotate_corp("z")
c2.move_corp("y", -1000)
order.append(c2)

c1 = SinkBox("C1", 900 - rules["thick_blat"] - rules["height_legs"], 900,530, rules)
usa1 = BoardPal("C1.front1", int((c1.width - 6)/2), c1.height - 4, 18, 2, 2, 2, 2)
usa2 = BoardPal("C1.front1", int((c1.width - 6)/2), c1.height - 4, 18, 2, 2, 2, 2)
usa1.rotate("x")
usa2.rotate("x")
usa1.move("x", 2)
usa1.move("z", 2)
usa2.move("x", usa1.length + 4)
usa2.move("z", 2)
c1.append(usa1)
c1.append(usa2)
#c1.add_front([[100, 50], [100, 50]], "door")
c1.remove_element("blat", "C1.blat")
c1.remove_all_pfl()

c1.rotate_corp("z")
c1.rotate_corp("z")
order.append(c1)

cc = Cabinet("dummy", 1, 1, 1, rules)

blat1 = Blat("blat1", 500, 500, 40)
cc.append(blat1)

blat2 = Blat("blat2", 3750, 500, 40)
blat2.move("z", 100)
cc.append(blat2)
cc.append(Accessory("decupare blat", 1))


blat3 = Blat("blat3", 3000, 600, 40)
blat3.move("z", 150)
cc.append(blat3)

order.append(cc)

output_directory = "output"
os.makedirs(output_directory, exist_ok=True)
customer_output_directory = os.path.join(output_directory, str(os.path.basename(__file__)).replace(".py", "_output"))
os.makedirs(customer_output_directory, exist_ok=True)

generate_manufacturing_files(order, customer_output_directory)
