"""Calculates stopping and safety distances for a vehicle at different speeds."""


def in_meters_per_second(speed_kmh):
    """
    Converts a speed from km/h to m/s.
    :param speed_kmh: speed in km/h
    :return: speed in m/s
    """
    return speed_kmh / 3.6


def reaction_distance(speed_mps):
    """
    Calculates the reaction distance.
    :param speed_mps: speed in m/s
    :return: reaction distance in meters
    """
    reaction_time = 1.44  # in Sekunden
    return speed_mps * reaction_time


def braking_distance(speed_mps, dry_road=True):
    """
    Calculates the braking distance.
    :param speed_mps: speed in m/s
    :param dry_road: whether the road is dry
    :return: braking distance in meters
    """
    braking_acceleration = 7 if dry_road else 4  # m/s^2
    return speed_mps**2 / (2 * braking_acceleration)


def stopping_distance(speed_kmh, dry_road=True):
    """
    Calculates the stopping distance (reaction distance + braking distance).
    :param speed_kmh: speed in km/h
    :param dry_road: whether the road is dry
    :return: stopping distance in meters
    """
    speed_mps = in_meters_per_second(speed_kmh)
    return reaction_distance(speed_mps) + braking_distance(speed_mps, dry_road)


def safety_distance_meter(speed_kmh, dry_road=True):
    """
    Calculates the safety distance in meters.
    :param speed_kmh: speed in km/h
    :param dry_road: whether the road is dry
    :return: safety distance in meters
    """
    speed_mps = in_meters_per_second(speed_kmh)
    braking_time = speed_mps / (7 if dry_road else 4)
    return speed_mps * braking_time


def safety_distance_seconds(speed_kmh, dry_road=True):
    """
    Calculates the safety distance in seconds.
    :param speed_kmh: speed in km/h
    :param dry_road: whether the road is dry
    :return: safety distance in seconds
    """
    speed_mps = in_meters_per_second(speed_kmh)
    return speed_mps / (7 if dry_road else 4)


def main():
    for speed in [50, 80, 120]:
        print(f'Anhaltestrecke bei {speed} km/h auf trockener Straße: {stopping_distance(speed)} m')
        print(f'Anhaltestrecke bei {speed} km/h auf nasser Straße: {stopping_distance(speed, dry_road=False)} m')
        print(f'Sicherheitsabstand bei {speed} km/h auf trockener Straße: '
              f'{safety_distance_meter(speed)}m oder {safety_distance_seconds(speed)}s')
        print(f'Anhaltestrecke bei {speed} km/h auf nasser Straße: '
              f'{safety_distance_meter(speed, dry_road=False)}m oder {safety_distance_seconds(speed, dry_road=False)}s')


if __name__ == '__main__':
    main()
