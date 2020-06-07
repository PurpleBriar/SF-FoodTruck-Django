import csv

from locatorApp.models import FoodTruckInfo
'''
Function to load data from csv file; will need to update to load from online endpoint
'''
def run():

    FoodTruckInfo.objects.all().delete()

    in_data = open('locatorApp/Mobile_Food_Facility_Permit.csv')
    reader = csv.reader(in_data)

    for row in reader:
        if row[10] != 'APPROVED':
            continue
        current_entry = FoodTruckInfo(locationId=int(row[0]),
                                        name=row[1],
                                        address=row[5],
                                        foodItems=row[11].replace(":", ","),
                                        latitude=float(row[14]),
                                        longitude=float(row[15]))
        print(current_entry)
        current_entry.save()