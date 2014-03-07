# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
# Initialize Qt resources from file resources.py
import resources
import fTools
import sys,os,imp
# Import the code for the dialog
from populationdialog import PopulationDialog
from loadCityDialog import Load_City_Dialog
from bufferbypercentagedialog import BufferByPercentageDialog
path = os.path.dirname(fTools.__file__)
ftu = imp.load_source('ftools_utils', os.path.join(path,'tools','ftools_utils.py'))

class Population:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # refernce to map canvas
        self.canvas = self.iface.mapCanvas()
        # out click tool will emit a QgsPoint on every click
        self.clickTool = QgsMapToolEmitPoint(self.canvas)
        #create our GUI dialog
        self.population_dlg = PopulationDialog()
        #flag to see if the files are loaded
        self.pathName = " "
        self.dataLoaded = False

        self.plugin_dir = os.path.dirname(__file__)
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'bufferbypercentage_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        self.buffer_by_percent_dlg = BufferByPercentageDialog()

        #tsdfasdddddddd
	 
    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/population/icon.png"), "PopulationCheck", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)
        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&some text that appears in the menu", self.action)
		# connect our custom function to a clickTool signal that the canvas was clicked
        QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.handleMouseDown)
        QObject.connect(self.population_dlg.ui.loadFile, SIGNAL("clicked()"), self.loadFiles)
        QObject.connect(self.population_dlg.ui.removeFile, SIGNAL("clicked()"), self.removeFiles)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("&some text that appears in the menu",self.action)
        self.iface.removeToolBarIcon(self.action)

    def handleMouseDown(self, point, button):
		
		# get the input distance
		distance = self.dlg.ui.lcdNumber.value()
		unit = ""
		km = self.dlg.ui.kmButton
		ml = self.dlg.ui.mileButton
		
		# checks which unit button gets check
		if km.isChecked():
			unit = km.text()
		else:
			unit = ml.text()
		
		#QMessageBox.information(self.iface.mainWindow(), "Values", distance + " " + unit)
	
    #load census files on map
    def loadFiles(self):
        
        if self.pathName == " ":
            self.pathName = QFileDialog.getExistingDirectory()

        #displays the loadfile dialog
        self.load_file_dlg = Load_City_Dialog()
        self.load_file_dlg.show()
        
        ui = self.load_file_dlg.ui
        result = self.load_file_dlg.exec_()

        

        #if ok is press on load city window
        if result == 1:

            location_name = str(ui.locationName.currentText())

            if location_name == "New York City":
                
                self.new_york_block = QgsVectorLayer(str(self.pathName)+"/at_tigeresri80915244/blk0036061.zip", "new_york_block", "ogr")
                self.new_york_polygon = QgsVectorLayer(str(self.pathName)+"/at_tigeresri65141495/lpy36061.zip", "new_york_polygon", "ogr")
                self.new_york_point = QgsVectorLayer(str(self.pathName)+"/at_tigeresri3640145951/lpt36061.zip", "new_york_point", "ogr")
                self.new_york_roads = QgsVectorLayer(str(self.pathName)+"/at_tigeresri6663135754/lkA36061.zip", "new_york_roads", "ogr")
                QgsMapLayerRegistry.instance().addMapLayer(self.new_york_block)
                QgsMapLayerRegistry.instance().addMapLayer(self.new_york_polygon)
                QgsMapLayerRegistry.instance().addMapLayer(self.new_york_roads)
                QgsMapLayerRegistry.instance().addMapLayer(self.new_york_point)

            elif location_name == "Brooklyn":

                self.brooklyn_block = QgsVectorLayer(str(self.pathName)+"/at_tigeresri80915244/blk0036047.zip", "brooklyn_block", "ogr")
                self.brooklyn_polygon = QgsVectorLayer(str(self.pathName)+"/at_tigeresri65141495/lpy36047.zip", "brooklyn_polygon", "ogr")
                self.brooklyn_point = QgsVectorLayer(str(self.pathName)+"/at_tigeresri3640145951/lpt36047.zip", "brooklyn_point", "ogr")
                self.brooklyn_roads = QgsVectorLayer(str(self.pathName)+"/at_tigeresri6663135754/lkA36047.zip", "brooklyn_roads", "ogr")

                QgsMapLayerRegistry.instance().addMapLayer(self.brooklyn_block)
                QgsMapLayerRegistry.instance().addMapLayer(self.brooklyn_polygon)
                QgsMapLayerRegistry.instance().addMapLayer(self.brooklyn_roads)
                QgsMapLayerRegistry.instance().addMapLayer(self.brooklyn_point)

            elif location_name == "Bronx":
                self.bronx_block = QgsVectorLayer(str(self.pathName)+"/at_tigeresri80915244/blk0036005.zip", "bronx_block", "ogr")
                self.bronx_polygon = QgsVectorLayer(str(self.pathName)+"/at_tigeresri65141495/lpy36005.zip", "bronx_polygon", "ogr")
                self.bronx_point = QgsVectorLayer(str(self.pathName)+"/at_tigeresri3640145951/lpt36005.zip", "bronx_point", "ogr")
                self.bronx_roads = QgsVectorLayer(str(self.pathName)+"/at_tigeresri6663135754/lkA36005.zip", "bronx_roads", "ogr")
                
                QgsMapLayerRegistry.instance().addMapLayer(self.bronx_block)
                QgsMapLayerRegistry.instance().addMapLayer(self.bronx_polygon)
                QgsMapLayerRegistry.instance().addMapLayer(self.bronx_roads)
                QgsMapLayerRegistry.instance().addMapLayer(self.bronx_point)

            elif location_name == "Queens":

                self.queens_block = QgsVectorLayer(str(self.pathName)+"/at_tigeresri80915244/blk0036081.zip", "queens_block", "ogr")
                self.queens_polygon = QgsVectorLayer(str(self.pathName)+"/at_tigeresri65141495/lpy36081.zip", "queens_polygon", "ogr")
                self.queens_point = QgsVectorLayer(str(self.pathName)+"/at_tigeresri3640145951/lpt36081.zip", "queens_point", "ogr")
                self.queens_roads = QgsVectorLayer(str(self.pathName)+"/at_tigeresri6663135754/lkA36081.zip", "queens_roads", "ogr")

                QgsMapLayerRegistry.instance().addMapLayer(self.queens_block)
                QgsMapLayerRegistry.instance().addMapLayer(self.queens_polygon)        
                QgsMapLayerRegistry.instance().addMapLayer(self.queens_roads)
                QgsMapLayerRegistry.instance().addMapLayer(self.queens_point)

            elif location_name == "Nassau County":

                self.nassau_block = QgsVectorLayer(str(self.pathName)+"/at_tigeresri80915244/blk0036059.zip", "nassau_block", "ogr")
                self.nassau_polygon = QgsVectorLayer(str(self.pathName)+"/at_tigeresri65141495/lpy36059.zip", "nassau_polygon", "ogr")
                self.nassau_point = QgsVectorLayer(str(self.pathName)+"/at_tigeresri3640145951/lpt36059.zip", "nassau_point", "ogr")
                self.nassau_roads = QgsVectorLayer(str(self.pathName)+"/at_tigeresri6663135754/lkA36059.zip", "nassau_roads", "ogr")
                
                QgsMapLayerRegistry.instance().addMapLayer(self.nassau_block)
                QgsMapLayerRegistry.instance().addMapLayer(self.nassau_polygon)
                QgsMapLayerRegistry.instance().addMapLayer(self.nassau_roads)
                QgsMapLayerRegistry.instance().addMapLayer(self.nassau_point)

            elif location_name == "Suffolk County": 

                self.suffolk_block = QgsVectorLayer(str(self.pathName)+"/at_tigeresri80915244/blk0036103.zip", "suffolk_block", "ogr")
                self.suffolk_polygon = QgsVectorLayer(str(self.pathName)+"/at_tigeresri65141495/lpy36103.zip", "suffolk_polygon", "ogr")
                self.suffolk_point = QgsVectorLayer(str(self.pathName)+"/at_tigeresri3640145951/lpt36005.zip", "suffolk_point", "ogr")
                self.suffolk_roads = QgsVectorLayer(str(self.pathName)+"/at_tigeresri6663135754/lkA36103.zip", "suffolk_roads", "ogr")

                QgsMapLayerRegistry.instance().addMapLayer(self.suffolk_block)
                QgsMapLayerRegistry.instance().addMapLayer(self.suffolk_polygon)
                QgsMapLayerRegistry.instance().addMapLayer(self.suffolk_roads)
                QgsMapLayerRegistry.instance().addMapLayer(self.suffolk_point)
            
            if not self.dataLoaded:
                #loads demographic data
                self.demoGraphicData = QgsVectorLayer(str(self.pathName)+"/tgr36000sf1blk.dbf", "Demographic Data", "ogr")
                QgsMapLayerRegistry.instance().addMapLayer(self.demoGraphicData)
                self.dataLoaded = True


            print location_name

        #get path name
        #self.pathName = QFileDialog.getExistingDirectory()

        #set the loaded flag to 1 which means the file are loaded

    #remove the census files on map
    def removeFiles(self):
        
        
        if self.loaded > 0:
            QgsMapLayerRegistry.instance().removeMapLayer(self.censusBlocks.id())
            QgsMapLayerRegistry.instance().removeMapLayer(self.landMarkPolygon.id())
            QgsMapLayerRegistry.instance().removeMapLayer(self.roads.id())
            QgsMapLayerRegistry.instance().removeMapLayer(self.landMarkPoints.id())
            QgsMapLayerRegistry.instance().removeMapLayer(self.demoGraphicData.id())
        
        else:
            msg = "No Files are loaded."
            QMessageBox.warning(self.dlg, "Error", msg)
        #reset the flag to 0 when files are remove
        self.loaded = 0
    
    #prompt user to choose a distance unit
    def validate_entries(self):
        msg = ''
        ui = self.population_dlg.ui
        if not (ui.kmButton.isChecked()) and not (ui.mileButton.isChecked()):
            msg = 'You required to choose a distance unit.'
            QMessageBox.warning(self.population_dlg,"Invalid information",msg)
        else:
            self.population_dlg.accept()
            self.buffer_by_percent_dlg.populateLayers()
            self.buffer_by_percent_dlg.show()
    
	# run method that performs all the real work
    def run(self):
		# See if OK was pressed
        QObject.connect(self.population_dlg.ui.buttonBox, SIGNAL("accepted()"), self.validate_entries)
        
         # show the dialog
        self.population_dlg.show()
		#ui = self.dlg.ui
        result = self.population_dlg.exec_()
        
        if result == 1:
            #pass
            #self.canvas.setMapTool(self.clickTool)
            msg = '\n'
            if self.population_dlg.ui.kmButton.isChecked():
                msg += 'Buffer Unit:   \tKilometer.'
            else:
                msg += 'Buffer Unit:   \tMile'
            #QMessageBox.information(self.population_dlg, 'USER INPUT', 'Buffer Range: \t'+str(int(self.population_dlg.ui.lcdNumber.value()))+msg,QMessageBox.Ok)
            

            #layer = self.censusBlocks

            '''
            provider = layer.dataProvider()
            layer.select(provider.attributeIndexes())

            for feature in layer.getFeatures():
                print feature
            '''
            #idx = layer.fieldNameIndex('STFID')
            
            #print feature.attributes()[idx]

            '''for feature in i:
              # retreive every feature with its geometry and attributes
                # fetch geometry
                geom = feature.geometry()
                print "Feature ID %d: " % feature.id()

                # show some information about the feature
                if geom.vectorType() == QGis.Point:
                  x = geom.asPoint()
                  print "Point: " + str(x)
                elif geom.vectorType() == QGis.Line:
                  x = geom.asPolyline()
                  print "Line: %d points" % len(x)
                elif geom.vectorType() == QGis.Polygon:
                  x = geom.asPolygon()
                  numPts = 0
                  for ring in x:
                    numPts += len(ring)
                  print "Polygon: %d rings with %d points" % (len(x), numPts)
                else:
                  print "Unknown"

                # fetch attributes
                attrs = feature.attributes()

                # attrs is a list. It contains all the attribute values of this feature
                print attrs

                #idx = layer.fieldNameIndex('name')
                #print feature.attributes()[idx]
            '''
        
