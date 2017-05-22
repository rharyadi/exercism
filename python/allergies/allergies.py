class Allergies(object):
    def __init__(self,n):
        self.n = n % 256

        allergen_list = ['cats',
                          'pollen',
                          'chocolate',
                          'tomatoes',
                          'strawberries',
                          'shellfish',
                          'peanuts',
                          'eggs']
        
        # Convert allergic score into binary value
        binary = [int(i) for i in bin(self.n)[2:].zfill(8)]
        allergen_dict = dict(zip(allergen_list,binary))
        self.lst = [a for a in allergen_list if allergen_dict[a]]

    def is_allergic_to(self,allergic):
        if allergic in self.lst:
            return True
        return False

