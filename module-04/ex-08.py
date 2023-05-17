def game(terra, power):
    for terra_in in terra:
        for energy in terra_in:
            if power >= energy:
                power += energy
            else:
                break
    return power