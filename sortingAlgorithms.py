DEFAULT_HEIGHT_MULTIPLIER = 20
class SortingAlgorithms:
    # the drawing and colouring aspects can probably be put in their own class, WIP as currently only one sort implemented
    @staticmethod
    def bubbleSort(root, bars):
        sorted = False
        while not sorted:
            sorted = True
            for i in range(len(bars) -1):
                if (bars[i].height > bars[i+1].height):
                    sorted = False
                    temp = bars[i]
                    bars[i] = bars[i+1]
                    bars[i+1] = temp
                    root.sortingArea.delete(f"{bars[i].height / DEFAULT_HEIGHT_MULTIPLIER}")
                    root.sortingArea.delete(f"{bars[i+1].height / DEFAULT_HEIGHT_MULTIPLIER}")
                    root.sortingArea.create_rectangle(i*(root.bars[i].width), 
                                                        root.sortingArea.winfo_height() - root.bars[i].height, 
                                                        i*(root.bars[i].width) + root.bars[i].width, 
                                                        root.sortingArea.winfo_height(),
                                                        fill="red",
                                                        tags=(f"{root.bars[i].height / DEFAULT_HEIGHT_MULTIPLIER}", "RECT"))
                    root.sortingArea.itemconfig("RECT", fill="white")
                    root.sortingArea.create_rectangle((i+1)*(root.bars[(i+1)].width), 
                                                        root.sortingArea.winfo_height() - root.bars[(i+1)].height, 
                                                        (i+1)*(root.bars[(i+1)].width) + root.bars[(i+1)].width, 
                                                        root.sortingArea.winfo_height(),
                                                        fill="red",
                                                        tags=(f"{root.bars[(i+1)].height / DEFAULT_HEIGHT_MULTIPLIER}", "RECT"))
                root.after(10, None)
                root.sortingArea.update()
        root.sortingArea.itemconfig("RECT", fill="white")
        for bar in bars:
            root.sortingArea.itemconfig(f"{bar.height / DEFAULT_HEIGHT_MULTIPLIER}", fill="green")
            root.sortingArea.update()
            root.after(10, None)
        root.after(1000, None)
        root.sortingArea.itemconfig("RECT", fill="white")
        return bars
            


    @staticmethod
    def mergeSort():
        pass
    
    @staticmethod
    def insertionSort():
        pass

    @staticmethod
    def quickSort():
        pass

    @staticmethod
    def randomSort():
        pass
    