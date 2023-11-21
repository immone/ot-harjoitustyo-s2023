import uuid

class Exercise:
    """ Luokka, joka kuvaa yksittäistä tehtävää

        Attributes:
            type:
                Merkkijonoarvo, joka kuvaa tehtävää.
            attemptsLeft:
                 Yksityinen.
                 Kokonaislukuarvo, joka kuvaa yritysten määrää.
            done:
                Vapaaehtoinen, oletusarvoltaan False.
                Boolean-arvo, joka kuvastaa, onko tehtävä jo tehty.
            game:
                Vapaaehtoinen, oletusarvoltaan None.
                Game-olio, joka kuvaa peliä johon tehtävä kuuluu.
            ex_id:
                Vapaaehtoinen, oletusarvoltaan generoitu uuid.
                Merkkijonoarvo, joku kuvaa tehtävän id:tä.
            hint:
                Vapaaehtoinen, oletusarvoltaan None.
                Merkkijonoarvo, joka on tehtäväkohtainen vihje.

    """

    def __init__(self, type, attempts, hint = None, done=False, game = None, ex_id=None):
        """Luokan konstruktori, joka luo uuden tehtävän.

        Args:
            type:
                Merkkijonoarvo, joka kuvaa tehtävää.
            attempts:
                 Kokonaislukuarvo, joka kuvaa yritysten määrää.
            done:
                Vapaaehtoinen, oletusarvoltaan False.
                Boolean-arvo, joka kuvastaa, onko tehtävä jo tehty.
            game:
                Vapaaehtoinen, oletusarvoltaan None.
                Game-olio, joka kuvaa peliä johon tehtävä kuuluu.
            ex_id:
                Vapaaehtoinen, oletusarvoltaan generoitu uuid.
                Merkkijonoarvo, joku kuvaa tehtävän id:tä.
            hint:
                Vapaaehtoinen, oletusarvoltaan None.
                Merkkijonoarvo, joka on tehtäväkohtainen vihje.
        """

        self.__attemptsLeft = attempts
        self.type = type
        self.hint = hint
        self.done = done
        self.solved = False
        self.game = game
        self.id = ex_id or str(uuid.uuid4())

    def is_done(self):
        """Apumetodi. Tarkastaa onko tehtävä ohi."""
        return self.done or self.__attemptsLeft == 0

    def decrease_attempts(self):
        """Apumetodi. Vähentää yrityksiä yhdellä. """
        if self.__attemptsLeft >= 1: self.__attemptsLeft -= 1

    def end_exercise(self):
        """ Parametriton metodi, joka päättää tehtävän, jos se on ohi
            ja kasvattaa pelaajan pisteitä, jos hän on vastannut oikein.

        Returns:
            Palauttaa True, jos harjoitus on ohi.
            Muussa tapauksessa palauttaa False.
        """
        if self.is_done():
            if self.solved:
                self.game.user.increase_points()
            return True
        return False


class MultipleChoice(Exercise):
    """ Aliluokka, joka mallintaa monivalintakysymystä.

        Attributes:
          answers:
            Lista, joka kuvaa mitä kysymyksiä käyttäjä on jo arvannut.
          questions:
            Kirjasto, joka koostuu kysymyksistä ja vastausvaihtoehdot.
          n:
            Kokonaislukuarvo, joka kuvaa kysymysten määrää
          correct:
            Yksityinen.
            Kuvaa oikean vastauksen indeksiä.

    """

    def __init__(self, type, attempts, hint = None, done=False, user=None, ex_id=None):
        """ Luokan konstruktori, joka luo uuden monivalintatehtävän.

        """
        super().__init__(type, attempts, hint, done, user, ex_id)
        self.__answers = []
        self.__questions = {}
        self.n = None
        self.__correct = None
        self.solved = False

    def set_question(self, q, a, correct):
        """ Metodi, joka lisää kysymyksen monivalintaan.

            Args:
                q:
                    Merkkijonoarvo, joka kuvaa kysymystä.
                a:
                    Lista, jossa on vastaukset.
                correct:
                    Kokonaislukuarvo, joka kuvaa oikean vastauksen indeksiä (alkaen luvusta 1).
        """
        self.__questions[q] = a
        self.n = len(list(self.__questions.values())[0])
        if correct < 1 or correct > self.n:
            raise ValueError("The correct choice should be an integer between 1 and n.")
        self.__correct = correct

    def check_answer(self, a):
        """ Metodi, joka tarkastaa onko vastaus oikein.

            Args:
                a: Kokonaislukuarvo, joka kuvaa vastausvaihtoehtoa.

            Returns:
                True, jos vastaus on oikein.
                False, jos vastaus on väärin.
        """
        print(self.n)
        if a < 0 or a > self.n:
            raise ValueError("The answer should be an integer between 1 and n.")
        self.__answers.append(a)
        if a == self.__correct:
            self.solved = True
            return True
        if a in self.__answers:
            return False
        else:
            self.decrease_attempts()
            return False

class DefinitionExercise(MultipleChoice):
    """ Aliluokka, joka kuvaa yksittäistä määritelmätehtävää.
    """
    def __init__(self, type, attempts, hint = None, done=False, user=None, ex_id=None):
        """ Luokan konstruktori, joka luo uuden monivalintatehtävän.
        """
        super().__init__(type, attempts, hint, done, user, ex_id)


class ProblemExercise(MultipleChoice):
    """ Aliluokka, joka kuvaa yksittäistä ongelmatehtävää.
    """
    def __init__(self, type, attempts, hint = None, done=False, user=None, ex_id=None):
        """ Luokan konstruktori, joka luo uuden ongelmatehtävän.

        """
        super().__init__(type, attempts, hint, done, user, ex_id)

class TheoremExercise(MultipleChoice):
    """ Aliluokka, joka kuvaa yksittäistä teorematehtävää.
    """
    def __init__(self, type, attempts, hint = None, done=False, user=None, ex_id=None):
        """ Luokan konstruktori, joka luo uuden teoreematehtävän.

        """
        super().__init__(type, attempts, hint, done, user, ex_id)

