from entities.exercise import DefinitionExercise
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
        difficulty:
            Merkkijonoarvo, joka kuvaa kysymysten vaikeustasoa.
        type:
            Merkkijonoarvo, joka kuvaa kysymysten tyyppiä.
    """

    def __init__(self, structure, type, difficulty):
        """Luokan konstruktori, joka luo uuden kysymysgeneraattorin.

        Args:
            difficulty:
                Merkkijonoarvo, joka kuvaa kysymysten vaikeustasoa.
            type:
                Merkkijonoarvo, joka kuvaa kysymysten tyyppiä.
        """
        self.difficulty = difficulty
        self.type = type

    def fetch_problems(self, n):
        """ Metodi, joka palauttaa kirjaston generoituja kysymyksiä."""

        out = []
        for q in range(n):  # pylint: disable=unused-variable
            new_problem = self.fetch_problem()
            out.append(new_problem)
        return out

    def fetch_problem(self):
        return DefinitionExercise("kysymys",
                                  ["ok", "a", "b", "c", 1],
                                  "easy"
                                  )