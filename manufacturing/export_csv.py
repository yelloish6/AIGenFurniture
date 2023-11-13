import os
import csv


def export_csv(Comanda, output_folder):
    # create folder with customer name if it doesn't exist
    folder_name = output_folder

    comanda = Comanda

    # output comanda pal
    name = os.path.join(folder_name, "comanda_pal_" + comanda.client + ".csv")
    corpuri = comanda.designed_cabinets

    with open(name, mode='w', newline="") as comanda_pal:
        comanda_writer = csv.writer(comanda_pal, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        comanda_writer.writerow(["Bucati", "Lungime", "Latime", "Orientabila", "Eticheta", "L1", "L2", "l1", "l2"])
        for corp in corpuri:
            for element in corp.material_list:
                if element.type == "pal":
                    comanda_writer.writerow(
                        [1, element.length, element.width, 0, element.label, element.cant_list[0],
                         element.cant_list[1], element.cant_list[2], element.cant_list[3]])

    # output comanda pfl
    name = os.path.join(folder_name, "comanda_pfl_" + comanda.client + ".csv")

    with open(name, mode='w', newline="") as comanda_pal:
        comanda_writer = csv.writer(comanda_pal, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        comanda_writer.writerow(["Bucati", "Lungime", "Latime", "Eticheta"])
        for corp in corpuri:
            for element in corp.material_list:
                if element.type == "pfl":
                    comanda_writer.writerow([1, element.length, element.width, element.label])

    # output comanda fronturi
    name = os.path.join(folder_name, "comanda_front_" + comanda.client + ".csv")

    with open(name, mode='w', newline="") as comanda_pal:
        comanda_writer = csv.writer(comanda_pal, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        comanda_writer.writerow(["Eticheta", "Lungime", "Latime", "Pret"])
        comanda_writer.writerow([comanda.mat_front])
        for corp in corpuri:
            for element in corp.material_list:
                if element.type == "front":
                    comanda_writer.writerow([element.label, element.length, element.width, element.price])

    # output comanda accesorii
    name = os.path.join(folder_name, "comanda_accesorii_" + comanda.client + ".csv")

    with open(name, mode='w', newline="") as comanda_pal:
        comanda_writer = csv.writer(comanda_pal, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        comanda_writer.writerow(["Nume", "Bucati", "Pret/buc", "Pret total"])
        # pe corpuri

        totals = []  # totals is a list containing total accessories and their amount and price

        for corp in corpuri:
            for element in corp.material_list:
                if element.type == "accesoriu":
                    comanda_writer.writerow(
                        [element.name, element.pieces, element.price, element.pieces * element.price])
                    found_in_totals = False
                    for i in range(len(totals)):
                        if totals[i][0] == element.name:
                            totals[i][1] += element.pieces
                            found_in_totals = True
                    if not found_in_totals:
                        totals.append([element.name, element.pieces, element.price])

        # total
        for i in range(len(totals)):
            # print(totals2[i][0], totals2[i][1], totals2[i][2], totals2[i][1] * totals2[i][2])
            comanda_writer.writerow(["TOTAL " + totals[i][0], totals[i][1], totals[i][2], totals[i][1] *
                                     totals[i][2]])

    # output pentru optimizare pal
    name = os.path.join(folder_name, "PannelsCuttingList_pal_" + comanda.client + ".csv")
    mobila = comanda.designed_cabinets
    with open(name, mode='w', newline="") as comanda_pal:
        comanda_writer = csv.writer(comanda_pal, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        comanda_writer.writerow(["Length", "Width", "Qty", "Label", "Enabled"])
        for corp in corpuri:
            for element in corp.material_list:
                if element.type == "pal":
                    comanda_writer.writerow([element.length, element.width, 1, element.label, "TRUE"])

    # pentru optimizare PFL
    name = os.path.join(folder_name, "PannelsCuttingList_pfl_" + comanda.client + ".csv")
    mobila = comanda.designed_cabinets
    with open(name, mode='w', newline="") as comanda_pal:
        comanda_writer = csv.writer(comanda_pal, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        comanda_writer.writerow(["Length", "Width", "Qty", "Enabled"])
        # pe corpuri
        for corp in corpuri:
            for element in corp.material_list:
                if element.type == "pfl":
                    comanda_writer.writerow([element.length, element.width, 1, element.label, "TRUE"])