from ui.exercise_view import ExerciseView
from ui.login_view import LoginView
from ui.choose_difficulty_view import ChooseDifficultyView
from ui.game_view import GameView


class UI:
    """Sovelluksen käyttöliittymästä vastaava luokka."""

    def __init__(self, root):
        """Luokan konstruktori. Luo uuden käyttöliittymästä vastaavan olion.

        Args:
            root:
                TKinter-olio, johon näkymä luodaan.
        """
        self._root = root
        self._current_view = None

    def start(self):
        """Käynnistää käyttöliittymän."""
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._show_exercise_view,
            self._show_choose_difficulty_view,
            self._show_login_view
        )

        self._current_view.pack()

    def _show_exercise_view(self):
        self._hide_current_view()

        self._current_view = ExerciseView(
            self._root, self._show_login_view, self._show_game_view)

        self._current_view.pack()

    def _show_choose_difficulty_view(self):
        self._hide_current_view()

        self._current_view = ChooseDifficultyView(
            self._root,
            self._show_exercise_view,
            self._show_login_view
        )

        self._current_view.pack()

    def _show_game_view(self):
        self._hide_current_view()

        self._current_view = GameView(
            self._root, self._show_choose_difficulty_view)

        self._current_view.pack()
