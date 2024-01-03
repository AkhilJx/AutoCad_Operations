import ezdxf
from ezdxf.math import Vec3

# dwg = ezdxf.new('AC1024')  # creates a new .dwg file with AutoCAD 2010 compatibility
# modelspace = dwg.modelspace()  # access the modelspace to add entities


doc = ezdxf.readfile("C:/Users/DELL/Downloads/230222 test sample.dxf")
modelspace = doc.modelspace()


start_point = Vec3(490191028.5511508, 2789121173.46078, 0.0)  # the start point of the line
end_point = Vec3(490200000, 2789120000.46078, 0)  # the end point of the line
modelspace.add_line(start_point, end_point)  # add the line to the modelspace

doc.saveas('drawing2.dwg')

















# import ezdxf
#
# # Load the .dwg file
# dwg = ezdxf.readfile("C:/Users/DELL/Downloads/230222 test sample.dwg")
#
# # Save the drawing to a .dxf file
# dwg.saveas("C:/Users/DELL/Downloads/output.dxf")

# import subprocess
#
# # Specify the path to your input DWG file and the desired output DXF file path
# input_file = "C:/Users/DELL/Downloads/230222 test sample.dwg"
# output_file = "C:/Users/DELL/Downloads/output.dxf"
#
# # Call dwg2dxf as a subprocess to convert the DWG file to DXF
# subprocess.call(["dwg2dxf", input_file, output_file])
