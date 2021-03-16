#!/wsr/bin/python

import csv, json

csvFilePath = "Cust_Purch_Data.csv"
jsonFilePath = "info.json"

# Read the CSV and add data to a dictionary..
data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        province = csvRow["province"]
        data[province] = csvRow
     
# add data to a root node..
root = {}
root["info"] = data

# Write data to a json file...
with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(root, indent = 4))


