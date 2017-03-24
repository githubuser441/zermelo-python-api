# zermelo-python-api
Een simpele onofficele wrapper voor de zermelo api.

Deze zermelo-python-api maakt gebruik van de requests libary dus deze moet worden geinstalleerd:

`pip install requests`

De volgende functies zijn beschikbaar:
- get_user() geeft een list met alle data over de huidige gebruiker
  - parameters:
  - (optioneel) *user* het id van de gebruiker waarvan u de data wilt LETOP: dit kan alleen als u de benodigde rechten hebt.
- get_afspraken() geeft een list met alle afspraken binnen de gegeven tijdvan de huidige gebruiker
  - parameters:
  - *start* datetime object met de start datum waarvan u alle afspraken wilt
  - *end* datetime object met de eind datum waarvan u alle afspraken wilt
  - (optioneel) *user* het id van de gebruiker waarvan u de data wilt
- get_mededelingen() geeft een list met alle mededelingen voor huidige gebruiker
  - parameters:
  - (optioneel) *user* het id van de gebruiker waarvan u de data wilt
- get_status() geeft een string met de huidige status van zermelo op uw school

Gebruik tijdelijk voor informatie over de output van de functies de [officele zermelo restapi documentatie](https://zermelo.atlassian.net/wiki/display/DEV/API+Entities)

### TODO:
- [ ] zet timestamp data die word opgehaalt van de api om in datetime objecten
- [ ] documentatie voor de output van functies
