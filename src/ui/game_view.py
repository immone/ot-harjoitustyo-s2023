import tkinter as tk
from tkinter import ttk, constants
from services.exercise_service import exercise_service


class GameView:
    """Tehtävien listauksesta vastaava näkymä."""

    def __init__(self, root, exercises, handle_set_exercise_done):
        """Luokan konstruktori. Luo uuden tehtävänäkymän.

        Args:
            root:
                TKinter-elementti, jonka sisään näkymä alustetaan.
            exercies:
                Lista Exercises-olioita, jotka näkymässä näytetään
            handle_set_exercise_done:
                Kutsuttava arvo, jota kutsutaan kun Exercise-olion sisältämä tehtävä
                valmistuu. Saa argumentiksi valmistuneen tehtävän id-arvon.
        """

        self._root = root
        self._exercises = exercises
        self._handle_set_exercise_done = handle_set_exercise_done
        self._frame = None

        self._initialize()

    def pack(self):
        """"Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """"Tuhoaa näkymän."""
        self._frame.destroy()

    def _initialize_exercise(self, exercise):
        item_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(master=item_frame, text=exercise.type)

        set_done_button = ttk.Button(
            master=item_frame,
            text="Done",
            command=lambda: self._handle_set_exercise_done(exercise.id)
        )

        label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        set_done_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for ex in self._exercises:
            self._initialize_exercise(ex)

