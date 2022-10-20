from IdentityCard import IdentityCard
from typing import List
from Storage.SqlIntegration import *
from Settings.AppSettings import *

settings = AppSettings("appsettings.json")
identity_cards: List[IdentityCard] = []
print(identity_cards)
for x in range(3):
    identity_card = IdentityCard()
    print("Insert forename")
    identity_card.forename = input()
    print("Insert lastname")
    identity_card.lastname = input()
    print("Insert city")
    identity_card.city = input()
    identity_cards.append(identity_card)
    print(len(identity_cards))
    print(identity_card)

for identity_card in identity_cards:
    print(identity_card.get_values())
print(identity_cards)
var = SqlIntegration(settings.database_connection)
print(var.execute_query("CREATE TABLE Persons (PersonID int,LastName varchar(255),FirstName varchar(255),Address varchar(255),City varchar(255))"))
print(var.read_query("select * from [dbo].[Persons]"))

