#!/usr/bin/env python3
import getopt
file_source = 'app-mipsel-01.list'
file_obj ='app-source.list'

def GetOrignal():
    app_list = []
    with open(file_source,'r') as f:
	    for eachline in f:
		    r_name = (eachline.strip('\n').split(' '))[1]
		    app_list.append(r_name)
    return app_list

def Check_Write():
	file_list = []
	applist = GetOrignal()
	with open(file_obj,'r') as f:
		for eachline in f:
		    appname = eachline.strip('\n')
		    file_list.append(appname)
	with open('result.txt','a') as f:
		f.write('apps which is not found:\n')
		for item in applist:
			if file_list.count(item) == 0:
				f.write('\n')
				f.write(item)
				f.write('\n')
if __name__ == '__main__':
	Check_Write()

