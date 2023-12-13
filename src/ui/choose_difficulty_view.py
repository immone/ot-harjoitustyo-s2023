import tkinter as tk
from tkinter import ttk, StringVar, constants
from services.user_service import user_service
from services.game_service import game_service


class ChooseDifficultyView:
    """Käyttäjän vaikeustason valitsemisesta vastaava näkymä."""

    def __init__(self, root, handle_choose_difficulty, handle_logout):
        """Luokan konstruktori. Luo uuden rekisteröitymisnäkymän.

        Args:
            root:
                TKinter-elementti, jonka sisään näkymä alustetaan.
            handle_show_login_view:
                Kutsuttava arvo, jota kutsutaan kun siirrytään takaisin kirjautumisnäkymään.
            handle_logout:
                Kutsuttava arvo, jota kutsutaan kun käyttäjä haluaa kirjautua ulos.
        """
        self._root = root
        self._user = user_service.get_current_user()
        self._handle_choose_difficulty = handle_choose_difficulty
        self._handle_logout = handle_logout
        self._frame = None
        self._error_label = None
        self._difficulty_variable = None

        self._initialize()

    def pack(self):
        """"Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def _logout_handler(self):
        game_service.logout()
        self._handle_logout()

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

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
            row=2,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _difficulty_handle(self):
        difficulty = self._difficulty_variable.get()
        if difficulty:
            self._user.update_skill(difficulty)
            self._handle_choose_difficulty()
        else:
            self._show_error("You have to choose a difficulty")
            return

    def _initialize_difficult_view(self):
        self._difficulty_variable = tk.StringVar()
        easy = ttk.Radiobutton(master=self._frame,
                                text='Easy',
                                var=self._difficulty_variable,
                                value='easy')

        hard = ttk.Radiobutton(master=self._frame,
                               text='Hard',
                               var=self._difficulty_variable,
                               value='Hard')

        easy.grid(row=0, column=0, padx=10, pady=10)
        hard.grid(row=1, column=0, padx=10, pady=10)

        choose_difficulty_button = ttk.Button(
            master=self._frame,
            text="Choose difficulty",
            command=self._difficulty_handle
        )
        choose_difficulty_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        self._error_label.grid(padx=5, pady=5)


        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        self._initialize_header()
        self._initialize_difficult_view()

        self._hide_error()