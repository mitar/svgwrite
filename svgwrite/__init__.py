#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: package definition file
# Created: 08.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3
"""
A Python library to create SVG drawings.

a simple example::

    import svgwrite

    dwg = svgwrite.Drawing('test.svg', profile='tiny')
    dwg.add(dwg.line((0, 0), (10, 0), stroke=svgwrite.rgb(10, 10, 16, '%')))
    dwg.add(dwg.text('Test', insert=(0, 0.2))
    dwg.save()

SVG Version
-----------

Only two types of SVG drawings could be created:

* *SVG 1.2 Tiny Profile* for svgwrite.parameter.profile = ``'tiny'``
* *SVG 1.1 Full Profile* for svgwrite.parameter.profile = ``'full|basic'``

"""

from drawing import Drawing
from utils import rgb

class Unit(object):
    """ Add units to values.
    """
    def __init__(self, unit='cm'):
        """ Constructor

        :Parameters:
        - `unit`: specify the unit string
        """
        self._unit=unit

    def __rmul__(self, other):
        """ add unit-strint to 'other'. (e.g. 5*cm => '5cm') """
        return "%s%s" % (other, self._unit)

    def __call__(self, *args):
        """ add unit-strings to all arguments.
        :Parameters:
        - `*args` : list of values
        e.g.: cm(1,2,3) => '1cm,2cm,3cm'
        """
        return ','.join(["%s%s" % (arg, self._unit) for arg in args])

cm = Unit('cm')
mm = Unit('mm')
em = Unit('em')
ex = Unit('ex')
px = Unit('px')
inch = Unit('in')
pc = Unit('pc')
pt = Unit('pt')
percent = Unit('%')
deg = Unit('deg')
grad = Unit('grad')
rad = Unit('rad')
Hz = Unit('Hz')
kHz = Unit('kHz')