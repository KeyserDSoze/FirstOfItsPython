from IdentityCard import IdentityCard
from typing import List
from SqlIntegration.SqlIntegration import *
from AppSettings.AppSettings import *

settings = AppSettings("appsettings.json")

identity_cards: List[IdentityCard] = []

for x in range(0):
    identity_card = IdentityCard()
    print("Insert forename")
    identity_card.forename = input()
    print("Insert lastname")
    identity_card.lastname = input()
    print("Insert city")
    identity_card.city = input()
    identity_cards.append(identity_card)
    print(len(identity_cards))

for identity_card in identity_cards:
    print(identity_card.get_values())

var = SqlIntegration(settings.database_connection)
var.connect()
print(var.query("select * from [dbo].[User]"))
var.disconnect()


    
