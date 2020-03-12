import requests
import json
import numpy
import FRCTeam
# Scores is an array, Average should be 0, matches will be an array.
TeamNumber = int(input("What team's data do you want?"))


request = requests.get("https://www.thebluealliance.com/api/v3/team/" + TeamNumber)

RequestResponse = json.loads(request.text)

Data = {
'Matches They Will Be In' : [],
'Scores': []
}

for e in RequestResponse:
    Data['Matches They Will Be In'].append(e[match_number])
    

request = requests.get()

RequestResponse = json.loads(request.text)

for x in RequestResponse:
    Data['scores'] = Data['scores'].append(x[score])

total = 0
for y in Data['scores']:
    total += Data['scores'[y]]
    average = total/len(Data['scores'])