import ezdxf

# Read the DWG file
doc = ezdxf.readfile("C:/Users/DELL/Downloads/230222 test sample.dxf")

# Get the model space
msp = doc.modelspace()

# Extract details from entities
details = []
for entity in msp:
    if entity.dxftype() == 'TEXT':
        details.append({
            'type': 'TEXT',
            'text': entity.dxf.text,
            'layer': entity.dxf.layer,
            'color': entity.dxf.color,
            'position': entity.dxf.insert,
            'height': entity.dxf.height
        })
    # elif entity.dxftype() == 'LINE':
    #     details.append({
    #         'type': 'LINE',
    #         'start_point': entity.dxf.start,
    #         'end_point': entity.dxf.end,
    #         'layer': entity.dxf.layer,
    #         'color': entity.dxf.color,
    #         'linetype': entity.dxf.linetype
    #     })
    # elif entity.dxftype() == 'POLYLINE':
    #     vertices = entity.get_points('xy')
    #     details.append({
    #         'type': 'POLYLINE',
    #         'vertices': vertices,
    #         'layer': entity.dxf.layer,
    #         'color': entity.dxf.color,
    #         'linetype': entity.dxf.linetype
    #     })
    # add more entity types as needed

# Print the extracted details
for detail in details:
    print(detail,"++++++++++++++")












# import ezdxf
#
# doc = ezdxf.readfile("C:/Users/DELL/Downloads/230222 test sample.dxf")
#
# msp = doc.modelspace()
# texts = [entity.dxf.text for entity in msp if entity.dxftype() == 'TEXT']
#
# # Print the extracted text
# for text in texts:
#     print(text,"************************")





# for entity in doc.entities:
#     print(type(entity))
#
# polylines = doc.modelspace().query('POLYLINE')
# print(polylines)
#
# data = []
# for polyline in polylines:
#     print("hai")
#     vertices = polyline.get_points('xy')
#     data.append({
#         'type': 'polyline',
#         'vertices': vertices,
#     })
# print(data)
# import json
#
# with open('C:/Users/DELL/Downloads/autocadfile.json', 'w') as f:
#     json.dump(data, f)


