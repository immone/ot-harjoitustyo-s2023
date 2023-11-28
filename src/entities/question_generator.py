from src.entities.exercise import DefinitionExercise
# Refaktoroi johonkin järkevämpään paikkaan

QUESTIONS = [
            ["Associativity, an inverse element under an operation and a neutral element",
             "Commutativity, an inverse element under an operation and a neutral element",
             "Distributivity, an inverse element under an operation and a neutral element"]
]

MOCK_YAML = {"id": {"difficulty": "Easy",
                    "description": "Group definition",
                    "correct": 0,
                    "attempts": 2,
                    'hint':   "You don't need one.",
                    "options": QUESTIONS,
                    "question": "What is included in the definition of a group?",
                    "id": 1337
                    }
             }


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

    def __init__(self, n, cn, difficulty, description, attempts):
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
        self.description = description
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

    def __init__(self, n, cn, difficulty, description, attempts): # pylint: disable=useless-parent-delegation
        """ Luokan konstruktori, joka luo uuden monivalintatehtävän.
        """
        super().__init__(n, cn, difficulty, description, attempts)

    def fetch_problems(self):
        out = []
        for q in range(self.n): # pylint: disable=unused-variable
            new_problem = self.randomized_problem(self.cn, self.difficulty)
            out.append(new_problem)
        return out

    def randomized_problem(self, choices, difficulty):
        ex = MOCK_YAML['id']
        options = ex['options']
        question = ex['question']
        correct = ex['correct']
        new_exercise = DefinitionExercise(ex['description'],
                                          ex['attempts'],
                                          ex['difficulty'],
                                          ex['hint'],
                                          ex['id']
                                          ) # pylint: disable=duplicate-code
        new_exercise.set_question(question, options, correct)
        return question
