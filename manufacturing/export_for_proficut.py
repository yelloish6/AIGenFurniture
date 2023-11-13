from furniture_design.comanda import Comanda
import openpyxl
import shutil

def export_pal_for_proficut(Comanda, output_folder):
    # self.create_folder()
    folder_name = output_folder
    comanda = Comanda

    shutil.copyfile("manufacturing/templates/Cote-Proficut-2018.xlsx", folder_name + "/Comanda_Proficut_" + comanda.client + ".xlsx")

    file = openpyxl.load_workbook(folder_name + "/Comanda_Proficut_" + comanda.client + ".xlsx")
    sheet = file.get_sheet_by_name("Sheet1")
    sheet['C1'] = comanda.client_proficut
    sheet['D2'] = comanda.tel_proficut
    sheet['D3'] = comanda.transport
    sheet['C4'] = comanda.adresa
    sheet['G4'] = comanda.mat_pal

    counter = 0
    for corp in comanda.designed_cabinets:
        for element in corp.material_list:
            if element.type == "pal":
                sheet['A' + str(10 + counter)] = "1"
                sheet['B' + str(10 + counter)] = element.length
                sheet['C' + str(10 + counter)] = element.width
                sheet['D' + str(10 + counter)] = 0
                sheet['E' + str(10 + counter)] = element.label
                sheet['F' + str(10 + counter)] = element.cant_list[0]
                sheet['G' + str(10 + counter)] = element.cant_list[1]
                sheet['H' + str(10 + counter)] = element.cant_list[2]
                sheet['I' + str(10 + counter)] = element.cant_list[3]
                counter += 1
    file.save(folder_name + "/Comanda_Proficut_" + comanda.client + ".xlsx")