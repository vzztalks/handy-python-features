from handy_features.iterators import Refrigerator
from handy_features.iterators import IceCreamMakingMachine


def iterator_check():
    refrigerator = Refrigerator()

    issuer_machine = iter(refrigerator)

    try:
        print("\nKid 1 is given {}".format(next(issuer_machine)))

        print("\nKid 2 is given {}".format(next(issuer_machine)))

        print("\nKid 3 is given {}".format(next(issuer_machine)))

        print("\nKid 4 is given {}".format(next(issuer_machine)))

        print("\nKid 5 is given {}".format(next(issuer_machine)))

        print("\nKid 6 is given {}".format(next(issuer_machine)))

    except Exception as e:

        print('\n' + str(e))


def iterator_save_memory_check():
    ice_cream_making_machine = IceCreamMakingMachine(5)

    try:
        print("\nKid 1 is given {}".format(next(ice_cream_making_machine)))

        print("\nKid 2 is given {}".format(next(ice_cream_making_machine)))

        print("\nKid 3 is given {}".format(next(ice_cream_making_machine)))

        print("\nKid 4 is given {}".format(next(ice_cream_making_machine)))

        print("\nKid 5 is given {}".format(next(ice_cream_making_machine)))

        print("\nKid 6 is given {}".format(next(ice_cream_making_machine)))

    except Exception as e:

        print('\n' + str(e))
