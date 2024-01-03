# AutoCad_Operations
This repository contains codes for performing autocad operations like drawing, fetching details, converting dwg to dxf format etc.

Repository Description
1. DWG to DXF Converter
This repository hosts Python code for a DWG to DXF converter. Utilizing the subprocess module, it seamlessly integrates with the ODAFileConverter tool, commonly employed for converting DWG files to various formats. Key features include:

Constants:
TEIGHA_PATH: Path to the ODAFileConverter executable.
INPUT_FOLDER: Folder containing input DWG files.
OUTPUT_FOLDER: Folder for storing converted files.
OUTVER: AutoCAD file format version for conversion (ACAD2018).
OUTFORMAT: Output file format for conversion (DXF).
RECURSIVE: Flag for recursive subdirectory processing (0 for no, 1 for yes).
AUDIT: Flag for auditing each input file during conversion (0 for no, 1 for yes).
INPUTFILTER: Optional filter for input files (e.g., "*.DWG").

Command Building:
The script constructs a command (cmd) as a list of arguments, including the ODAFileConverter path and all parameters.

Execution:
The subprocess.run function executes the command in the shell, with shell=True indicating a shell environment.

Outcome:
ODAFileConverter runs with specified parameters, converting DWG files to DXF format in the output folder, potentially auditing and recursing based on provided flags. Note: Validate the correct ODAFileConverter executable path (TEIGHA_PATH) and handle paths properly, especially those with spaces or special characters.

2. Drawing into DXF using pyautocad
This Python script employs the pyautocad library to interact programmatically with AutoCAD. Key functionalities include:

Importing the Library: import pyautocad
Creating an AutoCAD Object: acad = pyautocad.Autocad()
Drawing Operations:
      Accessing the active document.
      Opening a DWG file.
      Creating and adding a line.
      Saving and closing the document.

In summary, this script serves as a basic example of creating and modifying drawings in AutoCAD using Python.

3. Drawing in DXF using ezdxf Library
This Python script utilizes the ezdxf library to read a DXF file, add a line to its modelspace, and save the modified drawing as a new DWG file. Key components include:

Importing the Libraries:import ezdxf
from ezdxf.math import Vec3

Drawing Operations:Reading an existing DXF file.
                   Accessing the modelspace.
                   Defining start and end points.
                   Adding a line to the modelspace.
                   Saving the modified drawing.
The script also includes commented-out sections demonstrating alternative methods for similar results.

4. Getting Details from a DXF File
This Python script utilizes the ezdxf library to extract details from a DXF file, focusing on TEXT entities. Key steps include:

Breakdown of the Code:
        Importing the ezdxf module.
        Reading a DXF file.
        Accessing the model space.
        Extracting details from TEXT entities.
        Printing the extracted details.
(Optional) The script includes commented-out code for extracting information from other entity types such as LINE and POLYLINE. Additional commented-out sections show alternative approaches and saving polyline data to a JSON file.

In essence, this code demonstrates how to use the ezdxf library to extract information, primarily from TEXT entities, in a DXF file.


ANY SUUGGESTIONS IS WARMLY WELCOMED!!!!!!!!!!!!!
