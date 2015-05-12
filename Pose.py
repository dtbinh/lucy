#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Andrés Aguirre Dorelo
# MINA/INCO/UDELAR
# 
# Pose representation for calculus
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

import math
from simulator.LoadRobotConfiguration import LoadRobotConfiguration

#TODO find a better place for this chunk of code :P
jointNullValue ={}
jointNullValue["R_Ankle_Pitch"]=0
jointNullValue["R_Shoulder_Pitch"]=0
jointNullValue["L_Ankle_Pitch"]=0
jointNullValue["R_Hip_Pitch"]=0
jointNullValue["Hip_Pitch"]=0
jointNullValue["L_Knee angle"]=166.119092703
jointNullValue["L_Hip_Roll"]=0
jointNullValue["R_Ankle_Roll"]=0
jointNullValue["L_Ankle_Roll"]=0
jointNullValue["L_Shoulder_Pitch"]=0
jointNullValue["R_Hip_Yaw"]=0
jointNullValue["R_Hip_Roll"]=0
jointNullValue["R_Knee"]=166.534881592
jointNullValue["L_Hip_Yaw"]=0
jointNullValue["L_Elbow_Yaw"]=0
jointNullValue["R_Elbow_Yaw"]=0
jointNullValue["L_Shoulder_Yaw"]=0
jointNullValue["R_Shoulder_Yaw"]=0

class Pose:

    def __init__(self, poseValues={}):
        self.value = poseValues
        configuration = LoadRobotConfiguration()
        for joint in configuration.getJointsName():
            if joint not in self.value.keys():
                self.value[joint]=jointNullValue[joint]

    def setValue(self, key, value):
        self.value[key] = value

    def getValue(self, key):
        if key in self.value.keys():
            return self.value[key]
        else: #it can't happen
            return jointNullValue 

    def diff(self, pose):
        diff = 0
        for key in xrange(self.keys()):
            diff = diff + math.fabs(pose.getValue(key) - self.value[key])
        return diff


