#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Andrés Aguirre Dorelo
# MINA/INCO/UDELAR
#
# Parser for system configuration file
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

from xml.dom import minidom
import os
confFile = os.getcwd()+"/configuration/SystemConf.xml"

#TODO move this to configuration folder?
class LoadSystemConfiguration:
    
    def __init__(self):
        self.directoryValueMapping = {}
        xmldoc = minidom.parse(confFile)
        itemlist = xmldoc.getElementsByTagName("Directory") 
        for i in itemlist:
            name = i.getElementsByTagName("Name")[0]
            id   = i.getElementsByTagName("Value")[0]
            #print "Name:" + name.childNodes[0].toxml() + " Id: " + id.childNodes[0].toxml()
            self.directoryValueMapping[(name.childNodes[0].toxml())] = id.childNodes[0].toxml()        
            
    def getDirectory(self, name):
        return(self.directoryValueMapping[name])
    
    
#conf = LoadSystemConfiguration()
#print conf.getDirectory("Transformed mocap Files")
