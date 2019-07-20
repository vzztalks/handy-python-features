class IssuingMachine:

    def __init__(self, ice_creams):
        self.ice_creams = ice_creams

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.ice_creams) > 0:
            return self.ice_creams.pop(0)
        else:
            raise StopIteration("☹ Sorry, no ice creams in the store")
