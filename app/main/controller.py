#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
main.controller.py
~~~~~~~~~~~~~~~~~

Main routes for application.

:copyright: (c) 2015 by Cameron Dershem.
:license: see TOPMATTER
:source: github.com/cldershem/$SOME_REPO
"""
from flask import render_template
from . import main


@main.route('/')
def index():
    return render_template('index.html')
