DEFAULT_BAR_WIDTH = 20
DEFAULT_HEIGHT_MULTIPLIER = 20
SORTING_AREA_SIZE = 800



class Bar: # this will be the things that are getting sorted
    def __init__(self, position, numberOfBars):
        totalGap = numberOfBars -1
        heightMultiplier = 600 / numberOfBars
        self.width = ((SORTING_AREA_SIZE - totalGap) / numberOfBars) +1
        self.height = position * heightMultiplier
