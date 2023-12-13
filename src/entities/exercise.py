import uuid


class Exercise:
    """ Luokka, joka kuvaa yksittäistä tehtävää

        Attributes:
            description:
                Merkkijonoarvo, joka kuvaa tehtävää.
            difficulty:
                Merkkijono, joka kuvaa tehtävän vaikeutta.
            content:
                Lista. Sisältää tehtävän sisällön; sen ensimmäinen
                alkio on tehtävän kysymys, seuraavat alkiot vaihtoehtoja ja
                viimeinen alkio oikea vastaus.
            hint:
                Vapaaehtoinen, oletusarvoltaan None.
                Merkkijonoarvo, joka on tehtäväkohtainen vihje.
            ex_id:
                Vapaaehtoinen, oletusarvoltaan generoitu uuid.
                Merkkijonoarvo, joku kuvaa tehtävän id:tä.
    """

    def __init__(self, description, content, difficulty, hint=None, ex_id=None):
        """Luokan konstruktori, joka luo uuden tehtävän.

        Args:
            description:
                Merkkijonoarvo, joka kuvaa tehtävää.
            difficulty:
                Merkkijono, joka kuvaa tehtävän vaikeutta.
            content:
                Lista. Sisältää tehtävän sisällön; sen ensimmäinen
                alkio on tehtävän kysymys, seuraavat alkiot vaihtoehtoja ja
                viimeinen alkio oikea vastaus.
            hint:
                Vapaaehtoinen, oletusarvoltaan None.
                Merkkijonoarvo, joka on tehtäväkohtainen vihje.
            ex_id:
                Vapaaehtoinen, oletusarvoltaan generoitu uuid.
                Merkkijonoarvo, joku kuvaa tehtävän id:tä.
        """

        self.difficulty = difficulty
        self.description = description
        self.content = content
        self.__attempts_left = 1
        self.hint = hint
        self.done = False
        self.solved = False
        self.id = ex_id or str(uuid.uuid4())

    def is_done(self):
        """Apumetodi. Tarkastaa onko tehtävä ohi."""
        return self.done or self.__attempts_left == 0

    def decrease_attempts(self):
        """Apumetodi. Vähentää yrityksiä yhdellä. """
        if self.__attempts_left >= 1:
            self.__attempts_left -= 1

    def end_exercise(self):
        """ Parametriton metodi, joka päättää tehtävän.

        Returns:
            Palauttaa True, jos harjoitus on ohi.
            Muussa tapauksessa palauttaa False.
        """
        self.done = True
        if self.solved:
            return True
        return False


class MultipleChoice(Exercise):
    """ Aliluokka, joka mallintaa monivalintakysymystä.

        Attributes:
            description:
                Merkkijonoarvo, joka kuvaa tehtävää.
            difficulty:
                Merkkijono, joka kuvaa tehtävän vaikeutta.
            content:
                Lista. Sisältää tehtävän sisällön; sen ensimmäinen
                alkio on tehtävän kysymys, seuraavat alkiot vaihtoehtoja ja
                viimeinen alkio oikea vastaus.
            hint:
                Vapaaehtoinen, oletusarvoltaan None.
                Merkkijonoarvo, joka on tehtäväkohtainen vihje.
            ex_id:
                Vapaaehtoinen, oletusarvoltaan generoitu uuid.
                Merkkijonoarvo, joku kuvaa tehtävän id:tä.
    """

    def __init__(self, description, content, difficulty, hint=None, ex_id=None):
        """ Luokan konstruktori, joka luo uuden monivalintatehtävän.

        """
        self.n = len(content)
        if self.n < 3:
            raise ValueError(
                "A multiple choice exercise should have at least one question")
        self.question = content[0]
        self.options = content[1:-1]
        self.answer = content[-1]
        if self.answer < 0 or self.answer >= self.n:
            raise ValueError(
                "The correct choice should be one of the options")
        super().__init__(description, content, difficulty, hint, ex_id)

    def check_answer(self, a):
        """ Metodi, joka tarkastaa onko vastaus oikein.

            Args:
                a: Kokonaislukuarvo, joka kuvaa vastausvaihtoehtoa.

            Returns:
                True, jos vastaus on oikein.
                False, jos vastaus on väärin.
        """
        if a < 0 or a > self.n:
            raise ValueError(
                f"The answer should be a positive integer between 1 and {self.n-1}.")
        self.decrease_attempts()
        if a == self.answer:
            self.solved = True
            return True
        return False


class DefinitionExercise(MultipleChoice):
    """ Aliluokka, joka kuvaa yksittäistä määritelmätehtävää.
    """


class ProblemExercise(MultipleChoice):
    """ Aliluokka, joka kuvaa yksittäistä ongelmatehtävää.
    """


class TheoremExercise(MultipleChoice):
    """ Aliluokka, joka kuvaa yksittäistä teorematehtävää.
    """