"""Calculates stopping and safety distances for a vehicle at different speeds."""


def in_meters_per_second(speed_kmh):
    """
    Converts a speed from km/h to m/s.
    :param speed_kmh: speed in km/h
    :return: speed in m/s
    """
    pass


def reaction_distance(speed_mps):
    """
    Calculates the reaction distance.
    :param speed_mps: speed in m/s
    :return: reaction distance in meters
    """
    pass


def braking_distance(speed_mps, dry_road=True):
    """
    Calculates the braking distance.
    :param speed_mps: speed in m/s
    :param dry_road: whether the road is dry
    :return: braking distance in meters
    """
    pass


def stopping_distance(speed_kmh, dry_road=True):
    """
    Calculates the stopping distance (reaction distance + braking distance).
    :param speed_kmh: speed in km/h
    :param dry_road: whether the road is dry
    :return: stopping distance in meters
    """
    pass


def safety_distance_meter(speed_kmh, dry_road=True):
    """
    Calculates the safety distance in meters.
    :param speed_kmh: speed in km/h
    :param dry_road: whether the road is dry
    :return: safety distance in meters
    """
    pass


def safety_distance_seconds(speed_kmh, dry_road=True):
    """
    Calculates the safety distance in seconds.
    :param speed_kmh: speed in km/h
    :param dry_road: whether the road is dry
    :return: safety distance in seconds
    """
    pass


def main():
    # TODO: Berechne die Anhaltestrecke und den Sicherheitsabstand für 50, 80 und 120 km/h
    # TODO: Ruf die Funktionen auf und gib das Ergebnis aus
    ...


if __name__ == '__main__':
    main()
