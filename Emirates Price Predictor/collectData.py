#COLLECTING THE DATA FROM APIs
from bs4 import BeautifulSoup
import requests
import pandas as pd
import flightradar24
import json
import numpy as np

airline = 'UAE' #ICAO Code (UAE for Emirates)
fr = flightradar24.Api()
flights = fr.get_flights(airline)
flightStage2 = []
for i in flights:
    if (i != "stats") and (i != "full_count") and (i != "version"):
        flightStage2.append(flights[i])
flightStage3 = []
for i in flightStage2:
    holder = []
    holder2 = []
    holder.append(i[8])
    holder.append(i[9])
    holder2.append(i[11])
    holder2.append(i[12])
    dxb = 0
    notdxb = 0

    for x in holder2:
        if x == "DXB":
            dxb += 1
        elif x == "":
            pass
        else:
            notdxb+=1
    if (dxb == 1) and (notdxb == 1):
        if holder2[0] == "DXB":
            holder.append(holder2[1])
            flightStage3.append(holder)
        else:
            holder.append(holder2[0])

            flightStage3.append(holder)
FAPay = 16
aircraftLibrary = {
    "A388": 519,
    "B77L": 302,
    "B77W": 354
}
aircraftSpeeds = {
    "A388": 652.2,
    "B77L": 644.5,
    "B77W": 644.5
}
aircraftFAs = {
    "A388": 21,
    "B77L": 10,
    "B77W": 14
}
pilotPays = {
    "A388": (293+192+102),
    "B77L": (280+182+182),
    "B77W": (280+182+182)
}
cargoAircraft = ["A6-EFF","A6-EFG","A6-EFH","A6-EFI","A6-EFJ","A6-EFK","A6-EFL","A6-EFM","A6-EFN","A6-EFO","A6-EFS","A6-EGD","A6-EBJ"]
flightStage4 = []
for i in flightStage3:
    keep = True
    for x in cargoAircraft:
        if i[1] == x:
            keep = False
    if keep == True:
        flightStage4.append(i)
flightStage5 = []
destinations = []
for i in flightStage4:
    duplicate = False
    for x in destinations:
        if i[2] == x:
            duplicate = True

    if duplicate == False:
        flightStage5.append(i)
        destinations.append(i[2])
prices = []
places = []
airplanes = []
registrations = []
distances = []
capacity = []
cruise_speeds = []
totalFAPay = []
flight_time = []
FCPay = []
total_crew_pay = []
for i in flightStage5: #WEB SCRAPING TO FIND OUT DISTANCES FROM DXB
    places.append(i[2])
    airplanes.append(i[0])
    registrations.append(i[1])

    page = requests.get("https://www.prokerala.com/travel/airports/distance/from-dxb/to-"+str(i[2]).lower()+"/")
    soup = BeautifulSoup(page.content, "html.parser")
    try:
        distanceStage1 = soup.find_all('h2')[0:4][0].string
        holderstring = ""
        holderchar = ""
        index = 0
        while holderchar != "m":
            holderstring = holderstring + (distanceStage1[index])
            index += 1
            holderchar = distanceStage1[index]

        distances.append(holderstring)
    except:
        distances.append("")
    capacity.append(aircraftLibrary[i[0]])
    cruise_speeds.append(aircraftSpeeds[i[0]])
    time = (int(float(holderstring))/(aircraftSpeeds[i[0]]))
    flight_time.append(int(float(time))+2)
    totalFAPay.append(int(float((aircraftFAs[i[0]]) * time)))
    FCPay.append(int(float(pilotPays[i[0]]*time)))
    total_crew_pay.append(int(float((pilotPays[i[0]]*time)+((aircraftFAs[i[0]]) * time))))



querystring = {"inboundpartialdate": "2021-5-01"}

headers = {
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    'x-rapidapi-key': "Get your own API key and insert here"
}
for i in places:
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browseroutes/v1.0/US/USD/en-US/DXB-sky/"+str(i)+"-sky/2020-07-16"

    response = requests.request("GET", url, headers=headers)
    skyscannerStage1 = response.text
    skyscannerStage2 = res = json.loads(skyscannerStage1)
    skyscannerStage3 = skyscannerStage2["Quotes"]
    found = False
    for x in skyscannerStage3:
        id = x["QuoteId"]
        airlineOne = x["OutboundLeg"]
        if airlineOne["CarrierIds"] == [1035]:
            found = True
            prices.append(x["MinPrice"])
            break
    if found != True:
        prices.append("")
print(len(places))
print(len(prices))


flightStage6 = {"Aircraft_Registration" : registrations,"Aircraft_Type":airplanes,"Route":places,"Distances": distances,"Total_Capacity":capacity,"Price":prices,"Cruise_Speed": cruise_speeds,"Flight_time": flight_time,"Cabin_Crew_Hourly_Pay": totalFAPay,"Flight_Crew_Hourly_Pay": FCPay,"Total_Staff_Pay": total_crew_pay}
df =pd.DataFrame.from_dict(flightStage6)
df.to_csv(r'data.csv')

airport = "ATL" #predicting ticket prices for a route Emirates doesn't operate yet, this is Atlanta, GA, USA
page = requests.get("https://www.prokerala.com/travel/airports/distance/from-dxb/to-" + str(airport).lower() + "/")
soup = BeautifulSoup(page.content, "html.parser")
distanceStage1 = soup.find_all('h2')[0:4][0].string
holderstring = ""
holderchar = ""
index = 0
while holderchar != "m":
    holderstring = holderstring + (distanceStage1[index])
    index += 1
    holderchar = distanceStage1[index]
time1 = (int(float(holderstring))/(aircraftSpeeds["B77W"]))
time1 += 2

totalPilotPay = (pilotPays["B77W"]*time1)
totalCCPay = (aircraftFAs["B77W"]*time1)
totalStaff = totalPilotPay+totalCCPay
finalstage = {
    "Distances": [holderstring],
    "Flight_time": [time1],
    "Total_Staff_Pay": [totalStaff]
}
finalArray = pd.DataFrame.from_dict(finalstage)
finalArray.to_csv(r'data2.csv')










