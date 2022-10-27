
class IdentityCard:
    forename = ""
    lastname = ""
    city = ""

    def __init__(self, output_method, input_method):
        self.output_method = output_method
        self.input_method = input_method

    def get_values(self):
        return self.forename + " " + self.lastname + " from " + self.city

    def set_values(self):
        self.output_method("Insert forename")
        self.forename = self.input_method()
        self.output_method("Insert lastname")
        self.lastname = self.input_method()
        
        
    def set_values2(self):
        self.output_method("Insert city")
        self.city = self.input_method()