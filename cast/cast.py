#!/usr/bin/env python3
# CAST main class
# Author: Maxim Menshikov (maxim@menshikov.org)
import os
import sys
import json
from cast.compile_command_parser import read_db


class Cast:
    """
    Main Cast class
    """

    def __init__(self):
        self.compile_db = ""
        self.template = ""
        self.output = ""
        self.workdir = ""

    def __init__(self, compile_db, template, output, workdir):
        self.compile_db = compile_db
        self.template = template
        self.output = output
        self.workdir = workdir

    def validate(self):
        return os.path.isfile(self.compile_db) and \
            os.path.exists(self.template) and \
            os.path.exists(self.workdir) and \
            self.output != ""

    def translate(self):
        if self.validate() == False:
            return False

        data = read_db(self.compile_db, self.workdir)
        file_list = "".join(list(map(lambda file:
                                     "    <Compile Include=\"" + file + "\">\n" +
                                     "      <SubType>compile</SubType>\n" +
                                     "    </Compile>\n", data.entries)))
        folder_list = "".join(list(map(lambda folder:
                                       "    <Folder Include=\"" + folder + "\"/>\n",
                                       data.folders)))

        # Read template
        new_cproj = ""
        with open(self.template, 'r') as file:
            new_cproj = file.read()

        # Replace dummy comments with actual data
        new_cproj = new_cproj.replace("/*FileGroup*/", file_list) \
            .replace("/*FolderGroup*/", folder_list)

        # We could pretty print it, but Atmel Studio refuses most
        # kinds of pretty printing.

        # Write out xml
        with open(self.output, "w") as file:
            file.write(new_cproj)
