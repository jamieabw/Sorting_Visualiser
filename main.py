import tkinter as tk
from tkinter import messagebox
from bar import Bar
from sortingAlgorithms import SortingAlgorithms
import random
import threading

DEFAULT_BAR_COUNT = 30
DEFAULT_HEIGHT_MULTIPLIER = 20

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sorting Visualiser")
        self.geometry("1200x800")
        self.resizable(False, False)
        self.bars = []
        self.speed = 10
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
        self.sortButton = tk.Button(self.settingsFrame, text="Sort", bg="grey", command=self.startSort)
        self.sortButton.place(relx=0, rely=1, anchor="sw", relwidth=1)
        self.update_idletasks() # calls this to allow proper fitting, heights messed up otherwise
        self.shuffleButton = tk.Button(self.settingsFrame, text="Shuffle", command=self.createBars, bg="grey")
        self.shuffleButton.place(relx=0, rely=1 - (self.sortButton.winfo_height() / self.settingsFrame.winfo_height()), anchor="sw", relwidth=1)
        tk.Label(self.settingsFrame, text="Speed Of Sort:", bg="grey").place(relx=0.5, rely=0.1, anchor="center")
        self.speedSlider = tk.Scale(self.settingsFrame, from_=1, to=1000, orient="horizontal", command=self.setSpeed, bg="grey", bd=0, highlightthickness=0)
        self.speedSlider.place(relx=0,
                                rely=0.08 + (self.barsSlider.winfo_height() / self.settingsFrame.winfo_height()), anchor="nw", relwidth=1)
        

        self.sortSelected = tk.StringVar()
        self.sortSelected.set("Bubble Sort")
        self.sortChoices = ["Bubble Sort", "Insertion Sort", "Bogo Sort", "Merge Sort", "Quick Sort"]
        self.sortSelection = tk.OptionMenu(self.settingsFrame, self.sortSelected, *self.sortChoices)
        self.sortSelection.config(bg="grey", bd=1, highlightthickness=0)
        self.sortSelection.place(relx=0, rely=0.5, relwidth=1)
        
    def setSpeed(self, value=None):
        self.speed = int(1000 / self.speedSlider.get())



    def startSort(self):
        # this is currently a placeholder, colouring and audio are not implemented, WIP
        match self.sortSelected.get():
            case "Bubble Sort":
                self.bars = SortingAlgorithms.bubbleSort(self, self.bars, self.speed)
            case "Insertion Sort":
                self.bars = SortingAlgorithms.insertionSort(self, self.bars, self.speed)
            case "Bogo Sort":
                self.bars = SortingAlgorithms.bogoSort(self, self.bars, self.speed)
            case "Merge Sort":
                pass
            case "Quick Sort":
                pass

        



def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()