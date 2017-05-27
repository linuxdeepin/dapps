#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
import time
from time import sleep
gi.require_version('Wnck', '3.0')
from gi.repository import Wnck

screen = Wnck.Screen.get_default()
screen.force_update()

print("\n****************************************")
print("【windows_name】:")
for win in screen.get_windows():
    print(win.get_name())

print("\n****************************************")

print("【applications_name】:")
for win in screen.get_windows():
	print(win.get_application().get_name())