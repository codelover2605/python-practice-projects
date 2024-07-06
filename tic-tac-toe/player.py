class Player:

    def __init__(self, marker, name):
        self._marker = marker
        self._name = name

    def choose_spot(self, available_spots):
        spot = -1
        while spot not in available_spots:
            spot = int(input(f'\n{self._name}: Choose a spot from {available_spots}: '))

        return spot

    @property
    def marker(self):
        return self._marker

    @property
    def name(self):
        return self._name
