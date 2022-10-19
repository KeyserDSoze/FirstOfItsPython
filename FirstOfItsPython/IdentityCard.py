
class IdentityCard:
    forename = ""
    lastname = ""
    city = ""

    def get_values(self):
        return self.forename + " " + self.lastname + " from " + self.city
