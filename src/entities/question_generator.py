import random
from parser import *
from exercise import *
# Refaktoroi johonkin järkevämpään paikkaan
QUESTIONS_3 = ["0"]
ANSWERS_3 = [("Easy", "Group definition", "Which parts are included in the definition of a group?", 0, 2),
            ["Associativity, an inverse element under an operation and a neutral element",
             "Commutativity, an inverse element under an operation and a neutral element",
             "Distributivity, an inverse element under an operation and a neutral element"]
             ]
class QuestionGenerator:
    """Luokka, joka generoi tehtäväkysymyset.

    Attributes:
        n:
            Kokonaislukuarvo, joka kuvaa generoitavien kysymysten määrää.
        cn:
            Kokonaislukuarvo, joka kuvaa yhden kysymyksen monivalintojen lukumäärää.
        difficulty:
            Merkkijonoarvo, joka kuvaa kysymysten vaikeustasoa.
        type:
            Merkkijonoarvo, joka kuvaa kysymysten tyyppiä.
        attempts:
            Kokonaislukuarvo, joka kuvaa yritysten määrää.
    """

    def __init__(self, n, cn, difficulty, type, attempts):
        """Luokan konstruktori, joka luo uuden kysymysgeneraattorin.

        Args:
            n:
                Kokonaislukuarvo, joka kuvaa generoitavien kysymysten määrää.
            cn:
                Kokonaislukuarvo, joka kuvaa yhden kysymyksen monivalintojen lukumäärää.
            difficulty:
                Merkkijonoarvo, joka kuvaa kysymysten vaikeustasoa.
            type:
                Merkkijonoarvo, joka kuvaa kysymysten tyyppiä.
        """

        self.cn = cn
        self.n = n
        self.difficulty = difficulty
        self.type = type
        self.attempts = attempts

    def fetch_problems(self):
        """ Metodi, joka palauttaa kirjaston generoituja kysymyksiä."""
        raise NotImplementedError("Subclass needs to implement.")

    def randomized_problem(self, choices, difficulty):
        """ Metodi, joka hakee yhden halutunlaisen kysymysksen.

            Args:
                choices:
                    Kokokonasilukuarvo, joka kuvaa kysymysten lukumäärää
                difficulty:
                    Merkkijonoarvo, joka kuvaa kysymysten vaikeutta
        """
        raise NotImplementedError("Subclass needs to implement.")


class GroupQuestionGenerator(QuestionGenerator):
    """Aliluokka, joka generoi ryhmäteoreettiset kysymykset.

    """

    def __init__(self, n, cn, difficulty, type, attempts):
        """ Luokan konstruktori, joka luo uuden monivalintatehtävän.
        """
        super().__init__(n, cn, difficulty, type, attempts)

    def fetch_problems(self):
        out = []
        for q in range(self.n):
            next = self.randomized_problem(self.cn, self.difficulty)
            out.append(next)
        return out

    def randomized_problem(self, choices, difficulty):
        nQ = len(QUESTIONS_3)
        ind = random.randint(0, nQ)
        q = QUESTIONS_3[ind]
        a = ANSWERS_3[ind]
        cor = a[0]
        random.shuffle(a)
        correct_index = a.index(cor)
        if self.type == "definition":
            question = DefinitionExercise(q[0], choices, self.attempts)
            question.set_question(q[1], a, correct_index)
        return question
