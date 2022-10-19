from IdentityCard import IdentityCard


identity_card = IdentityCard()
print(identity_card)
identity_card2 = IdentityCard()
identity_card2.forename = "Alessandro"
print(identity_card2)
identity_card = IdentityCard()
print(identity_card)
identity_card = IdentityCard()
print(identity_card)
identity_card = IdentityCard()
print(identity_card)
identity_card = IdentityCard()
print(identity_card)
print("Insert forename")
identity_card.forename = input()
print("Insert lastname")
identity_card.lastname = input()
print("Insert city")
identity_card.city = input()

print(identity_card)
print(identity_card2)
print(identity_card.get_values())
print(identity_card.get_values())
print(globals())