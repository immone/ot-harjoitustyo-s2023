import uuid
from src.entities.question_generator import QuestionGenerator, GroupQuestionGenerator


class Game:
    """ Luokka, joka kuvaa yksittäistä harjoituspeliä.

        Attributes:
            type:
                Merkkijonoarvo, joka kuvaa tehtävän tyyppiä.
            done:
                Vapaaehtoinen, oletusarvoltaan False.
                Boolean-arvo, joka kuvastaa, onko peli ohi.
            n:
                Kokonaislukuarvo, joka kuvaa kysymysen lukumäärää.
            difficulty:
                Merkkijonoarvo, joka kuvaa pelin vaikeutta.
            problems:
                Lista, joka kuvaa pelin kaikkia kysmyksiä.
            user:
                Vapaaehtoinen, oletusarvoltaan None.
                User-olio, joka kuvaa tehtävän omistajaa.
            game_id:
                Vapaaehtoinen, oletusarvoltaan generoitu uuid.
                Merkkijonoarvo, joku kuvaa pelin id:tä.


    """

    def __init__(self, type, n, difficulty, user, game_id=None):
        """Luokan konstruktori, joka luo uuden tehtävän.

        Args:
            type:
                Merkkijonoarvo, joka kuvaa pelin tyyppiä.
            done:
                Vapaaehtoinen, oletusarvoltaan False.
                Boolean-arvo, joka kuvastaa, onko peli ohi.
            difficulty:
                Merkkijonoarvo, joka kuvaa pelin vaikeutta.
            n:
                Kokonaislukuarvo, joka kuvaa kysymysten lukumäärää.
            user:
                Vapaaehtoinen, oletusarvoltaan None.
                User-olio, joka kuvaa tehtävän omistajaa.
            id:
                Vapaaehtoinen, oletusarvoltaan generoitu uuid.
                Merkkijonoarvo, joku kuvaa pelin id:tä.
        """

        self.difficulty = difficulty
        self.n = n
        self.type = type
        self.done = False
        self.__user = user
        self.id = game_id or str(uuid.uuid4())
        self.__generator = GroupQuestionGenerator(self.n, 3, self.difficulty, type, 1)
        self.__problems = self.__generator.fetch_problems()

    def player(self):
        """ Palauttaa peliä pelaavan User-olion. """
        return self.__user