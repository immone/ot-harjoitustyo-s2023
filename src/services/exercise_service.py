from entities.exercise import Exercise
from repositories.exercise_repository import ex_repository as default_exercise_repository

class ExerciseService:
    """ Sovelluslogiikassa käyttöliittymän ja tehtävien tietokannan välisestä kommunikaatiosta
        vastaava luokka.
     """

    def __init__(self, exercise_repository=default_exercise_repository):
        """Luokan konstruktori. Luo uuden sovelluslogiikasta vastaavan palvelun.

        Args:
            exercise_repository:
                Vapaaehtoinen, oletusarvoltaan default ExerciseRepository-olio.
                Olio, jolla on ExerciseRepository-luokkaa vastaavat metodit.
            user_repository:
                Vapaaehtoinen, oletusarvoltaan UserRepository-olio.
                Olio, jolla on UserRepository-luokkaa vastaavat metodit.
        """
        self._user = None
        self._exercise_repository = exercise_repository

    def create_exercise(self, description, attempts, hint=None, game=None, ex_id=None):
        """Luo uuden tehtävän.

        Args:
            description:
                Merkkijonoarvo, joka kuvaa tehtävää.
            attempts:
                 Yksityinen.
                 Kokonaislukuarvo, joka kuvaa yritysten määrää.
           hint:
                Vapaaehtoinen, oletusarvoltaan None.
                Merkkijonoarvo, joka on tehtäväkohtainen vihje.
            game:
                Vapaaehtoinen, oletusarvoltaan None.
                Game-olio, joka kuvaa peliä johon tehtävä kuuluu.
            ex_id:
                Vapaaehtoinen, oletusarvoltaan generoitu uuid.
                Merkkijonoarvo, joku kuvaa tehtävän id:tä.

        Returns:
            Luotu tehtävä Exercise-olion muodossa.
        """

        return self._exercise_repository.create(exercise)



exercise_service = ExerciseService()
