import requests
from utils import loadJson
from datetime import datetime
from urllib.request import urlopen
import json

# Function to convert hours from 12hr to 24hr format
def convert12to24(hour):
    if hour[-2:]=='AM' and hour[:2]=='12':
        return str(0)
    elif hour[-2:]=='AM':
        return hour[:-2]
    elif hour[-2:]=='PM' and hour[:2]=='12':
        return hour[:-2]
    else:
        if(len(hour)==3):
            return str(int(hour[:1])+12)
        elif(len(hour)==4):
            return str(int(hour[:2])+12)

# Function to find if hour exists in the range
def isInTimeRange(hour, start, end):
    if start < end:
        if hour > start and hour < end:
            return True
        else:
            return False
    if start > end:
        if hour > start:
            return True
        else:
            return False
            
# Sample Input
userInput = ["https://filtered-task-question-data.s3.us-east-2.amazonaws.com/redfin/foodtruck.json", "1602172800"]

# User Input to variables
url = userInput[0]
timestamp = int(userInput[1])

# Converting string to date
date = datetime.utcfromtimestamp(timestamp).strftime('%m/%d/%Y %H:%M:%S')
day = datetime.utcfromtimestamp(timestamp).strftime('%A')
hour = int(datetime.utcfromtimestamp(timestamp).strftime('%H'))
# print(date, day, hour)

# Importing json from url 
ptr = urlopen(url)
data = json.loads(ptr.read())
n = len(data)

# Variable to store the results
output = []

for i in range(n):
    if day == data[i]['DayOfWeekStr']:
        starttime = int(convert12to24(data[i]['starttime']))
        endtime = int(convert12to24(data[i]['endtime']))
        if isInTimeRange(hour, starttime, endtime):
            output.append(data[i]['Applicant'])

# Removing duplicate values in results
output = list(set(output))

# Sorting the results
output.sort()

# Printing the output
for i in range(len(output)):
    print(output[i])