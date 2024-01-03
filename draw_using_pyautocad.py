import pyautocad

acad = pyautocad.Autocad()

doc = acad.doc
docPath = "C:/Users/DELL/Downloads/230222 test sample.dwg"
doc.Application.Documents.Open(docPath)

lineStart = pyautocad.APoint(0, 0)
lineEnd = pyautocad.APoint(10, 10)
line = acad.model.AddLine(lineStart, lineEnd)

doc.Save()
doc.Close()
