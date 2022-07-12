import csv

from attr import field

data =[]


with open("archive_dataset.csv","r")as s:
    csvreader = csv.reader(s)
    for row in csvreader:
        data.append(row)

headers = data[0]

planet_data = data[1:]
for data in planet_data:
    data[2]=data[2].lower()

planet_data.sort(key=lambda planet_data:planet_data[2])

with open("archive_datasets_sorted.csv","a+")as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)

#removing blank line
with open("archive_datasets_sorted.csv")as input, open("archive_datasets_sorted1.csv","w",newline="")as output:
    writer=csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)
            
