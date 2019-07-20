from handy_features.generators import make_ice_creams


def generator_check():

    ice_cream_making_machine = make_ice_creams(5)

    try:
        print("\nKid 1 is given {}".format(next(ice_cream_making_machine)))

        print("\nKid 2 is given {}".format(next(ice_cream_making_machine)))

        print("\nKid 3 is given {}".format(next(ice_cream_making_machine)))

        print("\nKid 4 is given {}".format(next(ice_cream_making_machine)))

        print("\nKid 5 is given {}".format(next(ice_cream_making_machine)))

        print("\nKid 6 is given {}".format(next(ice_cream_making_machine)))

    except Exception as e:

        print(e)
