from zermelo.zermelo import Zermelo
import datetime
import time
import pytz
import json

Z = Zermelo('je school', 'je koppelcode', True)
eind_datum = 7

# start en eind datum ophalen
nu = datetime.date.today()
start = nu
end = start + datetime.timedelta(days=eind_datum)
start = int(time.mktime(start.timetuple()))
end = int(time.mktime(end.timetuple()))

# user
user = Z.get_user()[0]
print("Hallo {} {} welkom bij de python-zermelo-api".format(user['firstName'],user['lastName']))

# afspraken
print("afspraken:")
afspraken = Z.get_afspraken(start, end)
afspraken = sorted(afspraken, key=lambda d: d['start'])
4
startDate_old = 0
for afspraak in afspraken:
    startDate = datetime.datetime.fromtimestamp(
                    int(afspraak['start'])
                ).date()
    if startDate != startDate_old:
        print("-----------------------")
    print(afspraak['startTimeSlotName']+' '+afspraak['subjects'][0]+' in '+afspraak['locations'][0])
    startDate_old = startDate
if len(afspraken) == 0:
    print("Er zijn geen afspraken in de komende {} dagen".format(eind_datum))

# mededelingen
print("mededelingen:")
mededelingen = sorted(Z.get_mededelingen(), key=lambda d: d['start'])

for mededeling in mededelingen:
     print("-----------------------")
     print(mededeling['title']+'\n'+mededeling['text'])
if len(mededelingen) == 0:
    print("Er zijn geen mededelingen")

print("status:")
print(Z.get_status())
