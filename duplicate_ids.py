import sys
import xml.etree.ElementTree as ET

if len(sys.argv) <= 1:
    print("No filename argument provided")
    exit(1)

try:
    tree = ET.parse(sys.argv[1])
    root = tree.getroot()
except FileNotFoundError:
    print("XML file not found at path")
    exit(2)
except ET.ParseError:
    print("XML file is malformed")
    exit(3)

ids = []

for child in root:
    ids.append(child.attrib.get('Id'))

if len(ids) > len(set(ids)):
    print("Duplicate rule ids found in file")
    exit(4)

print("No duplicate rule ids found in file")
exit(0)
