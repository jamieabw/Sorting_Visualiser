import random
DEFAULT_HEIGHT_MULTIPLIER = 20
class SortingAlgorithms:
    # the drawing and colouring aspects can probably be put in their own class, WIP 
    @staticmethod
    def bubbleSort(root, bars, speed, i=0, j=0):
        barsLength = len(bars)
        if i < barsLength - 1:
            if j < barsLength - i - 1:
                if bars[j].height > bars[j+1].height:
                    bars[j], bars[j+1] = bars[j+1], bars[j]

                root.sortingArea.delete("all")
                for idx, bar in enumerate(bars):
                    root.sortingArea.create_rectangle(
                        idx * bar.width,
                        root.sortingArea.winfo_height() - bar.height,
                        idx * bar.width + bar.width,
                        root.sortingArea.winfo_height(),
                        fill="red" if idx == j or idx == j+1 else "white",
                        tags=(f"{bar.height / DEFAULT_HEIGHT_MULTIPLIER}", "RECT")
                    )

                root.after(speed, lambda: SortingAlgorithms.bubbleSort(root, bars, speed, i, j + 1))
            else:
                root.after(speed, lambda: SortingAlgorithms.bubbleSort(root, bars, speed, i + 1, 0))
        else:
            for i in range(len(bars)):  
                root.sortingArea.itemconfig(f"{bars[i].height / DEFAULT_HEIGHT_MULTIPLIER}", fill="green")
                root.sortingArea.update()
                root.after(10)
            root.after(1000)
            root.sortingArea.itemconfig("RECT", fill="white")
        return bars

            


    @staticmethod
    def mergeSort(root, bars, speed, i=1):
        def mergeStep(root, bars, speed, i, j):
            leftSide = bars[j:j+i]
            rightSide = bars[j+i:j + (i * 2)]
            mergedList = []
            lPointer, rPointer = 0, 0
            while lPointer < len(leftSide) and rPointer < len(rightSide):
                if leftSide[lPointer].height < rightSide[rPointer].height:
                    mergedList.append(leftSide[lPointer])
                    lPointer += 1
                else:
                    mergedList.append(rightSide[rPointer])
                    rPointer += 1
            mergedList.extend(leftSide[lPointer:])
            mergedList.extend(rightSide[rPointer:])
            for k in range(len(mergedList)):
                bars[j + k] = mergedList[k]

            root.sortingArea.delete("all")
            for idx, bar in enumerate(bars):
                root.sortingArea.create_rectangle(
                    idx * bar.width,
                    root.sortingArea.winfo_height() - bar.height,
                    idx * bar.width + bar.width,
                    root.sortingArea.winfo_height(),
                    fill="red" if j <= idx < j + len(mergedList) else "white",
                    tags=(f"{bar.height / DEFAULT_HEIGHT_MULTIPLIER}", "RECT"),
                )
            root.sortingArea.update()

            if j + i * 2 < len(bars):
                root.after(speed, lambda: mergeStep(root, bars, speed, i, j + i * 2))
            else:
                root.after(speed, lambda: SortingAlgorithms.mergeSort(root, bars, speed, i * 2))

        if i >= len(bars):
            root.sortingArea.delete("all")
            for idx, bar in enumerate(bars):
                root.sortingArea.create_rectangle(
                    idx * bar.width,
                    root.sortingArea.winfo_height() - bar.height,
                    idx * bar.width + bar.width,
                    root.sortingArea.winfo_height(),
                    tags=(f"{bar.height / DEFAULT_HEIGHT_MULTIPLIER}", "RECT"),
                    fill="white"
                )
            return SortingAlgorithms.endSort(root, bars, speed)

        root.after(speed, lambda: mergeStep(root, bars, speed, i, 0))
        if i==1: return bars

    @staticmethod
    def insertionSort(root, bars, speed, i=1, j=None):
        if i < len(bars):
            if j is None:
                j = i - 1
                key = bars[i]
                SortingAlgorithms.insertionSort(root, bars, speed, i, j)
                return

            if j >= 0 and bars[j].height > bars[j + 1].height:
                bars[j + 1], bars[j] = bars[j], bars[j + 1]
                root.sortingArea.delete("all")
                for idx, bar in enumerate(bars):
                    root.sortingArea.create_rectangle(
                        idx * bar.width,
                        root.sortingArea.winfo_height() - bar.height,
                        idx * bar.width + bar.width,
                        root.sortingArea.winfo_height(),
                        tags=(f"{bar.height / DEFAULT_HEIGHT_MULTIPLIER}", "RECT"),
                        fill="white"
                    )
                root.sortingArea.itemconfig(f"{bars[j].height / DEFAULT_HEIGHT_MULTIPLIER}", fill="red")
                root.sortingArea.itemconfig(f"{bars[j+1].height / DEFAULT_HEIGHT_MULTIPLIER}", fill="red")

                root.sortingArea.update()
                root.after(speed, SortingAlgorithms.insertionSort, root, bars, speed, i, j - 1)
            else:
                root.after(speed, SortingAlgorithms.insertionSort, root, bars, speed, i + 1)
        else:
            return SortingAlgorithms.endSort(root, bars, speed)
        
    


        
        

    @staticmethod
    def quickSort():
        pass

    @staticmethod
    def bogoSort(root, bars, speed):
        sorted = False
        while not sorted:
            random.shuffle(bars)
            root.sortingArea.delete("all")
            for idx, bar in enumerate(bars):
                root.sortingArea.create_rectangle(
                idx * bar.width,
                root.sortingArea.winfo_height() - bar.height,
                idx * bar.width + bar.width,
                root.sortingArea.winfo_height(),
                tags=(f"{bar.height / DEFAULT_HEIGHT_MULTIPLIER}", "RECT")
                    )
            root.sortingArea.itemconfig("RECT", fill="red")
            root.sortingArea.update()
            root.after(speed)
            root.sortingArea.itemconfig("RECT", fill="white")
            sorted = True
            for i in range(len(bars) -1):
                if bars[i].height > bars[i+1].height:
                    sorted = False
                    break
            root.sortingArea.update()
        return SortingAlgorithms.endSort(root, bars, speed)
    

    @staticmethod
    def endSort(root, bars, speed):
        for i in range(len(bars)):  
            root.sortingArea.itemconfig(f"{bars[i].height / DEFAULT_HEIGHT_MULTIPLIER}", fill="green")
            root.sortingArea.update()
            root.after(10)
        root.after(1000)
        root.sortingArea.itemconfig("RECT", fill="white")
        return bars



    