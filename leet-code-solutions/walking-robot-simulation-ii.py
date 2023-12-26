class Robot:

    def __init__(self, width: int, height: int):
       self.first = [(i, 0, 'East') for i in range(1, width)]
       self.second = [(width - 1, i, 'North') for i in range(1, height)]
       self.third = [(i, height - 1, 'West')  for i in range(width - 2, -1, -1)]
       self.fourth = [(0, i, 'South') for i in range(height - 2, 0, -1)]
       self.all = [(0,0,'South')] + self.first + self.second + self.third + self.fourth
       self.steping = 2*(width - 1) + 2*(height - 1)
       self.steps = 0

    def step(self, num: int) -> None:
        self.steps += num
          
    def getPos(self) -> List[int]:
        return self.all[(self.steps % self.steping)][:-1]
    def getDir(self) -> str:
        if self.steps == 0:
            return 'East'
        return self.all[(self.steps % self.steping)][-1]
        

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()