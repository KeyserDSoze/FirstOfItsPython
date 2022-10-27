from IdentityCard import IdentityCard
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

print("insert the word 'e' to exit")
insertSomething = input()
while insertSomething != "e":
    identity_card = IdentityCard(print, input)
    identity_card.set_values()
    identity_card.set_values2()
    var.execute_query(f'''
        Insert into Table_IdentityCards (ForeName, LastName, City) values (
            '{identity_card.forename}',
            '{identity_card.lastname}',
            '{identity_card.city}'
            )
            ''')
    print("insert the word 'e' to exit")
    insertSomething = input()

    
print(var.read_query("select * from [dbo].[Table_IdentityCards]"))