import time


class Timer:
    """
    Class for tracking the time
    """
    def __init__(self):
        self.timer = {0: 0.0}

    def start(self, num_of_timer: [int, str] = 0) -> None:
        """
        Start new timer
        :param num_of_timer: str\int - name of the timer
        :return:
        """
        self.timer[num_of_timer] = time.time()

    def stop(self, num_of_timer: [int, str] = 0) -> float:
        """
        Check spent time for specific timer
        :param num_of_timer: str\int - name of the timer
        :return: float - (seconds) how many seconds spent from the start
        """
        return time.time() - self.timer[num_of_timer]
