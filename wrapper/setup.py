# coding=utf-8
from distutils.core import setup, Extension

setup(name='judgercore',
      version='2.0',
      ext_modules=[Extension('judgercore', sources=['judgercore.c'], libraries=["dl"])])
