# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from populationdialog import PopulationDialog

class Population:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # refernce to map canvas
        self.canvas = self.iface.mapCanvas()
        # out click tool will emit a QgsPoint on every click
        self.clickTool = QgsMapToolEmitPoint(self.canvas)
        #create our GUI dialog
        self.dlg = PopulationDialog()
        #flag to see if the files are loaded
        self.loaded = 0
	 
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
        QObject.connect(self.dlg.ui.loadFile, SIGNAL("clicked()"), self.loadFiles)
        QObject.connect(self.dlg.ui.removeFile, SIGNAL("clicked()"), self.removeFiles)

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
		
		QMessageBox.information(self.iface.mainWindow(), "Values", distance + " " + unit)
	
    #load census files on map
    def loadFiles(self):
        
        #set the loaded flag to 1 which means the file are loaded
        self.loaded = 1;
        #load the shape files into vector later
        self.roads = QgsVectorLayer("C:/Users/Kevin/Desktop/Denver/lkA08031.zip", "roads", "ogr")
        self.landMarkPolygon = QgsVectorLayer("C:/Users/Kevin/Desktop/Denver/lpy08031.zip", "LandMark Polygons", "ogr")
        self.landMarkPoints = QgsVectorLayer("C:/Users/Kevin/Desktop/Denver/lpt08031.zip", "LandMark Points", "ogr")
        self.censusBlocks = QgsVectorLayer("C:/Users/Kevin/Desktop/Denver/grp0008031.zip", "Census Blocks", "ogr")
        self.demoGraphicData = QgsVectorLayer("C:/Users/Kevin/Desktop/Denver/tgr08000sf1grp.dbf", "Demographic Data", "ogr")
        
        #add the shape file onto map layer
        QgsMapLayerRegistry.instance().addMapLayer(self.censusBlocks)
        QgsMapLayerRegistry.instance().addMapLayer(self.landMarkPolygon)
        QgsMapLayerRegistry.instance().addMapLayer(self.roads)
        QgsMapLayerRegistry.instance().addMapLayer(self.landMarkPoints)
        QgsMapLayerRegistry.instance().addMapLayer(self.demoGraphicData)
     
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
        ui = self.dlg.ui
        if ui.kmButton.isChecked()==False and ui.mileButton.isChecked()==False:
            msg = 'You required to choose a distance unit.'
            QMessageBox.warning(self.dlg,"Invalid information",msg)
        else:
            self.dlg.accept()
    
	# run method that performs all the real work
    def run(self):
		# See if OK was pressed
        QObject.connect(self.dlg.ui.buttonBox, SIGNAL("accepted()"), self.validate_entries)
        
         # show the dialog
        self.dlg.show()
		#ui = self.dlg.ui
        result = self.dlg.exec_()
        
        if result == 1:
            #pass
            #self.canvas.setMapTool(self.clickTool)
            msg = '\n'
            if self.dlg.ui.kmButton.isChecked()==True:
                msg += 'Buffer Unit:   \tKilometer.'
            else:
                msg += 'Buffer Unit:   \tMile'
            QMessageBox.information( self.dlg, 'USER INPUT', 'Buffer Range: \t'+str(int(self.dlg.ui.lcdNumber.value()))+msg,QMessageBox.Ok)
    
        
