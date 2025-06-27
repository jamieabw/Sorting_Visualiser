import tkinter as tk
from tkinter import messagebox
from bar import Bar
from sortingAlgorithms import SortingAlgorithms
import random

DEFAULT_BAR_COUNT = 30

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sorting Visualiser")
        self.geometry("1200x800")
        self.bars = []
        self.barCount = DEFAULT_BAR_COUNT
        self.sortingArea = tk.Canvas(self, width=800, height=600, bg="black")
        self.sortingArea.pack()
        tk.Label(self, text="Number Of Bars:").pack()
        self.barsSlider = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL, command=self.createBars)
        self.barsSlider.set(DEFAULT_BAR_COUNT)
        self.createBars()
        self.barsSlider.pack()
        self.shuffleButton = tk.Button(self, text="Shuffle", command=self.createBars)
        self.shuffleButton.pack()

    
    def createBars(self, value=None):
        self.bars = []
        self.sortingArea.delete("all")
        self.barCount = self.barsSlider.get()
        for i in range(1, self.barCount +1): # starts at 1 to prevent 0 height
            self.bars.append(Bar(i, self.barCount))
        random.shuffle(self.bars)
        for j in range(self.barCount):
            self.sortingArea.create_rectangle(j*(self.bars[j].width), 
                                              600 - self.bars[j].height, 
                                              j*(self.bars[j].width) + self.bars[j].width, 
                                              600,
                                            fill="white")
        


def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()