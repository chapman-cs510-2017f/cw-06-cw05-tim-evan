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
dfInput = [[(-1-1j),-1j,(1-1j)],[(-1+1j),1j,(1+1j)]]
dfInputApply = [[2j,-1,-2j],[-2j,-1,2j]]
dfInputZoom = [[2j,(3+4j)],[(-3+4j),8j]]

def f(z):
    return z*z

def test_cplane():
    myPlane = cp.ArrayComplexPlane(-1,1,3,-1,1,2)
    test1 = pd.DataFrame(dfInput,index=['y1*i', 'y2*i'], columns=['x1','x2'])
    assert_frame_equal(myPlane.getPlane(), test1)

def test_apply():
    myPlane = cp.ArrayComplexPlane(-1,1,3,-1,1,2)
    myPlane.apply(f)
    test2 = pd.DataFrame(dfInputApply,index=['y1*i', 'y2*i'], columns=['x1','x2'])
    assert_frame_equal(myPlane.getPlane(), test2, check_dtype=False)

def test_zoom():
    myPlane = cp.ArrayComplexPlane(-1,1,3,-1,1,2)
    myPlane.apply(f)
    myPlane.zoom(1,2,2,1,2,2)
    test4 = pd.DataFrame(dfInputZoom,index=['y1*i', 'y2*i'], columns=['x1','x2'])
    assert_frame_equal(myPlane.getPlane(), test4)

def test_refresh():
    myPlane = cp.ArrayComplexPlane(-1,1,3,-1,1,2)
    myPlane.apply(f)
    myPlane.refresh()
    test5 = pd.DataFrame(dfInput,index=['y1*i', 'y2*i'], columns=['x1','x2'])
    assert_frame_equal(myPlane.getPlane(), test5)

