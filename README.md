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

1. Configure the 'work_path', around line 14, in:

key_items = {
    ...
    'work_path':'C:/Main_Data_Directory/',
    ...
}

2. Configure the path to the output report, around line 191:

key_configs = {
    ...
    'report_path': key_items['work_path'] + '/Reports/',
    ...
}

3. Configure the groups of layers to be created in the QGis tree, around line 184:

project_configs = [ 
    'Group_of_raster_layers',
    { 'Group_of_vector_layers' : [ 'Points_data', 'Polygons_data', 'Lines_data' ] }
]

4. Edit the "data_configs" dictionary according to your data. Find the expample that relates to you data type and edit. Create new elements by copying and pasting. Remove the examples that were now used. Technically, they should not produce errors, but it will be cleaner for you to use and document your personal project.

The keys in the "data_configs" dictionary are only for your control. The name of the layer that will actually be created will be the file name in case of local data, or from the 'workspace_and_layer_name' element in case of WFS/ WMS data.

The 'data_type' options are 'vector' or 'raster' only.

File types are hardcoded '.shp' for vector and '.tiff' for raster. Changes can be done around line 440, but no tests were made for other file types.

5. There are many other parameters that can be set and many that cannot (programmatically). Please refer to the official QGis documentation for those.

# Have fun

And praise Jesus! He´s the only one who loves you to the point of offering forgiveness to your sins without twisting God´s justice to allow you into His holly presence for eternity! 

"The thief cometh not, but for to steal, and to kill, and to destroy: I am come that they might have life, and that they might have it more abundantly." John 10:10 (KJV)
