# QGis_ProjectBuilder
This script automates the creation of a project in QGis, importing data and setting up the visuals. This includes options such as transparency, colors, outlines and rules based visualization and scale dependent visualisation.

Imports shapefiles and raster files, both locally or remotely via WFS or WMS.


# Exploring Your Data

I suggest the following code snippets to explore your data and help understanding the options you need to configure in the script.

layer = iface.activeLayer()
print("Layer name:", layer.name())

For dealing with VECTOR LAYERS:

renderer = layer.renderer()
print("Renenerer:", renderer)
print("Type:", renderer.type())
print("Renderer dump:", renderer.dump())
print("Symbol:", renderer.symbol())
print("Symbol:", renderer.symbol().type())
print("Properties:", renderer.symbol().symbolLayers()[0].properties())


For dealing with RASTER LAYERS:

#print(layer.name())
#print(layer.renderer().type())

# Basic Usage on Quick Steps

The scritp assumes that all you data (the local data) is nested under a single directory, called 'work_path'. However, you can change this for every data, except for the report that comes as an output.

1. Configure the 'work_path' located around line 14, in:

key_items = {
    ...
    'work_path':'E:/Data_Main_Directory/',
    ...
}

2. Configure the path to the output report located around line 283:

key_configs = {
    ...
    'report_path': key_items['work_path'] + '/Relatorios_Scripts/',
    ...
}

3. Configure the groups of layers to be created in QGis:

