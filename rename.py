# by ekelly
# 07/22/2020
#renames feature classes in geodatabeses using certain charecers of the  gdb name


import os
import arcpy
from arcpy import env

#path to folder where the geodatabases are saved
env.workspace = r'\\DATASERVER1\ScienceData$\ekelly\Documents\AGOL\Live_on_AC'

fclist = []
for dirpath, dirnames, filenames in arcpy.da.Walk(env.workspace,datatype="FeatureClass"):
    for filename in filenames:
        fclist.append(os.path.join(dirpath, filename))

dblist = []
# List all file geodatabases in the current workspace
for dirpath, dirnames, filenames in arcpy.da.Walk(env.workspace,datatype="FeatureDataset"):
    for dirname in dirnames:
        dblist.append(os.path.join(dirpath, dirname))

#print fclist
#print dblist #names end with .gdb


new_names = []
fc_names = []
gdb_name_index = 8
fc_name_index = 9


#loops throug the gdbs and adds first nine andd last four characters of the geodatabasename to the layers' name
for fc in fclist:
      gdb_name = os.path.splitext(fc.split(os.sep)[gdb_name_index])[0]
      fc_name = os.path.splitext(fc.split(os.sep)[fc_name_index])[0]
      fc_name1 = gdb_name + ".gdb" + "\\" + fc_name
      fc_names.append(fc_name1)
      updated_fc_name = gdb_name + ".gdb" + "\\" + gdb_name[:9] + "_" + fc_name + gdb_name[-4:]
      new_names.append(updated_fc_name)

#print new_names
#print fc_names


#renames features using the new names
env.workspace = r'\\DATASERVER1\ScienceData$\ekelly\Documents\AGOL\Live_on_AC'
for inFeature, outFeature in zip(fc_names, new_names):
   arcpy.Rename_management(inFeature, outFeature, "FeatureClass")


