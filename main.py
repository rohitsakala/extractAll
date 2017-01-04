'''
	Python code to run moss on IIIT Hyderabad Assignments
'''

'''
	Loading necessay modules
'''
import zipfile
import tarfile
import gzip
import os
import sys
import subprocess

'''
	Main function to stages
'''
def main(assgnFile):
	extractMain(assgnFile)
	renameFiles()
	extractIndividual()
	cleanUp()

'''
	Function to extract the main file
'''
def extractMain(assgnFile):
	os.system('mkdir extracted')
	with zipfile.ZipFile(assgnFile, "r") as z:
    		z.extractall('./extracted/')

'''
	Rename files without spaces
'''
def renameFiles():
	os.system('rename "s/ /_/g" ./extracted/*')

'''
	Function to extract individual files
'''
def extractIndividual():
	os.system("mkdir ./individual")
	for i in os.listdir('./extracted/'):
		if i.endswith(".zip"):
			fileName = os.path.splitext(i)[0]
			try:
				with zipfile.ZipFile("./extracted/"+i, "r") as z:
    					z.extractall('./individual/'+fileName+'/')	
			except Exception, e:
				print "Assignment that failed to be extracted:  " + i
		elif i.endswith(".tar.gz"):
			try:
				fileName = os.path.splitext(i)[0]
				fileName = os.path.splitext(fileName)[0]
				tar = tarfile.open("./extracted/"+i, "r")
    				tar.extractall('./individual/'+fileName+'/')
    				tar.close()
    			except:
    				print "Assignment that failed to be extracted:  " + i
    		elif i.endswith(".gz"):
			try:
				fileName = os.path.splitext(i)[0]
				fileName = os.path.splitext(fileName)[0]
				tar = tarfile.open("./extracted/"+i, "r")
    				tar.extractall('./individual/'+fileName+'/')
    				tar.close()
    			except:
    				print "Assignment that failed to be extracted:  " + i
    		else:
    			print "Assignment Name failed to be extracted:  " + i


'''
	Function to remove directories/filess unnecessary
'''
def cleanUp():
	os.system("rm -r extracted")

if __name__ == '__main__':
	main(sys.argv[1])
