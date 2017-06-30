import sys
try:
  from lxml import ET
  print("running with lxml.etree")
except ImportError:
  try:
    # Python 2.5
    import xml.etree.cElementTree as ET
    print("running with cElementTree on Python 2.5+")
  except ImportError:
    try:
      # Python 2.5
      import xml.etree.ElementTree as ET
      print("running with ElementTree on Python 2.5+")
    except ImportError:
      try:
        # normal cElementTree install
        import cElementTree as ET
        print("running with cElementTree")
      except ImportError:
        try:
          # normal ElementTree install
          import elementtree.ElementTree as ET
          print("running with ElementTree")
        except ImportError:
          print("Failed to import ElementTree from any known place")
gpstree = ET.parse('example/gps.tcx')
gpsroot = gpstree.getroot()

# print(gpsroot.attrib)

namespaces = {  'ns0':'http://www.garmin.com/xmlschemas/ActivityExtension/v2',
                'xsi':'http://www.w3.org/2001/XMLSchema-instance',
                'ns3':'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2',
                'schemaLocation':'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2 http://www.garmin.com/xmlschemas/TrainingCenterDatabasev2.xsd'}

# xmlns="http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2"
# xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
# xmlns:ns3="http://www.garmin.com/xmlschemas/ActivityExtension/v2"
# xsi:schemaLocation="http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2 http://www.garmin.com/xmlschemas/TrainingCenterDatabasev2.xsd"


# <?xml version="1.0"?>
# <foo xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" thing1="this" thing2="that">
#   ....
#   <somedata bar="1">
#     <moredata whatsit="42"></moredata>
#   </somedata>
#   ....
# </foo>


# default = "http://www.garmin.com/xmlschemas/ActivityExtension/v2"
# xsi = "http://www.w3.org/2001/XMLSchema-instance"
# ns3 = "http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2"
# ns = {"None": default, "xmlns:xsi": xsi, "xmlns:ns3": ns3}
#
# for attr, uri in ns.items():
#     ET.register_namespace(attr.split(":")[1], uri)
#
# TrainingCenterDatabase = etree.Element("TrainingCenterDatabase",
#     dict(xsi:schemaLocation="http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2 http://www.garmin.com/xmlschemas/TrainingCenterDatabasev2.xsd")


# print(ET.tostring(gpsroot))
print(gpsroot.keys())


# namespace = 'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2'

# for Activities in gpsroot.findall('tcx:Activities',namespaces):
for Activities in gpsroot.findall('{http://www.garmin.com/xmlschemas/ActivityExtension/v2}TrainingCenterDatabase'):
    # for Activity in Activities.findall('.'):
    print(ET.tostring(Activities))
#     Activity = Activities.find('Activity')
#     print(Activity)
