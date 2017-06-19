#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import gettext
import unittest
import json
from time import sleep
from lib import runTest
from subprocess import getstatusoutput as rt
from lib import window
import subprocess

class DFM_OpenFile(unittest.TestCase):
    caseid = '0000000'

    @classmethod
    def setUpClass(cls):
        def load():
            with open('test_menu.json', 'r') as json_file:
                data = json.load(json_file)
                return data

        ddata = load()

        cls.pwd = os.getcwd()
        cls.data = 'data'
        cls.fileName = ddata['OpenFile'][0]['fileName']
        cls.eventType = 'OpenFile'
        cls.testFilePath = 'file://' + '/'.join([cls.pwd, cls.data, cls.fileName])
        cls.windowName = ddata['OpenFile'][0]['windowName']

    @classmethod
    def tearDownClass(cls):
        pass

    def cmdline(self, argDict):
        args = json.dumps(argDict)
        return 'dde-file-manager -e \'' + args + '\''

    def testOpenFile_URL(self):
        args = {"eventType": self.eventType,
                "url": self.testFilePath,
                "mode": 2}
        cmdstring = self.cmdline(args)
        print(cmdstring)

        child1 = subprocess.Popen("dde-file-manager -d >/dev/null 2>&1", shell=True)
        sleep(2)

        (status, output) = rt(cmdstring)

        docwin = window.findWindow(self.windowName)
        self.assertTrue(None != docwin)

        window.closeWindow(docwin)

        docwinclose = window.findWindow(self.windowName, mode="nowait")
        self.assertTrue(None == docwinclose)

        print(child1.pid)
        child1.kill()
        os.system('killall dde-file-manager')

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DFM_OpenFile('testOpenFile_URL'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    runTest(DFM_OpenFile)

