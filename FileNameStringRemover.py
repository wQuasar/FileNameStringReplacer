# Python script to rename all the files in a folder by replacing a certain substring from the name.
# Using a straightforward approach for string search but, it does the job. 

import os

# Get the list of files in a dir and then rename it
def removeString(sub_string, replace_string):
	file_list = os.listdir(".")

	for file in file_list:
		if os.path.isfile(file):
			if file != "StringRemover.py":
				new_name = getNewName(file.split(), sub_string.split(), replace_string.split())

				# Replacing only if a valid name change
				if (new_name == ""):
					print ("Did you just try to remove the entirety of: " + file + " !!!")

				elif (new_name != file): 
					print (file + " -> " + new_name)
					os.rename(file, new_name)


# Method to do most of the grunt work. Get the new name of the file as a string after replacing the substring.
def getNewName(old_name, sub_string_list, replace_string_list):
	extension = old_name[len(old_name) -1][old_name[len(old_name) - 1].find("."):]
	old_name[len(old_name) - 1] = old_name[len(old_name) -1][:old_name[len(old_name) - 1].find(".")]

	# Traversing through the entire name. Using while loop because we're changing the list each [valid] time
	i = 0
	while (i < len(old_name) - len(sub_string_list) + 1):
		if (old_name[i] == sub_string_list[0]):
			# Vars to keep track of the indexes
			begin = i
			end = i

			# Found the name! Let's traverse further to find if it is present in its entirety
			for j in range(1, len(sub_string_list)):
				if old_name[i + j] != sub_string_list[j]:
					end = -1
					break
				else:
					end += 1

			# end == -1 indicates that the string was not present in its entirety
			if end != -1:
				old_name = old_name[:begin] + replace_string_list + old_name[end + 1:]


		i += 1

	# if the entire name is "", just return that (will not be renamed)
	if (old_name == [""]):
		return ""

	# Adding the exension to the last index
	old_name[len(old_name) - 1] = old_name[len(old_name) - 1] + extension

	# Finally joining the name and returning
	return " ".join(old_name)


# Main init method
def init():
	print ("** KEEP BACKUPS YOU PUNK! **\n")
	sub_string = input("Enter the substring to be removed from the file names in this folder: ")
	replace_string = input("Enter the string to be replaced it with (Just press ENTER if nothing): ")

	print ("----- BEGIN PROCESSING -----\n")

	if (sub_string != ""):
		removeString(sub_string, replace_string)
	else :
		print ("WTF! You entered nothing?!")

	print ("\n----- END PROCESSING ----- ")

# Self start
init()
