from config import Config

class TM:
    """
    TM for Turing Machine represents a Turing Machine code
    Computes for a given configuration the next step.s
    """
    def __init__(self, name: str, nb_states: int, states: list, nb_tapes: int, transi_list: list):
        self.name = name
        self.nb_state = nb_states
        self.states = states
        self.nb_tapes = nb_tapes
        self.transi_list = transi_list

    def __str__(self):
        s =f"Name : {self.name} \n"
        s += f"Number of states : {self.nb_states} \n"
        for i in range(len(self.states)):
            s += f"\t - {self.states[i]}"
        s += f"Number of tape.s : {self.nb_tapes} \n"
        for i in range(len(self.transi_list)):
            s+= f"\t - {self.transi_list[i]} \n"
        return s

    def next_step(self, conf):
        """
        Given a Config, returns the new Config following the machine rules
        """
        pass

    def run(self, conf):
        """
        Given a Config, computes all Config until end of program (q = 1) and returns the last Config
        """
        pass

    def run_print(self, conf):
        """
        Given a Config, computes all Config until end of program (q = 1) and returns the last Config
        Also prints out in a pretty manner how it works
        """
        pass

    @staticmethod
    def load_from_file(filepath: str):
        pass

    def create_init_config(self, input_):
        """
        Creates a Config using the input_, and gives it the good amount of tapes
        """
        pass


if __name__ == '__main__':
    tm = TM("toto", 1, [0], 3, [])
    print(tm)