#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
config.py
~~~~~~~~~~~~~~~~~

Config for application.

:copyright: (c) 2015 by Cameron Dershem.
:license: see TOPMATTER
:source: github.com/cldershem/$SOME_REPO
"""
import secrets
import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    CSRF_ENABLED = True
    SECRET_KEY = secrets.SECRET_KEY

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    Testing = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


config = {
    'development': DevelopmentConfig,
    'test': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
    }
