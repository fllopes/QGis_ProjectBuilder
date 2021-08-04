# Automates the creation of the project structure
# Imports and styles the required necessary data
# @author Filipe Lopes, 04/08/2021

import os
from pathlib import Path
import datetime



key_items = {
    "timing": [],
    'work_path':'C:/Main_Data_Directory/',
    "script_version":  '1_1_0_prod' # Use "prod" for "production" and "dev" for "development"
}



data_configs = {

    'polygon_layer_1': {
        'load': True,
        'path': key_items['work_path'] + '/Polygon_data_1/',
        'layer_group': 'Polygons_data',             # Must be added in the 'project_configs' (here, mention only the subgroup, when is the case)
        'data_type': 'vector',
        'connection':'ogr',
        'appearence': {
            'min_scale': 0 ,
            'max_scale': 0,
            'style': {
                'color': '255,158,23,0',            # Fill color: R,G,B,Transparency
                'outline_color': '35,35,35,255',    # R,G,B,Transparency
                'outline_style': 'solid',
                'outline_width': '0.26',
                'outline_width_unit': 'MM',
                'style': 'solid'
            }
        }
    },

    'polygon_layer_2': {
        'load': True,
        'path': key_items['work_path'] + '/Polygon_data_2/',
        'layer_group': 'Polygons_data',             # Must be added in the 'project_configs' (here, mention only the subgroup, when is the case)
        'data_type': 'vector',
        'connection':'ogr',
        'appearence': {
            'min_scale': 0 ,
            'max_scale': 0,
            'style': {
                'color': '255,158,23,0',            # Fill color: R,G,B,Transparency
                'outline_color': '35,35,35,255',    # R,G,B,Transparency
                'outline_style': 'solid',
                'outline_width': '0.26',
                'outline_width_unit': 'MM',
                'style': 'solid'
            }
        }
    },

    'Points_layer_1': {
        'load': True,
        'path': key_items['work_path'] + '/Points_data_1/',
        'layer_group': 'Points_data',                 # Must be added in the 'project_configs' (here, mention only the subgroup, when is the case)
        'data_type': 'vector',
        'connection':'ogr',
        'appearence': {
            'min_scale': 5000.0 ,
            'max_scale': 0,
            'style': {
                'color': '119,13,225,255',            # Point fill color: R,G,B,Transparency
                'outline_color': '119,13,225,255',    # R,G,B,Transparency
                'outline_style': 'no',
                'outline_width': '0',
                'outline_width_unit': 'MM',
                'size': '1.6',                        # Point size
                'size_unit': 'MM'
            }
        }
    },

    'Points_data_with_Rules_based_visualization': {
        'load': True,
        'path': key_items['work_path'] + '/Points_data_2/',
        'layer_group': 'Points_data',                 # Must be added in the 'project_configs' (here, mention only the subgroup, when is the case)
        'data_type': 'vector',
        'connection':'ogr',
        'appearence': {
            'min_scale': 3000.0 ,
            'max_scale': 0,
            'rules': [
                {
                    'label': 'some_label_1',
                    'expression': '"some_field" is not NULL',
                    'fill_color': '#01abff'
                },
                {
                    'label': 'some_label_2',
                    'expression': '"some_field" is NULL',
                    'fill_color': '#faa105'
                }
            ]
        }
    },

    'Lines_data_layer': {
        'load': True,
        'path': key_items['work_path'] + '/Line_data/',
        'layer_group': 'Lines_data',                # Must be added in the 'project_configs' (here, mention only the subgroup, when is the case)
        'data_type': 'vector',
        'connection':'ogr',
        'appearence': {
            'min_scale': 150000.0 ,
            'max_scale': 0,
            'style': {
                'line_color': '125,139,143,255',    # R,G,B,Transparency
                'customdash': '5;2',                # Dashed line pattern: 5;2
                'line_style': 'solid',
                'line_width': '0.26',
                'line_width_unit': 'MM'
            }
        }
    },

    'WFS_Vector_Data': {
        'load': True,
        'path': 'http://.../geoserver/wfs',
        'layer_group': 'Polygons_data',
        'data_type': 'vector',
        'connection':'WFS',
        'workspace_and_layer_name':'some-workspace:some-vector-layer-on-server',
        'user':'pmsv-funcate',
        'psw':'123pmsv',
        'appearence': {
            'min_scale': 3000.0 ,
            'max_scale': 0,
            'rules': [
                {
                    'label': 'Fachada OK',
                    'expression': '"fachada" is not NULL',
                    'fill_color': '#01abff'
                },
                {
                    'label': 'Sem Fachada',
                    'expression': '"fachada" is NULL',
                    'fill_color': '#faa105'
                }
            ]
        }
    },

    'Several_local_raster_layers_style_1': {
        'load': True,
        'path': key_items['work_path'] + '/Local_raster_data/',
        'layer_group': 'Group_of_raster_layers',    # Must be added in the 'project_configs' (here, mention only the subgroup, when is the case)
        'data_type': 'raster',
        'connection':'',
        'appearence': {
            'min_scale': 1000.0 ,
            'max_scale': 350.0,
            'opacity': 0.7
        }
    },

    'WMS_Raster_Data': {
        'load': True,
        'path': 'http://.../geoserver/ows?version=1.3.0',
        'layer_group': 'Group_of_raster_layers',
        'data_type': 'raster',
        'connection':'WMS',
        'workspace_and_layer_name':'some-workspace:some-raster-layer-on-server',
        'crs':'EPSG:31983',
        'appearence': {
            'min_scale': 1000.0 ,
            'max_scale': 0,
            'opacity': 1.0
        }
    }
}



# List of groups. Groups with subgroups are in dictionaries.
project_configs = [ 
    'Group_of_raster_layers',
    { 'Group_of_vector_layers' : [ 'Points_data', 'Polygons_data', 'Lines_data' ] }
]



key_configs = {
    'report_on_screen': True,
    'report_to_file': True,
    'report_path': key_items['work_path'] + '/Reports/',
    'report_file_prefix': 'ProjectBuilder_Report',
    'file_postfix': str('_v' + key_items["script_version"] + '_' + datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + '.txt')
}



def main():

    path = path_check(key_configs['report_path'])
    if not path:
        print('ERROR: verify the existence of the informed path ("{}")'.format(key_configs['report_path']))
        return None

    time_log('Main_Process', 'start', '\n--------------------------------\nBeginning the main process: ', key_items["timing"], True)

    for group in project_configs:
        create_group(group, None)

    for data in data_configs:

        if data_configs[data]['load']:

            if data_configs[data]['connection'] not in {'WFS', 'WMS'}:

                path = path_check(data_configs[data]['path'])
                if not path:
                    print('FAILED to import the data "{}". Verify the existence of the informed path "{}". Continuing to load the remaining data.'.format(data, data_configs[data]['path']))
                    continue

                trigger(data_configs[data]['path'], data_configs[data]['layer_group'], data_configs[data]['data_type'], data_configs[data]['connection'], data_configs[data]['appearence'] )
            
            if data_configs[data]['connection'] in {'WFS', 'WMS'}:

                if not QgsProject.instance().mapLayersByName(data_configs[data]['workspace_and_layer_name']):

                    data_import(data_configs[data]['path'], data, data_configs[data]['layer_group'], data_configs[data]['data_type'], data_configs[data]['connection'], data_configs[data]['appearence'])
                
                else:
                    conditional_print('Layer "{}" already exsists in thi project.'.format(data_configs[data]['workspace_and_layer_name']), False, True)
    
    time_log('Main_Process', 'end', '\nEnding the main process: ', key_items["timing"], True)
    conditional_print(str(' Duração: ' + procedure_time('Main_Process')), True, True)



# conditional_print option
def conditional_print(something_to_print, screen_report, file_report):

    if key_configs['report_on_screen'] and screen_report:
        print(something_to_print)
    if key_configs['report_to_file'] and file_report:
        print(something_to_print, file=open(str(key_configs['report_path'] + key_configs['report_file_prefix'] + key_configs['file_postfix']), 'a'))



# Runs a verification on the path provided by the user
def path_check(path):

    if path:

        path = path.replace('\\','//')

        if path[len(path)-1] != '/':

            path += '/'

        if os.path.isdir(path):
            return True

        else:
            return False
    
    else:
        return False


# Time Log
def time_log(procedure, event, message, log_array, print_option):

    log = {
        'process': procedure,
        'event': event,
        'message': message,
        'log_time': datetime.datetime.now()
    }
    log_array.append(log)

    if print_option:
        conditional_print(str(message + str(log['log_time'])), True, True)



# Returns da total time the last processment done
def procedure_time(process):

    initial_time_Index = next((index for index, item in enumerate(key_items['timing']) if (item['process'] == process and item['event'] == 'start')), None)
    final_time_Index = next((index for index, item in enumerate(key_items['timing']) if (item['process'] == process and item['event'] == 'end')), None)

    procedure_time = key_items['timing'][final_time_Index]['log_time'] - key_items['timing'][initial_time_Index]['log_time']
    return str(procedure_time)



# imports VECTOR and RASTER data
def data_import(path, layer_name, layer_group, data_type, connection, appearence):

    if data_type == 'vector':

        if connection == 'WFS':          

            uri = QgsDataSourceUri()
            uri.setParam('service', connection)
            uri.setParam('version', '1.1.0')
            # uri.setParam('request', 'GetFeature')
            uri.setParam('typename', data_configs[layer_name]['workspace_and_layer_name'])
            # uri.setParam('srsName', 'EPSG:31983')
            uri.setUsername(data_configs[layer_name]['user'])
            uri.setPassword(data_configs[layer_name]['psw'])
            uri.setParam('url', path)

            layer = QgsVectorLayer(uri.uri(), data_configs[layer_name]['workspace_and_layer_name'], connection)

        else:

            layer = QgsVectorLayer(path, layer_name, connection)

    if data_type == 'raster':

        if connection == 'WMS':

            uri = QgsDataSourceUri()
            uri.setParam('layers', data_configs[layer_name]['workspace_and_layer_name'])
            uri.setParam("styles", '')
            uri.setParam('format', 'image/png')
            uri.setParam('crs', data_configs[layer_name]['crs'])
            uri.setParam('dpiMode', '7')
            uri.setParam('featureCount', '10')
            uri.setParam('contextualWMSLegend', '0')
            uri.setParam('url', path)

            layer = QgsRasterLayer(str(uri.encodedUri(), "utf-8"), data_configs[layer_name]['workspace_and_layer_name'], connection)
        
        else:

            layer = QgsRasterLayer(path, layer_name)

    if not layer.isValid():

        conditional_print('FALHA ao carregar o layer "{}".'.format(layer_name), True, True)

    else:

        set_appearence(layer, appearence, data_type )

        QgsProject.instance().addMapLayer(layer, False)

        layer_positioning(layer, layer_group)

        conditional_print('Layer "{}" importado com sucesso.'.format(layer_name), False, True)



# Sets the appearence of the layer
# @min_scale is the largest number  (ex.: 150000 as in 1:150000.0)
# @max_scale is the smallest number (ex.: 1000 as in 1:1000.0)
# Symbol type code in QGis (renderer.symbol().type()):
# QgsMarkerSymbol = 0   (used for points)
# QgsLineSymbol = 1     (used for lines)
# QgsFillSymbol = 2     (used for polygons)
# 
def set_appearence(layer, appearence, data_type ):

    layer.setScaleBasedVisibility( True )

    layer.setMinimumScale( appearence['min_scale'] )

    layer.setMaximumScale( appearence['max_scale'] )

    if data_type == 'raster':

        layer.renderer().setOpacity( appearence['opacity'] )

    if data_type == 'vector':

        renderer = layer.renderer()

        if renderer.symbol().type() == 0:

            if 'rules' in appearence:

                symbol = QgsSymbol.defaultSymbol( layer.geometryType() )
                renderer = QgsRuleBasedRenderer( symbol )

                # Gets the root rule
                root_rule = renderer.rootRule()

                for rule in appearence['rules']:

                    label = rule['label']
                    expression = rule['expression']
                    color = QColor( rule['fill_color'] )

                    # Clones the default rule
                    rule = root_rule.children()[0].clone()

                    # Sets the label, expression and color
                    rule.setLabel( label )
                    rule.setFilterExpression( expression )
                    rule.symbol().setColor( color )

                    # Appends the rule to the list of rules
                    root_rule.appendChild( rule )

                    # Applies the renderer
                    layer.setRenderer( renderer )

                # Deletes the default rule (empty)
                root_rule.removeChildAt(0)

                return None

            else:

                symbol = QgsMarkerSymbol.createSimple( appearence['style'] )
        
        if renderer.symbol().type() == 1:

            symbol = QgsLineSymbol.createSimple( appearence['style'] )

        if renderer.symbol().type() == 2:

            symbol = QgsFillSymbol.createSimple( appearence['style'] )

        layer.renderer().setSymbol(symbol)



# Lists the files in the source folder
def map_files(source, data_type):

    file_list = []

    files = (entry for entry in Path(source).iterdir() if entry.is_file())

    for file in files:

        if data_type == 'vector':

            if file.name[(len(file.name)-3):].upper() == 'SHP':

                file_list.append(file)
        
        if data_type == 'raster':

            if file.name[(len(file.name)-3):].upper() == 'TIF':

                file_list.append(file)
    
    return file_list



# Triggers the procedure according with the data type (vector or raster)
def trigger(source, layer_group, data_type, connection, appearence):

        file_list = map_files(source, data_type)

        if file_list:

            for file in file_list:

                layer_name = file.name[:(len(file.name)-4)]

                if not QgsProject.instance().mapLayersByName(layer_name):

                    data_import(str(file), layer_name, layer_group, data_type, connection, appearence)

                else:
                    conditional_print('Layer "{}" already exsists in thi project.'.format(layer_name), False, True)

        else:
            conditional_print('No file with type "{}" was found in the directory:\n"{}"'.format(data_type, source), True, True)
            pass



# Places the layer into the right group & position
def layer_positioning( layer, layer_group ):

    root = QgsProject.instance().layerTreeRoot()

    group = root.findGroup( layer_group )

    if group:

        group.insertChildNode(-1, QgsLayerTreeLayer( layer ))

        root.findLayer( layer.id() ).setItemVisibilityChecked( False )
    
    else:
        conditional_print('The group "{}" does not exist in this project. Check the name informed in "project_configs". For now, the layer will be inserted into the root.'.format(layer_group, layer.name()), True, True)

        root.addLayer( layer )

        root.findLayer( layer.id() ).setItemVisibilityChecked( False )

        conditional_print('The layer "{}" was successfuly inserted into the root.'.format( layer.name() ), True, True)     



# Creates the project structure
# @nest_root must be None for non-nested groups
def create_group( group, nest_root ):

    root = QgsProject.instance().layerTreeRoot()

    # Case of nested groups
    if type(group) is dict:

        nest_root_group_name = list(group.keys())[0]

        # Checks if group already exists
        if not root.findGroup( nest_root_group_name ):

            new_group = QgsLayerTreeGroup( nest_root_group_name )

            # Creates new group in the root group to hold the subgroups afterwards
            root.addChildNode(new_group)

            conditional_print('Group "{}" criated with success.'.format( nest_root_group_name ), False, True)

        else:

                conditional_print('Group "{}" already exists in thi project.'.format( nest_root_group_name ), False, True)
                pass

        for subgroup in group[ list(group.keys())[0] ]:

            create_group( subgroup, nest_root_group_name )

    # Case of non-nested groups
    else:

        if nest_root:

            relative_root = root.findGroup( nest_root )

            # Checks if group already exists
            if not relative_root.findGroup( group ):

                new_group = QgsLayerTreeGroup( group )

                # Creates subgroup in the relative root group
                relative_root.addChildNode(new_group)

                conditional_print('Group "{}" criated with success.'.format( group ), False, True)

            else:

                conditional_print('Group "{}" already exists in thi project.'.format( group ), False, True)
                pass

        else:

            # Checks if group already exists
            if not root.findGroup( group ):

                new_group = QgsLayerTreeGroup( group )

                # Creates new group in the root group
                root.addChildNode(new_group)

                conditional_print('Group "{}" criated with success.'.format( group ), False, True)
            
            else:

                conditional_print('Group "{}" already exists in thi project.'.format( group ), False, True)
                pass



main()





# 'For of him, and through him, and to him, are all things: to whom be glory for ever. Amen.' Romans 11.36
