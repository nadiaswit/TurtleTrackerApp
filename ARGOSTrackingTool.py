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

#Create two new dictionary objects
date_dict = {}
coord_dict = {}
#as the loop iterates, we want to add new items to each dictionary

#Iterate through all lines in the line list
for lineString in line_list:
    if lineString[0] in ("#", "u"): continue
    #Split the string into a list of data types
    lineData = lineString.split()
    
    #once items are parsed/split into strings, want to save as new variables
    #Extract items in list into variables
    #Even though items look like numbers, they're actually strings
    #Better to keep nominal data as strings
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    #if obs_lc not in ("1", "2", "3"):
    #   continue
    obs_lat = lineData[6]
    obs_long = lineData[7]
    
    #Print location of Sara if lc is 1, 2, or 3
    #f prints entire line as string
    if obs_lc in ("1", "2", "3"):
        print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_long} on {obs_date}")
        date_dict[record_id] = obs_date
        coord_dict[record_id] = (obs_lat,obs_long)

