import os
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree

def create_annotation_elem(image_name, size):
    annotation_elem = Element('annotation')

    filename_elem = SubElement(annotation_elem, 'filename')
    filename_elem.text = image_name + '.jpg'
    
    size_elem = SubElement(annotation_elem, 'size')
    width_elem = SubElement(size_elem, 'width')
    width_elem.text = str(size[0])
    height_elem = SubElement(size_elem, 'height')
    height_elem.text = str(size[1])
    depth_elem = SubElement(size_elem, 'depth')
    depth_elem.text = '3'

    return annotation_elem

def add_object_elem(annotation_elem, label, xmin, ymin, xmax, ymax):
    object_elem = SubElement(annotation_elem, 'object')
    name_elem = SubElement(object_elem, 'name')
    name_elem.text = label
    bndbox_elem = SubElement(object_elem, 'bndbox')
    xmin_elem  = SubElement(bndbox_elem, 'xmin')
    xmin_elem.text = str(xmin)
    ymin_elem = SubElement(bndbox_elem, 'ymin')
    ymin_elem.text = str(ymin)
    xmax_elem = SubElement(bndbox_elem, 'xmax')
    xmax_elem.text = str(xmax)
    ymax_elem = SubElement(bndbox_elem, 'ymax')
    ymax_elem.text = str(ymax)


#coords_list is [[(xmin, ymin), (xmax, ymax)], ... ]
def generate_xml(image_name, size ,coords_list, labels, output_dir):
    #create annotation element
    annotation_elem = create_annotation_elem(image_name, size)

    for i, coords in enumerate(coords_list):
        xmin, ymin, xmax, ymax = coords[0][0], coords[0][1], coords[1][0], coords[1][1]
        label = labels[i]

        add_object_elem(annotation_elem, label, xmin, ymin, xmax, ymax)

    output_path = os.path.join(output_dir, image_name + '.xml')
    ElementTree(annotation_elem).write(output_path, encoding='UTF-8')


    
    