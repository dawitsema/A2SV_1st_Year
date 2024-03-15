class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.stack = [homepage]  
        self.pt = 0  

    def visit(self, url: str) -> None:
        self.stack = self.stack[:self.pt + 1]
        self.stack.append(url)
        self.pt += 1

    def back(self, steps: int) -> str:
        self.pt = max(0, self.pt - steps)  
        return self.stack[self.pt]

    def forward(self, steps: int) -> str:
        self.pt = min(len(self.stack) - 1, self.pt + steps)  
        return self.stack[self.pt]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
