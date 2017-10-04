#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from abscplane import AbsComplexPlane

###
# Name: Evan A Walker, Tim Frenzel
# Student ID: 01932978 , 
# Email: walke208@mail.chapman.edu , frenz102@mail.chapman.edu
# Course: CS510 Fall 2017
# Assignment: Classwork 06
###

class ArrayComplexPlane(AbsComplexPlane):
    """ArrayComplexPlane that subclasses the abstract base class AbsComplexPlanes
    Args:
        xmin (float): plane's min real value
        xmax (float): plane's max real value
        xlen   (int): # pnts spanning [xmin, xmax]
        ymin (float): plane's min imag value
        ymax (float): plane's max imag value
        ylen   (int): # pnts spanning [ymin, ymax]

    Attributes:
        plane (): a meshgrid of two linspaces x, and y values. is the current state of the complex plane
        fs (list): holds all functions f that were applied to plane in a list data structure

    Functions:
        __init__(self,xmin,xmax,xlen,ymin,ymax,ylen)    :constructor, sets all args to given input, then constructs plane attribute using args
        __setPlane(self,xmin,xmax,xlen,ymin,ymax,ylen)  :private fxn that acts much like a second constructor, resets plane and args to given input
        printPlane(self)                                :prints plane
        refresh(self)                                   :resets plane to args values and sets fs = []. does this by calling __setPlane, then clearing the fs
        apply(self, f, addTofs)                         :applys function f to all pnts in plane, and adds f to fs iff addTofs = True
        zoom(self,xmin,xmax,xlen,ymin,ymax,ylen)        :resets plane size and reapplys all f in fs in order. does this using apply and __setPlane
    """

    def __init__(self,xmin,xmax,xlen,ymin,ymax,ylen):
        """this function is the constructor and implements all private vars to given input,
        implements self.plane(complex plane) using the given input
        Args:
            xmin (int): minimum x value in table
            xmax (int): maximum x value in table
            xlen (int): # x points
            ymin (int): minimum y value in table
            ymax (int): maximum y value in table
            ylen (int): # y points
        Return:
            Null: returns nothing
        """

        ##   Implementing private vars  ##
        self.xmin  = xmin
        self.xmax  = xmax
        self.xlen  = xlen
        self.ymin  = ymin
        self.ymax  = ymax
        self.ylen  = ylen
        self.fs = []   #stays list, DO NOT change to numpy array

        ##  Implementing private var self.plane using numpy  ##
        #self.plane = self.setPlane(xmin,xmax,xlen,ymin,ymax,ylen)
        x = np.linspace(self.xmin,self.xmax,self.xlen)
        y = np.linspace(self.ymin,self.ymax,self.ylen)
        xx, yy = np.meshgrid(x, y)
        self.plane = xx - yy*1j

        self.plane = pd.DataFrame(self.plane, index=-y*1j+0, columns=x)
        return

    def __setPlane(self,xmin,xmax,xlen,ymin,ymax,ylen):
        """this function sets private vars to given input,
        and uses given input to create and set self.plane
        Args:
            xmin (int): minimum x value in table
            xmax (int): maximum x value in table
            xlen (int): # x points
            ymin (int): minimum y value in table
            ymax (int): maximum y value in table
            ylen (int): # y points
        Return:
            Null: returns nothing
        """
        self.xmin  = xmin
        self.xmax  = xmax
        self.xlen  = xlen
        self.ymin  = ymin
        self.ymax  = ymax
        self.ylen  = ylen

        x = np.linspace(self.xmin,self.xmax,self.xlen)
        y = np.linspace(self.ymin,self.ymax,self.ylen)
        xx, yy = np.meshgrid(x, y)
        self.plane = xx - yy*1j

        self.plane = pd.DataFrame(self.plane, index=-y*1j+0, columns=x)

        return

    def printPlane(self):
        """this function prints complex plane in a legible fashion.
        Args:
            none
        Return:
            Null: returns nothing
        """
        print("########################################-Complex Plane-######################################## \n")
        print(self.plane , "\n")
        print("############################################################################################### \n")
        return

    def refresh(self):
        """this function resets self.plane to private stored variables that define the table
        and clears all functions applied by setting self.fs = []
        Args:
           none
        Return:
           Null: returns nothing
        """
        self.__setPlane(self.xmin,self.xmax,self.xlen,self.ymin,self.ymax,self.ylen)
        self.fs = []
        return

    def apply(self, f, addTofs):
        """this function adds given input f to self.fs, then
        applies f to all pnts in self.plane
        Args:
            addTofs (bool): if True, input f is appended to fs. if False, f not appended to fs
            f (fxn): complex function
        Return:
            Null: returns nothing
        """
        if addTofs == True:
            self.fs.append(f)
        self.plane = f(self.plane)
        return

    def zoom(self,xmin,xmax,xlen,ymin,ymax,ylen):
        """this function changes the table size using given input values,
        and re-applys all f in self.fs. this is achieved by calling setPlane and
        applyAllF, see also these fxns
        Args:
            xmin (int): minimum x value in table
            xmax (int): maximum x value in table
            xlen (int): # x points
            ymin (int): minimum y value in table
            ymax (int): maximum y value in table
            ylen (int): # y points
        Return:
            Null: returns nothing
        """
        self.__setPlane(xmin,xmax,xlen,ymin,ymax,ylen)
        for k in range(len(self.fs)):
            self.apply(self.fs[k],False)
        return

#












##
    #FOR TESTING ONLY, DELETE FOR FINAL SUBMISSION
##
myPlane = ArrayComplexPlane(-4,4,9,-4,4,9)
myPlane.printPlane()

def f(x):
    return x*x

myPlane.apply(f,True)
print("APPLY f() TO PLANE")
myPlane.printPlane()
myPlane.refresh()
print("REFRESHED PLANE")
myPlane.printPlane()
myPlane.zoom(-2,2,5,-2,2,5)
print("ZOOMED PLANE")
myPlane.printPlane()

##
    # NOTE: WE DO NOT NEED A MAIN BECAUSE WE ARE NOT ACCESSING FILE THROUGH COMMAND TERMINAL.
    #       SINCE WE ARE ONLY USING THE CODE IN THE JUPYTER NOTEBOOK
##



























