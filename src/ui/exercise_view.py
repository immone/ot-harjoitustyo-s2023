import tkinter as tk
from tkinter import ttk, constants
from services.exercise_service import exercise_service
from ui.game_view import GameView

class ExerciseView:
    """Tehtävien listauksesta ja lisäämisestä vastaava näkymä."""

    def __init__(self, root, handle_logout):
        """Luokan konstruktori. Luo uuden tehtävänäkymän.

        Args:
            root:
                TKinter-elementti, jonka sisään näkymä alustetaan.
            handle_logout:
                Kutsuttava-arvo, jota kutsutaan kun käyttäjä kirjautuu ulos.
        """
        self._root = root
        self._handle_logout = handle_logout
        self._user = exercise_service.get_current_user()
        self._frame = None
        self._type_variable = None
        self._structure_variable = None
        self._exercise_list_frame = None
        self._exercise_list_view = None

        self._initialize()

    def pack(self):
        """"Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """"Tuhoaa näkymän."""
        self._frame.destroy()

    def _logout_handler(self):
        exercise_service.logout()
        self._handle_logout()

    def _handle_set_exercise_done(self, id):
        exercise_service.set_exercise_done(id)
        self._initialize_exercises()

    def _initialize_exercises(self):
        if self._exercise_list_view:
            self._exercise_list_view.destroy()

        exercises = exercise_service.get_undone_exercises()

        self._exercise_list_view = GameView(
            self._exercise_list_frame,
            exercises,
            self._handle_set_exercise_done
        )

        self._exercise_list_view.pack()

    def _initialize_header(self):
        user_label = ttk.Label(
            master=self._frame,
            text=f"Logged in as {self._user.username}"
        )

        logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._logout_handler
        )

        user_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        logout_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.N
        )

    def _handle_create_exercise(self):
        type = self._type_variable.get()
        structure = self._structure_variable.get()

        if type and structure:
            exercise_service.create_exercises(type, structure)
            self._initialize_exercises()
            self._type_variable.delete(0, constants.END)

    def _initialize_footer(self):
        self._type_variable = tk.StringVar()
        self._structure_variable = tk.StringVar()

        type_label = ttk.Label(self._frame, text="Algebraic structure")
        type_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
        group = ttk.Radiobutton(master=self._frame,
                               text='Group',
                               var=self._structure_variable,
                               value='group')

        ring = ttk.Radiobutton(master=self._frame,
                                text='Ring',
                                var=self._structure_variable,
                                value='ring')

        field = ttk.Radiobutton(master=self._frame,
                               text='Field',
                               var=self._structure_variable,
                               value='field')

        ring.grid(row=1, column=0, padx=10, pady=10,sticky=constants.W)
        group.grid(row=2, column=0, padx=10, pady=10,sticky=constants.W)
        field.grid(row=3, column=0, padx=10, pady=10,sticky=constants.W)

        question_label = ttk.Label(self._frame, text="Question type")
        question_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.N)
        definition = ttk.Radiobutton(master=self._frame,
                                text='Definition',
                                var=self._type_variable,
                                value='def')

        problem = ttk.Radiobutton(master=self._frame,
                               text='Problem',
                               var=self._type_variable,
                               value='prob')

        theorem = ttk.Radiobutton(master=self._frame,
                                text='Theorem',
                                var=self._type_variable,
                                value='theorem')

        definition.grid(row=1, column=0, padx=10, pady=10, sticky=constants.N)
        problem.grid(row=2, column=0, padx=10, pady=10, sticky=constants.N)
        theorem.grid(row=3, column=0, padx=10, pady=10, sticky=constants.N)

        create_exercise_button = ttk.Button(
            master=self._frame,
            text="Start",
            command=self._handle_create_exercise
        )

        create_exercise_button.grid(
            row=3,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.S
        )

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._exercise_list_frame = ttk.Frame(master=self._frame)

        self._initialize_header()
        self._initialize_exercises()
        self._initialize_footer()

        self._exercise_list_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)
