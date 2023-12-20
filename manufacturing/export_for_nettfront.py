import openpyxl
import shutil


def export_front_for_nettfront(order, output_folder):

    file_path = output_folder + "/Comanda_Front_" + order.mat_front + "_" + order.client + ".xlsx"
    shutil.copyfile("manufacturing/templates/Formular_de_comanda_nett_front.xlsx", file_path)
    file = openpyxl.load_workbook(file_path)
    sheet = file.get_sheet_by_name("Sheet1")

    sheet['C17'] = order.mat_front

    counter = 0
    for cabinet in order.cabinets_list:
        for element in cabinet.elements_list:
            if element.type == "front":
                sheet['B' + str(21 + counter)] = element.length
                sheet['C' + str(21 + counter)] = element.width
                sheet['D' + str(21 + counter)] = 1
                sheet['F' + str(21 + counter)] = element.label
                counter += 1
    file.save(file_path)
