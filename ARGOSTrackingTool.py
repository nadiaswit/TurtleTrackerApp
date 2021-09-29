#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Nadia Swit (nadia.swit@duje,edu)
# Date:   Fall 2021
#--------------------------------------------------------------
#creating two dictionaries: one having date values and one with coordinates
#date dictionary: key = uid, value =  date (value can be same, key diff)
#coordinate dictionary: key = tag_id, value = lat/long coordinate pair
#need a string method to pull out specific characters
#treat as a delineated file

#Create a variable pointing to the data file
file_name = './Data/Raw/Sara.txt'

#Create a file object from the file
file_object = open(file_name, 'r')

#Read entire contents of data file and put into a list
line_list = file_object.readlines()

#Close the file
file_object.close()


#Pretend we read one line of data from the file
lineString = line_list[100]

#Split the string into a list of data types
lineData = lineString.split()

#once items are parsed/split into strings, want to save as new variables
#Extract items in list into variables
record_id = lineData[0]
obs_date = lineData[2]
obs_lc = lineData[4]
obs_lat = lineData[6]
obs_long = lineData[7]

#Print location of Sara
#f prints entire line as string
print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_long} on {obs_date}")

