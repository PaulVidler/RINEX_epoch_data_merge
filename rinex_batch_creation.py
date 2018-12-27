import os
import zipfile
import time
import subprocess

"""--------------------------------------------------------------------------------------
This script will take zipped RINEX data from the smartnet network or other GPS reciever and 
merge files from different epochs.

*** Must be used in conjunction with a valid TEQC executable ****

Put all RINEX ZIP files and teqc.exe files into the same folder and run this py file

Paul Vidler - 31/10/2018

--------------------------------------------------------------------------------------"""

#ask for input to name output files
batch_file_name = input("What would like to name the final files? eg: Moreton_181018 : ")

file_list = os.listdir()
cur_dir = os.getcwd()

#print(file_list)

#create list for zipped files
zipped_list = []

#add only zip files to zipped_list
for file in file_list:
    if file.endswith(".zip"):
        zipped_list.append(file)
        
for file in zipped_list:
    print("Unzipping: " + file)

#extract all zip files in zipped_list into the current directory
for i in zipped_list:
    unzip = zipfile.ZipFile(i)
    unzip.extractall(cur_dir)

file_list2 = os.listdir()

#short delay to ensure zipping is complete
time.sleep(2)

#create new lists for each kind of item extracted from ZIP
list_18g = []
list_18n = []
list_18o = []

for file in file_list2:
    if file.endswith(".18g"):
        list_18g.append(file)

for file in file_list2:
    if file.endswith(".18n"):
        list_18n.append(file)

for file in file_list2:
    if file.endswith(".18o"):
        list_18o.append(file)

"""print(list_18g)
print(list_18n)
print(list_18o)"""

#make batch file
"""Decided to make a batch file rather than run the commands straight into 
DOS so there is a record of exactly what was done """

line1 = "teqc {} > {}{}\n".format(' '.join(list_18g), batch_file_name,".18g")
line2 = "teqc {} > {}{}\n".format(' '.join(list_18n), batch_file_name,".18n")
line3 = "teqc {} > {}{}\n".format(' '.join(list_18o), batch_file_name,".18o")

print("Making batch file: {}".format(batch_file_name))

batch_file = open("merge_rinex.bat", "a+")
batch_file.write(line1)
batch_file.write(line2)
batch_file.write(line3)
batch_file.write("pause")

batch_file.close()

print("Running batch file........")

# then run the batch file

os.system("merge_rinex.bat")

print("Complete!")

#Open location on server where RINEX data is to be stored/backed up
subprocess.Popen(r'explorer /select,"H:\Raw_Nav_Data\GPS_Cards\Smartnet\"')





