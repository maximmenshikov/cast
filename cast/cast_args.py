#!/usr/bin/env python3
# CAST argument parser
# Author: Maxim Menshikov (maxim@menshikov.org)
import argparse
import os
import re


def file_path(p):
    """
    Verify that file exists or throw exception otherwise

    :param      p:    Target path
    :type       p:    str
    """
    if os.path.isfile(p):
        return p
    else:
        raise FileNotFoundError(p)


def prepare_parser():
    """
    Parse CAST arguments
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--compile-db",
                        help="Compilation database",
                        required=True,
                        type=file_path)
    parser.add_argument("-t", "--template",
                        help="CProj template",
                        required=True,
                        type=file_path)
    parser.add_argument("-o", "--output",
                        help="Output CProj project",
                        required=True)
    parser.add_argument("-w", "--workdir",
                        help="Working directory which should be truncated from compile db",
                        default=os.getcwd())
    return parser
