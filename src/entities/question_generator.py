import random
from entities.exercise import DefinitionExercise, TheoremExercise, ProblemExercise
from repositories.exercise_repository import ex_repository


class QuestionGenerator:
    """Luokka, joka generoi tehtäväkysymyset.

    Attributes:
        difficulty:
            Merkkijonoarvo, joka kuvaa kysymysten vaikeustasoa.
        type:
            Merkkijonoarvo, joka kuvaa kysymysten tyyppiä.
        structure:
            Kysymyksien tyyppi.
    """

    def __init__(self, ex_type, difficulty, structure):
        """Luokan konstruktori, joka luo uuden kysymysgeneraattorin.

        Args:
            difficulty:
                Merkkijonoarvo, joka kuvaa kysymysten vaikeustasoa.
            type:
                Merkkijonoarvo, joka kuvaa kysymysten tyyppiä.
        """
        self.difficulty = difficulty
        self.type = ex_type
        self.structure = structure

    def fetch_problems(self, n):
        """ Metodi, joka palauttaa parametrin n osoittaman
            kokoisen listan satunnaisesti generoituja kysymyksiä.
        """

        if self.type == 'definition':
            q_type = DefinitionExercise
        elif self.type == 'theorem':
            q_type = TheoremExercise
        else:
            q_type = ProblemExercise

        out = []
        exercises = ex_repository.find_all_by_difficulty(self.difficulty)
        n = min(n, len(exercises))
        for e in exercises:
            if type(e) == q_type and e.structure == self.structure:
                out.append(e)
        random.shuffle(out)
        print(out)
        return out[0:n]
