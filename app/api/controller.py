#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
api.controller.py
~~~~~~~~~~~~~~~~~

Controller for the api

:copyright: (c) 2015 by Cameron Dershem.
:license: see TOPMATTER
:source: github.com/cldershem/$SOME_REPO
"""
from flask import Blueprint


mod = Blueprint('api', __name__, url_prefix='/api/v1/')


@mod.route('/')
def api():
    return "API not yet implemented"
