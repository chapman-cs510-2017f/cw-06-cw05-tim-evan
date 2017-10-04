#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from abscplane import AbsComplexPlane

###
# Name: Evan A Walker, Tim Frenzel
# Student ID: 01932978 , 
# Email: walke208@mail.chapman.edu , frenz102@mail.chapman.edu
# Course: CS510 Fall 2017
# Assignment: Classwork 06
###
from abscplane import AbsComplexPlane

class ArrayComplexPlane(AbsComplexPlane):
    def __init__(self,xmin,xmax,xlen,ymin,ymax,ylen):
        """this function is the constructor and implements all private vars to given input,
        implements self.plane(complex plane) using the given input
        Args:
            self (key word): to refrence private vars
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
        x = np.linspace(self.xmin,self.xmax,self.xlen)
        y = np.linspace(self.ymin,self.ymax,self.ylen)
        x, y = np.meshgrid(x, y)
        self.plane = x - y*1j

        return

    def printTable(self):
        """this function prints complex plane in a legible fashion.
        Args:
            self (key word): to refrence private vars
        Return:
            Null: returns nothing
        """
        print("##########################-Complex Plane-##############################")
        print(self.plane)
        print("#######################################################################")
        return

    def refresh(self):
        """this function resets self.plane to private stored variables that define the table
        and clears all functions applied by setting self.fs = []
        Args:
           self (key word): to refrence private vars
        Return:
           Null: returns nothing
        """

        x = np.linspace(self.xmin,self.xmax,self.xlen)
        y = np.linspace(self.ymin,self.ymax,self.ylen)
        x, y = np.meshgrid(x, y)
        self.plane = x - y*1j

        self.fs = []
        return

    def apply(self, f):
        """this function adds given input f to self.fs, then
        applies f to all pnts in self.plane
        Args:
            self (key word): to refrence private vars
            f (fxn): complex function
        Return:
            Null: returns nothing
        """
        self.fs.append(f)
        self.plane = f(self.plane)
        return

    def applyAllf(self):
        """applies all of the transformations in fs, in order, to the plane
        without adding functions to fs. This changes self.plane
        Args:
            self (key word): to refrence private vars
        Return:
            Null: returns nothing
        """
        for k in range(len(self.fs)):
            f = self.fs[k]
            self.plane = f(self.plane)
        return

    def setPlane(self,xmin,xmax,xlen,ymin,ymax,ylen):
        """this function sets private vars to given input,
        and uses given input to create and set self.plane
        Args:
            self (key word): to refrence private vars
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
        x, y = np.meshgrid(x, y)
        self.plane = x - y*1j
        return

    def zoom(self,xmin,xmax,xlen,ymin,ymax,ylen):
        """this function changes the table size using given input values,
        and re-applys all f in self.fs. this is achieved by calling setPlane and
        applyAllF, see also these fxns
        Args:
            self (key word): to refrence private vars
            xmin (int): minimum x value in table
            xmax (int): maximum x value in table
            xlen (int): # x points
            ymin (int): minimum y value in table
            ymax (int): maximum y value in table
            ylen (int): # y points
        Return:
            Null: returns nothing
        """
        self.setPlane(xmin,xmax,xlen,ymin,ymax,ylen)
        self.applyAllf()
        return

##
    #FOR TESTING ONLY, DELETE FOR FINAL SUBMISSION
##
myPlane = ArrayComplexPlane(-4,4,9,-4,4,9)
myPlane.printTable()

def f(x):
    return x*x

myPlane.apply(f)
myPlane.printTable()
myPlane.refresh()
myPlane.printTable()
myPlane.zoom(-2,2,5,-2,2,5)
myPlane.printTable()


##
    # NOTE: WE DO NOT NEED A MAIN BECAUSE WE ARE NOT ACCESSING FILE THROUGH COMMAND TERMINAL.
    #       SINCE WE ARE ONLY USING THE CODE IN THE JUPYTER NOTEBOOK
##



























