#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Andrés Aguirre Dorelo
# MINA/INCO/UDELAR
# 
# Lucy crossover function
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

import pyevolve.Util as Util
from random import randint as rand_randint, choice as rand_choice
import math


def diff(frame1, frame2):
   diff=0
   for position in range(len(frame1)):
      diff = diff + math.fabs(frame1[position]-frame2[position])
   return diff

def G2DListCrossoverSingleHPoint(genome, **args):
   """ The crossover of G2DList, Single Horizontal Point """
 
   sister = None
   brother = None
   gMom = args["mom"]
   gDad = args["dad"]

   cut = rand_randint(1, gMom.getHeight() - 1)

   if args["count"] >= 1:
      sister = gMom.clone()
      sister.resetStats()
      for i in xrange(cut, sister.getHeight()):
         sister[i][:] = gDad[i][:]

   if args["count"] == 2:
      brother = gDad.clone()
      brother.resetStats()
      for i in xrange(cut, brother.getHeight()):
         brother[i][:] = gMom[i][:]

   return (sister, brother)

def G2DListCrossoverSingleNearHPoint(genome, **args):
   """ The crossover of G2DList, Single Horizontal Point """
 
   sister = None
   brother = None
   gMom = args["mom"]
   gDad = args["dad"]
   minimalDiff = 1000000
   minimalDiffPosition = 0

   cut = rand_randint(1, gMom.getHeight() - 1)
   
   frame1 = gMom[cut]

   for position in xrange(gDad.getHeight()):
      frameDiff = diff(frame1, gDad[position])
      if frameDiff < minimalDiff and frameDiff>5: #avoid 
         minimalDiff = frameDiff
         minimalDiffPosition = position
   print "difference between poses: ", minimalDiff

   frame2 = gDad[minimalDiffPosition]

   sister = gMom.clone()
   brother = gDad.clone()
   if args["count"] >= 1:
      sister.resetStats()
      for i in xrange(minimalDiffPosition, brother.getHeight()):
         if cut+(i-minimalDiffPosition) < sister.getHeight():
            sister[cut+(i-minimalDiffPosition)][:] = gDad[i][:]

   if args["count"] == 2:
      brother.resetStats()
      for i in xrange(minimalDiffPosition, sister.getHeight()):
         if i < brother.getHeight() and cut+(i-minimalDiffPosition) < gMom.getHeight():
            brother[i][:] = gMom[cut+(i-minimalDiffPosition)][:]

   return (sister, brother)

def G2DListCrossoverSingleNearHPointImprove(genome, **args):
   """ The crossover of G2DList, Single Horizontal Point"""
   
   sister = None
   brother = None
   gMom = args["mom"]
   gDad = args["dad"]
   minimalDiff = 1000000
   minimalDiffPosition = 0

   cut = rand_randint(1, gMom.getHeight() - 1)
   
   frame1 = gMom[cut]

   for position in range(gDad.getHeight()):
      frameDiff = diff(frame1, gDad[position])
      #if frameDiff < minimalDiff and frameDiff>5: #avoid to choose a gene already injected gene
      if frameDiff < minimalDiff:
         minimalDiff = frameDiff
         minimalDiffPosition = position
         print minimalDiffPosition, minimalDiff, gDad.getHeight()
   print "difference between poses: ", minimalDiff, "crossover posititon:", crossover

   frame2 = gDad[minimalDiffPosition]

   sister = gMom.clone()
   brother = gDad.clone()
   if args["count"] >= 1:
      sister.resetStats()
   
      for i in xrange(minimalDiffPosition, brother.getHeight()):
         if cut+(i-minimalDiffPosition) < sister.getHeight():
            sister[cut+(i-minimalDiffPosition)][:] = gDad[i][:]

      lastGene = cut + (brother.getHeight()-1) - minimalDiffPosition
      if lastGene < sister.getHeight():
         frame1 = sister[lastGene]

      for position in range(gDad.getHeight()):
         frameDiff = diff(frame1, gDad[position])
         if frameDiff < minimalDiff and frameDiff>5: #avoid to choose a gene already injected gene
            minimalDiff = frameDiff
            minimalDiffPosition = position

         for i in xrange(lastGene, sister.getHeight()):
            if minimalDiffPosition+lastGene-i < gMom.getHeight():
               sister[i][:] = gMom[minimalDiffPosition+lastGene-i]

   if args["count"] == 2:
      brother.resetStats()
      for i in xrange(minimalDiffPosition, sister.getHeight()):
         if i < brother.getHeight() and cut+(i-minimalDiffPosition) < gMom.getHeight():
            brother[i][:] = gMom[cut+(i-minimalDiffPosition)][:]

      lastGene = cut + (sister.getHeight()-1) - minimalDiffPosition
      if lastGene < brother.getHeight():
         frame1 = brother[lastGene]

      for position in range(gMom.getHeight()):
         frameDiff = diff(frame1, gMom[position])
         if frameDiff < minimalDiff and frameDiff>5: #avoid to choose a gene already injected gene
            minimalDiff = frameDiff
            minimalDiffPosition = position

         for i in xrange(lastGene, brother.getHeight()):
            if minimalDiffPosition+lastGene-i < gDad.getHeight():
               brother[i][:] = gDad[minimalDiffPosition+lastGene-i]

   return (sister, brother)
