import tkinter as tk
from tkinter import messagebox
from bar import Bar
from sortingAlgorithms import SortingAlgorithms
import random

DEFAULT_BAR_COUNT = 30
DEFAULT_HEIGHT_MULTIPLIER = 20

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sorting Visualiser")
        self.geometry("1200x800")
        self.resizable(False, False)
        self.bars = []
        self.barCount = DEFAULT_BAR_COUNT
        self.sortingArea = tk.Canvas(self, width=800, height=800, bg="black")
        self.sortingArea.place(relx=1, rely=0, anchor="ne")
        self.settingsFrame = tk.Frame(self, bg="grey", width=400, height=800)
        self.settingsFrame.place(relx=0,rely=0, anchor="nw")
        self.createSettings()
        self.createBars()

    
    def createBars(self, value=None):
        self.bars = []
        self.sortingArea.delete("all")
        self.barCount = self.barsSlider.get()
        for i in range(1, self.barCount +1): # starts at 1 to prevent 0 height
            self.bars.append(Bar(i, self.barCount))
        random.shuffle(self.bars)
        for j in range(self.barCount):
            self.sortingArea.create_rectangle(j*(self.bars[j].width), 
                                              self.sortingArea.winfo_height() - self.bars[j].height, 
                                              j*(self.bars[j].width) + self.bars[j].width, 
                                              self.sortingArea.winfo_height(),
                                            fill="white",
                                            tags=(f"{self.bars[j].height / DEFAULT_HEIGHT_MULTIPLIER}", "RECT"))
            

    def createSettings(self):
        tk.Label(self.settingsFrame, text="Number Of Bars:", bg="grey").place(relx=0.5, rely=0.01, anchor="center")
        self.barsSlider = tk.Scale(self.settingsFrame, from_=0, to=300, orient=tk.HORIZONTAL, command=self.createBars, bg="grey", bd=0, highlightthickness=0)
        self.barsSlider.set(DEFAULT_BAR_COUNT)
        self.barsSlider.place(relx=0, rely=0.02, anchor="nw", relwidth=1)
        self.update_idletasks() # calls this to allow proper fitting, heights messed up otherwise
        self.shuffleButton = tk.Button(self.settingsFrame, text="Shuffle", command=self.createBars, bg="grey")
        self.shuffleButton.place(relx=0, rely=0.02 + (self.barsSlider.winfo_height() / self.settingsFrame.winfo_height()), anchor="nw", relwidth=1)
        self.sortButton = tk.Button(self.settingsFrame, text="Sort", bg="grey", command=self.startSort)
        self.sortButton.place(relx=0, rely=1, anchor="sw", relwidth=1)


    def startSort(self):
        # this is currently a placeholder, colouring and audio are not implemented, WIP
        self.bars = SortingAlgorithms.bubbleSort(self, self.bars)
        """for j in range(self.barCount):
            self.sortingArea.create_rectangle(j*(self.bars[j].width), 
                                              self.sortingArea.winfo_height() - self.bars[j].height, 
                                              j*(self.bars[j].width) + self.bars[j].width, 
                                              self.sortingArea.winfo_height(),
                                            fill="white",
                                            tags=f"{self.bars[j].height / DEFAULT_HEIGHT_MULTIPLIER}")"""



def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()