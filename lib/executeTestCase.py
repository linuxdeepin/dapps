#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
from unittest import TextTestRunner, TextTestResult

resultfile = 'result.txt'

class HandleTestResult(TextTestResult):
    def startTestRun(self):
        self.startTime=time.time()

    def startTest(self, test):
        super(HandleTestResult, self).startTest(test)
        self.test = test

    def stopTestRun(self):
        re = len(self.failures) == 0 and len(self.errors) == 0
        caseid = type(self.test).caseid
        seconds = "%.3f" % (time.time() - self.startTime)
        minutes = convertToMinutes(float(seconds))
        commitresult(caseid, re, minutes)

def runTest(testcase):
    TextTestRunner(resultclass=HandleTestResult).run(testcase.suite())

def convertToMinutes(secs):
    left,right = divmod(secs, 60)
    pointright = right/60
    munites = '%.2f' % (left+pointright)
    return munites

def commitresult(id, result, time):
    if os.path.exists(resultfile):
        with open(resultfile, 'a') as f:
            idstr = " ".join((str(id), str(result), str(time)))
            f.write(idstr + os.linesep)
            f.close()
    else:
        with open(resultfile, 'w') as f:
            idstr = " ".join((str(id), str(result), str(time)))
            f.write(idstr + os.linesep)
            f.close()
