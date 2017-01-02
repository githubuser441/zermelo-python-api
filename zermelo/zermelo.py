import os
import json
import requests
from dateutil import parser
try:
    from bs4 import BeautifulSoup
except ImportError:
    print("""
    Als u gebruik wilt maken van de get_nieuws() functie
     heeft u de BeautifulSoup libary nodig.""")

class Zermelo(object):

    def __init__(self, school="", koppelcode="", save=False):
        koppelcode=koppelcode.replace(" ", "")
        self.session = requests.Session()
        if save and os.path.exists("token.json"):
            with open('token.json') as token_file:
                token_data = json.load(token_file)
                school = token_data['school']
        else:
            if school == "":
                raise TypeError("__init__() missing 1 required positional argument: \'school\'")
            if school == "":
                raise TypeError("__init__() missing 1 required positional argument: \'koppelcode\'")
        self.url = 'https://'+school+'.zportal.nl/api/'

        if not os.path.exists("token.json"):
            token_response = self.session.post(url=self.url+'v3/oauth/token',  data={
            "grant_type": "authorization_code",
            "code":koppelcode
            })
            if token_response.status_code == 200:
                token_data = json.loads(token_response.text)
            elif token_response.status_code == 400:
                raise Exception("error 400: koppelcode is ongeldig")
            else:
                raise Exception("error "+str(token_response.status_code))

        self.access_token = token_data['access_token']

        if save and not os.path.exists("token.json"):
            token_data['school'] = school
            with open('token.json', 'w') as token_file:
                json.dump(token_data, token_file)
            self.access_token = token_data['access_token']

    def get_user(self, user="~me", extra={}):
        params = {
            'access_token': self.access_token
        }
        params.update(extra)
        r = self.session.get(self.url+'v3/users/'+user, params=params)
        if r.status_code != 200:
            raise Exception("error "+str(r.status_code)+"\n"+r.text)
        return json.loads(r.text)['response']['data']

    def get_afspraken(self, start, end, user="~me", extra={}):
        params = {
            'user': user,
            'start': start,
            'end': end,
            'access_token': self.access_token
        }
        params.update(extra)
        r = self.session.get(self.url+'v3/appointments', params=params)
        if r.status_code != 200:
            raise Exception("error "+str(r.status_code)+"\n"+r.text)
        return json.loads(r.text)['response']['data']

    def get_mededelingen(self, start=False, end=False, user="~me"):
        params = {
            'user': user,
            'access_token': self.access_token
        }
        if start:
            params['start'] = start
        if end:
            params['end'] = end

        r = self.session.get(self.url+'v2/announcements', params=params)
        if r.status_code != 200:
            raise Exception("error "+str(r.status_code)+"\n"+r.text)
        return json.loads(r.text)['response']['data']

    def get_status(self):
        r = self.session.get(self.url+'v3/status/status_message')
        if r.status_code != 200:
            raise Exception("error "+str(r.status_code)+"\n"+r.text)
        return r.text

    """ misschien ooit
    def get_nieuws(self):
        r = self.session.get(self.url+'v3//status/news')
        if r.status_code != 200:
            raise Exception("error "+str(r.status_code)+"\n"+r.text)

        soup = BeautifulSoup(r.text, 'html.parser')
        for nieuws_artikel in soup.find_all('p'):
            print(nieuws_artikel)
            try:
                datum = parser.parse(str(nieuws_artikel.i.text))
            except ValueError:
                datum = parser.parse(str(nieuws_artikel.i.text[:-7])) # quick and hackie
            content = nieuws_artikel.text.replace()

            print(datum)
            print(content)
            print("-------------------")


        return True
        """
