#!/usr/bin/env python3
# CAST limited compile command definition
# Author: Maxim Menshikov (maxim@menshikov.org)

class CompileCommand:
    """
    Compile command reading result
    """

    def __init__(self):
        """
        Construct compile command reading result without any entries
        """
        self.entries = list()
        self.folders = dict()

    def __init__(self, entries, folders):
        """
        Construct a new instance of compile command reading result with given
        entries and folders

        :param      entries:  Array of entry paths
        :type       entries:  list of str
        :param      folders:  Array of folder paths
        :type       folders:  dict of str
        """
        self.entries = entries
        self.folders = folders
