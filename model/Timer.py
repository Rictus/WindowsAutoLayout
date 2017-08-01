import time

# TODO : N'instancier cette classe que s'il y a plus d'une fenêtres
# et s'il y a plus d'une fenêtres visible
#
class Timer:
    def __init__(self, windows):
        """
        :param windows: List of Window
        :return:
        """
        self._start_timer()
        self.windows = windows

    def _start_timer(self):
        self.start = time.clock()

    def _update_timer(self):
        self.time_spent = time.clock() - self.start

    def alert(self):
        """
        Alert the user if he want to save the current layout
        :return:
        """
        print("You've been using this layout of windows since a while now."
              "You can save it to easily retrieve this layout later.")
        agree_to_save = input("Type Y to save it. Anything else to quit.")
        if agree_to_save == "Y":
            self.save_layout()

    def update(self):
        """
        Update the timer
        If the time spent is significant, alert the user
        :return:
        """
        self._update_timer()
        limit = 100  # TODO
        if self.time_spent > limit:
            self.alert()

    def save_layout(self):
        """
         Save the layout
        :return:
        """
        print("Let's save your layout ! (When this feature will be developed)")
