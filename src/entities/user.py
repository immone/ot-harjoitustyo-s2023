class User:
    """Luokka, joka kuvaa yksittäistä käyttäjää.

    Attributes:
        username:
            Merkkijonoarvo, joka kuvaa käyttäjän käyttäjätunnusta.
        password:
            Merkkijonoarvo, joka kuvaa käyttäjän salasanaa.
        skill:
            Merkkijonoarvo, joka kuvaa tehtävien vaikeustasoa.
        correct:
            Kokonaislukuarvo, joka kuvaa oikeiden tehtävien lukumäärää
    """

    def __init__(self, username, password, skill):
        """Luokan konstruktori, joka luo uuden käyttäjän.

        Args:
            username:
                Merkkijonoarvo, joka kuvaa käyttäjän käyttäjätunnusta.
            password:
                Merkkijonoarvo, joka kuvaa käyttäjän salasanaa.
            skill:
                Merkkijonoarvo, joka kuvaa käyttäjän (tai pelin) vaikeustasoa.
        """

        self.username = username
        self.password = password
        self.all_games = []
        self.skill = skill
        self.__correct = 0

    def update_skill(self, new):
        """ Metodi, jolla voi muuttaa käyttäjän valitsemien tehtävien vaikeustasoa.

        Args:
            new: Merkkijonoarvo, joka kuvaa uutta vaikeustasoa
        """
        self.skill = new

    def get_points(self):
        """ Metodi, joka palauttaa käyttäjän pistemäärän.
        """

        return self.__correct
