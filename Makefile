# Andrés Aguirre Dorelo
# MINA/INCO/UDELAR
#
# Makefile for Lucy
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

VREP_VERSION = V-REP_PRO_EDU_V3_2_1_64_Linux
VREP_URL = http://coppeliarobotics.com/$(VREP_VERSION).tar.gz

env: 
	wget $(VREP_URL)
	tar zxvf V-REP_PRO_EDU*
	ln -s $(VREP_VERSION)/programming/remoteApiBindings/python/python/vrep.py .
	ln -s $(VREP_VERSION)/V-REP_PRO_EDU_V3_2_1_64_Linux/programming/remoteApiBindings/python/python/vrepConst.py .
	ln -s $(VREP_VERSION)/V-REP_PRO_EDU_V3_2_1_64_Linux/programming/remoteApiBindings/lib/lib/64Bit/remoteApi.so .
	cd tests
	ln -s ../vrep.py .
	ln -s ../vrepConst.py .
	ln -s ../remoteApi.so .