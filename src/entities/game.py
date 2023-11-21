import uuid
from question_generator import QuestionGenerator
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

    def __init__(self, type, n, difficulty, done=False, user = None, game_id=None):
        """Luokan konstruktori, joka luo uuden tehtävän.

        Args:
            type:
                Merkkijonoarvo, joka kuvaa tehtävän tyyppiä.
            done:
                Vapaaehtoinen, oletusarvoltaan False.
                Boolean-arvo, joka kuvastaa, onko peli ohi.
            difficulty:
                Merkkijonoarvo, joka kuvaa pelin vaikeutta.
            n:
                Kokonaislukuarvo, joka kuvaa kysymysen lukumäärää.
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
        self.__problems = self.__generator.fetch_problems()
        self.done = done
        self.user = user
        self.id = game_id or str(uuid.uuid4())
        self.__generator = QuestionGenerator(self.n, self.difficulty, type)