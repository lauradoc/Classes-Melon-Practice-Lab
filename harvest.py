############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        self.pairing = []


    def add_pairing(self, *pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairing.extend(pairing)
        

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('musk', 1998, 'green',
                    True, True, 'Muskmelon')
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('cas', 2003, 'orange',
                    False, False, 'Casaba')
    cas.add_pairing('strawberries', 'mint')
    all_melon_types.append(cas)

    cren = MelonType('cren', 1996, 'green',
                    False, False, 'Crenshaw')
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yw = MelonType('yw', 2013, 'yellow',
                    False, True, 'Yellow Watermelon')
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f'{melon.name} pairs with \n -{melon.pairing}')

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}

    for melon in melon_types:

        melon_dict[melon.code] = melon

    return melon_dict

############
# Part 2   #
############

melon_types = make_melon_types() 

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, MelonType, shape, color, field, harvester):
        self.shape = shape
        self.color = color
        self.field = field
        self.harvester = harvester

    def is_sellable(self):

        if self.shape > 5 and self.color > 5 and self.field != 3:
            return True 

        else:
            return False

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melon_list = []

    melons_by_id = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon_list.append(melon_1)

    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon_list.append(melon_2)

    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon_list.append(melon_3)

    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon_list.append(melon_4)

    melon_5 = Melon(melons_by_id['cas'], 8, 9, 35, 'Michael')
    melon_list.append(melon_5)

    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon_list.append(melon_6)

    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon_list.append(melon_7)

    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon_list.append(melon_8)

    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')
    melon_list.append(melon_9)


    return melon_list


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable() is True:

            print(f'Harvested by {melon.harvester} from Field {melon.field} (CAN BE SOLD)')

        else:
            print(f'Harvested by {melon.harvester} from Field {melon.field} (NOT SELLABLE)')


def create_melon_log(melon_types):
    """loops over file creating melon object for each line of file"""

    harvest_log = open('harvest_log.txt')


    melon_objects = []

    for line in harvest_log:

        line = line.split(' ')

        melon = Melon(line[5], line[1], line[3], line[11], line[8])
        
        melon_objects.append(melon)

    return melon_objects




