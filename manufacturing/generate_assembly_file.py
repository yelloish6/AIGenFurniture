import fitz
import math
from furniture_design.cabinets.elements.board import Board

VIEW_ANGLE = 30
DRAW_AREA = [500, 700]
DRAW_AREA_START = [50, 50]


def generate_assembly_file(order, output_path):
    doc = fitz.open()
    angle_z = math.sin(math.radians(VIEW_ANGLE))
    angle_x = math.cos(math.radians(VIEW_ANGLE))
    for cabinet in order.cabinets_list:

        page = doc.new_page()
        shape = page.new_shape()
        shape.insert_text(fitz.Point(DRAW_AREA_START[0], DRAW_AREA_START[1]), cabinet.label)
        scale_factor = max((cabinet.height + cabinet.depth * angle_z)/DRAW_AREA[1], (cabinet.width + cabinet.depth * angle_x)/DRAW_AREA[0])
        # find the overall cabinet offset on X and Y axis
        offset_min_x = math.inf
        offset_min_y = math.inf
        for element in cabinet.elements_list:
            if isinstance(element, Board):
                if element.position[3] < offset_min_x:
                    offset_min_x = element.position[3]
                if element.position[4] < offset_min_y:
                    offset_min_y = element.position[4]
        for element in cabinet.elements_list:
            if isinstance(element, Board):
                label = element.label
                pos = [0, 0, 0, 0, 0, 0]
                for i in range(3):
                    if element.position[i] < 0:
                        pos[i] = element.position[i] * -1
                        pos[i+3] = element.position[i+3] + element.position[i]
                    else:
                        pos[i] = element.position[i]
                        pos[i + 3] = element.position[i + 3]

                width = pos[0] / scale_factor
                depth = pos[1] / scale_factor
                height = pos[2] / scale_factor

                ox = DRAW_AREA_START[0]+ pos[3]/scale_factor + pos[4] / scale_factor * angle_x - offset_min_x / scale_factor
                oz = DRAW_AREA_START[1] + DRAW_AREA[1] - (pos[5] / scale_factor) - (pos[4] / scale_factor * angle_z) - height # - offset_min_y / scale_factor

                origin = fitz.Point(ox, oz)
                p1 = fitz.Point(ox + depth * angle_x, oz - depth * angle_z)
                p2 = fitz.Point(ox + depth * angle_x + width, oz - depth * angle_z)
                p3 = fitz.Point(ox + width, oz)
                p4 = fitz.Point(ox + width, oz + height)
                p5 = fitz.Point(ox + depth * angle_x + width, oz + height - depth * angle_z)
                p6_2 = fitz.Point(origin.x + (p5.x - origin.x)/2, origin.y + (p5.y - origin.y)/2)
                p6 = fitz.Point(ox, oz + height)
                # print(ox, oz, ox + depth * angle_z, oz + depth * angle_x)

                face = fitz.Rect(origin, p4)
                top = fitz.Quad(p1, p2, origin, p3)
                lateral = fitz.Quad(p3, p2, p4, p5)
                shape.draw_rect(face)
                shape.draw_quad(top)
                shape.draw_quad(lateral)
                # shape.finish(color=(0, 0, 0), fill=(1, 1, 1), width=1, fill_opacity=0.5)
                shape.insert_text(p6_2, label)
                # shape.insert_text(label)
                print(label, pos)
        shape.draw_rect([1, 1, 594, 841]) # the size of one page
        # shape.draw_rect([50, 50, 550, 750]) # rectangle around the drawing
        shape.finish(color=(0, 0, 0), fill=(1, 1, 1), width=1, fill_opacity=1)
        shape.commit()
    doc.save(output_path + '/Assembly_file.pdf')
