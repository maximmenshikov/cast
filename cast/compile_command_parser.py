#!/usr/bin/env python3
# CAST limited compile command parser
# Author: Maxim Menshikov (maxim@menshikov.org)
import os
import json
import sys
from pathlib import Path
from cast.compile_command import CompileCommand


def read_db(path, work_dir):
    """
    Read a compilation database and get set of files and folders

    :param      path:      The path
    :type       path:      { type_description }
    :param      work_dir:  The work dir
    :type       work_dir:  { type_description }

    :return:    CompileCommand object
    """
    with open(path, 'r') as file:
        data = file.read()

    entries = json.loads(data)
    folders = dict()
    files = list()
    work_dir_path = Path(work_dir)

    for entry in entries:
        file = entry["file"]

        file_path = Path(file)
        if work_dir_path in file_path.parents:
            file = os.path.relpath(file, work_dir)

        file = os.path.normpath(file)
        folder = os.path.dirname(file)

        # Convert slashes anyway because we target Windows
        file = file.replace("/", "\\")
        folder = folder.replace("/", "\\")

        files.append(file)
        folders[folder] = True

    return CompileCommand(files, folders)
