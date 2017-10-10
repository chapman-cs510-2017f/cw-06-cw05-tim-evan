#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cplane_np as cp
from pandas.util.testing import assert_frame_equal
import numpy as np
import pandas as pd


###
# Name: Evan A Walker, Tim Frenzel
# Student ID: 01932978 , 
# Email: walke208@mail.chapman.edu , frenz102@mail.chapman.edu
# Course: CS510 Fall 2017
# Assignment: Classwork 06
###

#evaluate each methods in the class of cplane_np
dfInput = [[0,2],[3j,2+3j]]
dfInput2 = [[3+1j,4+1j],[3+2j,4+2j]]

def f(z):
    return z+2

def test_cplane():
    myPlane = cp.ArrayComplexPlane(0,2,2,0,3,2)
    test1 = pd.DataFrame(dfInput,index=['y1*i', 'y2*i'], columns=['x1','x2'])
    assert_frame_equal(myPlane.plane, test1)
    
def test_apply():
    myPlane = cp.ArrayComplexPlane(0,2,2,0,3,2)
    test2 = pd.DataFrame(dfInput,index=['y1*i', 'y2*i'], columns=['x1','x2'])
    assert_frame_equal(myPlane.plane, test2, check_dtype=False)

def test_zoom():
    myPlane = cp.ArrayComplexPlane(0,2,2,0,3,2)
    myPlane.apply(f)
    myPlane.zoom(1,2,2,1,2,2)
    test4 = pd.DataFrame(dfInput2,index=['y1*i', 'y2*i'], columns=['x1','x2'])
    assert_frame_equal(myPlane.plane, test4)

def test_refresh():
    myPlane = cp.ArrayComplexPlane(0,2,2,0,3,2)
    myPlane.apply(f)
    myPlane.refresh()
    test5 = pd.DataFrame([[0,2],[3j,2+3j]],index=['y1*i', 'y2*i'], columns=['x1','x2'])
    assert_frame_equal(myPlane.plane, test5)
