import tkinter as tk
from tkinter import ttk, constants
from services.game_service import game_service


class ProblemListView:
    """Tehtävien listauksesta vastaava näkymä."""

    def __init__(self, root, exercises, handle_set_ex_done):
        """Luokan konstruktori. Luo uuden tehtävälistausnäkymän.

        Args:
            root:
                TKinter-elementti, jonka sisään näkymä alustetaan.
            todos:
                Lista Exercise-olioita, jotka näkymässä näytetään
            handle_set_todo_done:
                Kutsuttava-arvo, jota kutsutaan kun tehtävä valmistuu. Saa argumentiksi valmistuneen tehtävän id-arvon.
        """

        self._root = root
        self._exercises = exercises
        self._handle_set_ex_done = handle_set_ex_done

        self._answer_variable = None
        self._frame = None

        self._initialize()

    def pack(self):
        """"Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """"Tuhoaa näkymän."""
        self._frame.destroy()

    def feedback(self, t):
        secondary_window = tk.Toplevel()
        secondary_window.title("Feedback")
        secondary_window.config(width=100, height=30)
        # Create a button to close (destroy) this window.
        button_close = ttk.Button(
            secondary_window,
            text=t,
            command=secondary_window.destroy
        )
        button_close.place(x=0, y=0)
        secondary_window.focus()

    def _handle_problem_window(self, exercise):
        problem_window = tk.Toplevel(self._root)
        problem_window.title(f"{exercise.description}")
        problem_window.config(width=300, height=200)

        self._answer_variable = tk.StringVar()

        type_label = ttk.Label(problem_window, text=f"{exercise.question}")
        type_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.E)
        a = 1
        for opt in exercise.options:
            next = ttk.Radiobutton(master=problem_window,
                                   text=f"{opt}",
                                   var=self._answer_variable,
                                   value=a)

            next.grid(row=a, column=0, padx=10, pady=10, sticky=constants.E)
            a += 1

        def handle_answer():
            user_answer = self._answer_variable.get()
            if user_answer:
                if int(user_answer) == (exercise.answer+1):
                    game_service.increase_points()
                    self.feedback("Correct!")
                else:
                    self.feedback("Wrong!")
            problem_window.destroy()
            self._handle_set_ex_done(exercise.id)

        check_answer = ttk.Button(
            master=problem_window,
            text="Check",
            command=handle_answer
        )

        check_answer.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        close_button = ttk.Button(
            master=problem_window,
            text="Close",
            command=problem_window.destroy
        )

        close_button.grid(
            row=3,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _initialize_exercise(self, ex):
        item_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(master=item_frame, text=ex.description)

        set_done_button = ttk.Button(
            master=item_frame,
            text="Choose",
            command=lambda: self._handle_problem_window(ex)
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


class GameView:
    """Tehtävien listauksesta vastaava näkymä."""

    def __init__(self, root, handle_go_to_login_view):
        """Luokan konstruktori. Luo uuden tehtävänäkymän.

        Args:
            root:
                TKinter-elementti, jonka sisään näkymä alustetaan.
            exercises:
                Lista Exercises-olioita, jotka näkymässä näytetään
            handle_set_exercise_done:
                Kutsuttava arvo, jota kutsutaan kun Exercise-olion sisältämä tehtävä
                valmistuu. Saa argumentiksi valmistuneen tehtävän id-arvon.
        """

        self._root = root
        self._exercises = game_service.get_exercises()
        self._handle_go_to_login_view = handle_go_to_login_view
        self._handle_choose_exercise = None
        self._exercise_list_view = None
        self._exercise_list_frame = None
        self._frame = None
        self._initialize()

    def pack(self):
        """"Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def refresh_points(self):
        correct_label = ttk.Label(
            self._frame, text=f"{game_service.correct()}/{game_service.answered()} correct")
        correct_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.E)

    def destroy(self):
        """"Tuhoaa näkymän."""
        self._frame.destroy()

    def _handle_set_ex_done(self, ex_id):
        game_service.set_exercise_done(ex_id)
        self._initialize_exercises()

    def _initialize_exercises(self):
        if self._exercise_list_view:
            self._exercise_list_view.destroy()

        exercises = game_service.get_undone_exercises()
        self.refresh_points()

        self._exercise_list_view = ProblemListView(
            self._exercise_list_frame,
            exercises,
            self._handle_set_ex_done
        )

        self._exercise_list_view.pack()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._exercise_list_frame = ttk.Frame(master=self._frame)
        correct_label = ttk.Label(
            self._frame, text=f"{game_service.correct()}/{game_service.answered()} correct")
        correct_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.E)

        self._initialize_exercises()

        self._exercise_list_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)
