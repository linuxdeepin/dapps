#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gettext
import unittest
from lib.executeTestCase import runTest

from dde_file_manager import DFM_OpenFile
from dde_file_manager import DFM_OpenFileByApp
from dde_file_manager import DFM_CompressFiles
from dde_file_manager import DFM_DecompressFile
from dde_file_manager import DFM_DecompressFileHere

from dde_file_manager import DFM_RenameFile
from dde_file_manager import DFM_DeleteFiles
from dde_file_manager import DFM_MoveToTrash
from dde_file_manager import DFM_RestoreFromTrash
from dde_file_manager import DFM_PasteFile

from dde_file_manager import DFM_NewFolder
from dde_file_manager import DFM_NewFile
from dde_file_manager import DFM_OpenFileLocation
from dde_file_manager import DFM_CreateSymlink
from dde_file_manager import DFM_FileShare

from dde_file_manager import DFM_OpenInTerminal
from dde_file_manager import DFM_OpenNewWindow


def main():
    classes = []
    classes.append(DFM_OpenFile)
    classes.append(DFM_OpenFileByApp)
    classes.append(DFM_CompressFiles)
    classes.append(DFM_DecompressFile)
    classes.append(DFM_DecompressFileHere)

    classes.append(DFM_RenameFile)
    classes.append(DFM_DeleteFiles)
    classes.append(DFM_MoveToTrash)
    classes.append(DFM_RestoreFromTrash)
    classes.append(DFM_PasteFile)

    classes.append(DFM_NewFolder)
    classes.append(DFM_NewFile)
    classes.append(DFM_OpenFileLocation)
    classes.append(DFM_CreateSymlink)
    classes.append(DFM_FileShare)

    classes.append(DFM_OpenInTerminal)
    classes.append(DFM_OpenNewWindow)

    for c in classes:
        runTest(c)

if __name__ == "__main__":
    unittest.installHandler()
    main()
