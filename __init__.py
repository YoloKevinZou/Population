# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Population
                                 A QGIS plugin
 popcheck
                             -------------------
        begin                : 2014-02-07
        copyright            : (C) 2014 by hello
        email                : hello@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load Population class from file Population
    from population import Population
    return Population(iface)
