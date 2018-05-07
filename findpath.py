import os
def print_directory_content(spath):
	
	for schild in os.listdir(spath):
		schildpath = os.path.join(spath, schild)
		if os.path.isdir(schildpath):
			return print_directory_content(schildpath)
		else:
			print(schildpath)

print_directory_content("/home/")
