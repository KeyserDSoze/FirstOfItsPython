from IdentityCard import IdentityCard

identity_cards: list[IdentityCard] = []

for x in range(5):
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



    
