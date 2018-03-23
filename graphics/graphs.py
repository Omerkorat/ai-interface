"""Classes that define graphs."""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class MovingGraph:
    def __init__(self, linestyle="-", color="b", x_tickers=[], y_tickers=[],
                 func=np.sin, frequency=12, amplitude=.3, smoothness=.001, speed=.4):
        """
        :param linestyle: Straight, dashed, etc'.
        :param color: COlor of the line.
        :param x_tickers: The labels on the x axis.
        :param y_tickers: The labels on the y axis.
        :param func: The transformation applied to the x values to create the 2D function.
        :param frequency: Wave frequency. Higher values means more waves (or whatever is the right term).
        :param wavelength: How high the peak of the wave goes. Higher value means goes higher.
        :param smoothness: How smooth is the line when it curves. Change this value only if you know what you're
        doing. Basically, if you set it greater than 1, it will give you lines that break abruptly.
        :param speed: How fast the wave goes.
        """


        self.function = func
        self.amplitude = amplitude
        self.speed=speed
        self.fig, ax = plt.subplots()
        ax.set_yticklabels(y_tickers)
        ax.set_xticklabels(x_tickers)
        self.x = np.arange(0, frequency * np.pi, smoothness)
        self.line, = ax.plot(self.x, self.function(self.x), linestyle=linestyle, color=color)

    def updage(self, i):
        """This function updates the graph. It is called in a loop
        to create the animation."""
        self.line.set_ydata(self.function(self.x + i * self.speed) * self.amplitude)  # update the data
        return self.line,

    def init(self):
        """The function that starts the graph. This is the initial state."""
        self.line.set_ydata(np.ma.array(self.x, mask=True))
        return self.line,

    def show(self):
        """Runs the animation."""
        ani = animation.FuncAnimation(self.fig, self.updage, np.arange(1, 50), init_func=self.init,
                                      interval=25, blit=True)
        plt.show()
