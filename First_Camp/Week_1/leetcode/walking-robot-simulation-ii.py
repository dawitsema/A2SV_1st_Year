class Robot:

    def __init__(self, width: int, height: int):
        self.width = width - 1
        self.height = height - 1
        self.mod = 2 * (self.width + self.height)
        self.position = 0
        self.moved = False

    def step(self, num: int) -> None:
        self.moved = True
        self.position = (self.position + num) % self.mod
        
    def getPos(self) -> List[int]:
        pos = self.position
        if pos <= self.width:
            return [pos, 0]
        pos -= self.width
        if pos <= self.height:
            return [self.width, pos]
        pos -= self.height
        if pos <= self.width:
            return [self.width - pos, self.height]
        pos -= self.width
        return [0, self.height - pos]
            
    def getDir(self) -> str:
        pos = self.position
        if pos == 0:
            return 'South' if self.moved else 'East'
        if pos <= self.width:
            return 'East'
        pos -= self.width
        if pos <= self.height:
            return 'North'
        pos -= self.height
        if pos <= self.width:
            return 'West'
        return 'South'