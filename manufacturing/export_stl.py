# STL exporter
import os
from furniture_design.cabinets.elements.board import *


def export_stl_order(order, output_folder):
    file_name = os.path.join(output_folder, "3D " + order.client)

    offset = 0
    for cabinet in order.cabinets_list:
        cabinet.move_corp("x", offset)
        for material in cabinet.elements_list:
            if isinstance(material, Board):
                i = 0
                export_stl(file_name,
                           material.label + str(i),
                           material.position[0],
                           material.position[1],
                           material.position[2],
                           material.position[3],
                           material.position[4],
                           material.position[5])
                i += 1
        offset += cabinet.width + 1

        # cabinet.drawCorp(name, ox + ofset, oy, oz)
        # ofset = ofset + self.corpuri[i].width + 1


def export_stl_2(file_name, label, x, y, z, ox, oy, oz):
    """
    generates an stl file containing one board with given dimensions (x,y,z) and offset (ox, oy, oz)
    can be used in a loop
    :param file_name: name of the STL file to export to
    :param label: label of the piece being written
    :param x: size on x axis
    :param y: size on y axis
    :param z: size on z axis
    :param ox: orientation on x axis
    :param oy: orientation on y axis
    :param oz: orientation on x axis
    :return: n/a
    """
    name = file_name + ".stl"

    with open(name, mode='a') as stl_file:
        stl_file.write('solid ' + label + '\n')

        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')

        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')

        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')

        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')

        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')

        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')

        #		stl_file.write('    vertex 0.0 0.0 0.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 0.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex 0.0 0.0 '+str(z)+'.0'+'\n')

        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        #		stl_file.write('    vertex 0.0 '+str(y)+'.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex 0.0 0.0 0.0'+'\n')
        #		stl_file.write('    vertex 0.0 0.0 '+str(z)+'.0'+'\n')

        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        #		stl_file.write('    vertex 0.0 0.0 0.0'+'\n')
        #		stl_file.write('    vertex 0.0 '+str(y)+'.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex 0.0 '+str(y)+'.0 0.0'+'\n')

        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        #		stl_file.write('    vertex 0.0 '+str(y)+'.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 '+str(y)+'.0 0.0'+'\n')
        #		stl_file.write('    vertex 0.0 '+str(y)+'.0 0.0'+'\n')

        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        #		stl_file.write('    vertex '+str(x)+'.0 '+str(y)+'.0 0.0'+'\n')
        #		stl_file.write('    vertex 0.0 '+str(y)+'.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 '+str(y)+'.0 '+str(z)+'.0'+'\n')

        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        #		stl_file.write('    vertex '+str(x)+'.0 '+str(y)+'.0 0.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 0.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 0.0 0.0'+'\n')

        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        #		stl_file.write('    vertex '+str(x)+'.0 0.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 '+str(y)+'.0 0.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 '+str(y)+'.0 '+str(z)+'.0'+'\n')

        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('endsolid ' + label + '\n')


def export_stl(file_name, label, x, y, z, ox, oy, oz):
    """
    generates an stl file containing one board with given dimensions (x,y,z) and offset (ox, oy, oz)
    can be used in a loop
    :param file_name: name of the STL file to export to
    :param label: label of the piece being written
    :param x: size on x axis
    :param y: size on y axis
    :param z: size on z axis
    :param ox: orientation on x axis
    :param oy: orientation on y axis
    :param oz: orientation on x axis
    :return: n/a
    """
    file_name = file_name + ".stl"

    if not os.path.exists(file_name):
        # print("Create file and add the 'solid' line")
        create_new_file(file_name)
        # print("Write the board to write")
        write_board(file_name, label, x, y, z, ox, oy, oz)
        # print("write the end solid")

    else:
        # print("delete last row from file")
        delete_last_row(file_name)
        # print("Write the board to write")
        write_board(file_name, label, x, y, z, ox, oy, oz)
        # print("write the end solid")


def create_new_file(file_name):
    with open(file_name, mode='a') as stl_file:
        stl_file.write('solid ' + file_name + '\n')
    stl_file.close()


def delete_last_row(file_name):

    with open(file_name, mode='r') as stl_file:
        data = stl_file.readlines()
        data[len(data)-1] = ""
        # print(data)
    stl_file.close()

    with open(file_name, mode='w') as stl_file:
        stl_file.writelines(data)
    stl_file.close()


def write_board(file_name, label, x, y, z, ox, oy, oz):
    with open(file_name, mode='a') as stl_file:

        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')

        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')

        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')

        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')

        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')

        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')

        #		stl_file.write('    vertex 0.0 0.0 0.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 0.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex 0.0 0.0 '+str(z)+'.0'+'\n')

        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        #		stl_file.write('    vertex 0.0 '+str(y)+'.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex 0.0 0.0 0.0'+'\n')
        #		stl_file.write('    vertex 0.0 0.0 '+str(z)+'.0'+'\n')

        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        #		stl_file.write('    vertex 0.0 0.0 0.0'+'\n')
        #		stl_file.write('    vertex 0.0 '+str(y)+'.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex 0.0 '+str(y)+'.0 0.0'+'\n')

        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        #		stl_file.write('    vertex 0.0 '+str(y)+'.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 '+str(y)+'.0 0.0'+'\n')
        #		stl_file.write('    vertex 0.0 '+str(y)+'.0 0.0'+'\n')

        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        #		stl_file.write('    vertex '+str(x)+'.0 '+str(y)+'.0 0.0'+'\n')
        #		stl_file.write('    vertex 0.0 '+str(y)+'.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 '+str(y)+'.0 '+str(z)+'.0'+'\n')

        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        #		stl_file.write('    vertex '+str(x)+'.0 '+str(y)+'.0 0.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 0.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 0.0 0.0'+'\n')

        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        #		stl_file.write('    vertex '+str(x)+'.0 0.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 '+str(y)+'.0 0.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 '+str(y)+'.0 '+str(z)+'.0'+'\n')

        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('endsolid ' + file_name + '\n')
    stl_file.close()


def draw_cabinet(self, filename, ox, oy, oz):
    for i in range(len(self.elements_list)):
        if isinstance(self.elements_list[i], Board):
            export_stl(filename,
                       self.elements_list[i].label + str(i),
                       self.elements_list[i].position[0],
                       self.elements_list[i].position[1],
                       self.elements_list[i].position[2],
                       self.elements_list[i].position[3] + ox,
                       self.elements_list[i].position[4] + oy,
                       self.elements_list[i].position[5] + oz)


def draw(self, ox, oy, oz):
    folder_name = self.create_folder()
    name = os.path.join(folder_name, "3D " + self.client)
    if os.path.exists(name+".stl"):
        os.remove(name+".stl")
    offset = 0
    for i in range(len(self.corpuri)):
        self.corpuri[i].draw_cabinet(name, ox + offset, oy, oz)
        offset = offset + self.corpuri[i].width + 1