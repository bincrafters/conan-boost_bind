#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostBindConan(base.BoostBaseConan):
    name = "boost_bind"
    url = "https://github.com/bincrafters/conan-boost_bind"
    lib_short_names = ["bind"]
    header_only_libs = ["bind"]
    b2_requires = [
        "boost_config",
        "boost_core",
    ]


