class Allergies(object):
    def __init__(self,n):
        self.n = n % 256

        allergies_list = ['cats',
                          'pollen',
                          'chocolate',
                          'tomatoes',
                          'strawberries',
                          'shellfish',
                          'peanuts',
                          'eggs']

        binary = [int(i) for i in bin(self.n)[2:].zfill(8)]
        self.allergies_dict = dict(zip(allergies_list,binary))
        self.lst = [a for a in allergies_list if self.allergies_dict[a]]

    def is_allergic_to(self,allergic):
        if self.allergies_dict[allergic]:
            return True
        return False

