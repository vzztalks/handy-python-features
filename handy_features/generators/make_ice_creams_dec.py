def make_ice_creams(raw_material):
    for i in range(raw_material):
        yield '🍦({})'.format(i + 1)
