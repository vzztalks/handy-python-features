class IceCreamMakingMachine:

    def __init__(self, raw_material):
        self.raw_material = raw_material
        self.id = 0

    def make_ice_cream(self):
        self.raw_material -= 1
        self.id += 1
        return '🍦({})'.format(self.id)

    def __iter__(self):
        return self

    def __next__(self):
        if self.raw_material > 0:
            return self.make_ice_cream()
        else:
            raise StopIteration("☹ Sorry, no enough raw material")
