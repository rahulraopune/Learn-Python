import zipfile
import os

workspace = zipfile.ZipFile("workspace.zip","w",zipfile.ZIP_DEFLATED)
for file in os.listdir('.'):
	workspace.write(file)
	
workspace.close()
print ("Workspace Zipped")
