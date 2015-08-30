import os

for root,subFolders,files in os.walk("/"):
	for file in files:
     		file_path=str(os.path.join(root,file))
		print str(file_path)

            			

	for dir in subFolders:
	         print str(dir)
