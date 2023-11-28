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
        self._create_exercise_entry = None
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
            self._handle_set_exercise_done()
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
            sticky=constants.EW
        )

    def _handle_create_todo(self):
        ex_content = self._create_exercise_entry.get()

        if ex_content:
            exercise_service.create_exe(ex_content)
            self._initialize_exercises()
            self._create_exercise_entry.delete(0, constants.END)

    def _initialize_footer(self):
        self._create_exercise_entry = ttk.Entry(master=self._frame)

        create_todo_button = ttk.Button(
            master=self._frame,
            text="Create",
            command=self._handle_create_todo
        )

        self._create_exercise_entry.grid(
            row=2,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        create_todo_button.grid(
            row=2,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._todo_list_frame = ttk.Frame(master=self._frame)

        self._initialize_header()
        self._initialize_exercises()
        self._initialize_footer()

        self._todo_list_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)
