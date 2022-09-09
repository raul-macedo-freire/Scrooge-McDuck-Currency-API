# NOTE: This code has been extracted from a comment in stack overflow. 
# This code is a workaround to read environment variables with ConfigParser
# FONT: https://stackoverflow.com/a/49529659/19544670

import configparser
import os

class EnvInterpolation(configparser.BasicInterpolation):
    """Interpolation which expands environment variables in values."""

    def before_get(self, parser, section, option, value, defaults):
        value = super().before_get(parser, section, option, value, defaults)
        return os.path.expandvars(value)