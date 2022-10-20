from IdentityCard import IdentityCard
from typing import List
from Storage.SqlIntegration import *
from Settings.AppSettings import *

settings = AppSettings("appsettings.json")
var = SqlIntegration(settings.database_connection)
print(var.execute_query('''
    IF NOT EXISTS (SELECT 'X'
                       FROM   INFORMATION_SCHEMA.TABLES
                       WHERE  TABLE_NAME = 'Table_IdentityCards'
                              AND TABLE_SCHEMA = 'dbo')
    BEGIN
        CREATE TABLE Table_IdentityCards (
            Id int NOT NULL IDENTITY primary key,
            ForeName varchar(255) NOT NULL,
            LastName varchar(255) NOT NULL,
            City varchar(255) NOT NULL
        )
    END
            '''))
print(var.read_query("select * from [dbo].[Table_IdentityCards]"))
identity_cards: List[IdentityCard] = []
print(identity_cards)
print("insert the word 'e' to exit")
insertSomething = input()
while insertSomething != "e":
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
    print("insert the word 'e' to exit")
    insertSomething = input()

for identity_card in identity_cards:
    print(identity_card.get_values())
print(identity_cards)

for identity_card in identity_cards:
    var.execute_query(f'''
        Insert into Table_IdentityCards (ForeName, LastName, City) values (
            '{identity_card.forename}',
            '{identity_card.lastname}',
            '{identity_card.city}'
            )
            ''')
print(var.read_query("select * from [dbo].[Table_IdentityCards]"))
