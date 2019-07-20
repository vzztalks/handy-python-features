from .issuing_machine_dec import IssuingMachine


class Refrigerator:

    def __init__(self):
        self.ice_creams = ['🍦(1)', '🍦(2)', '🍦(3)', '🍦(4)', '🍦(5)']

    def __iter__(self):
        return IssuingMachine(self.ice_creams)
