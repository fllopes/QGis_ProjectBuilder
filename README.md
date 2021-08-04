# QGis_ProjectBuilder
This script automates the creation of a project in QGis, importing data and setting up the visuals. This includes options such as transparency, colors, outlines and rules based visualization and scale dependent visualisation.


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
