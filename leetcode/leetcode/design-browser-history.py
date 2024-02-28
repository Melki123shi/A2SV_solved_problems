class Node:
    def __init__(self, val, prev = None, next = None):
        self.prev = prev
        self.next = next 
        self.val = val

class BrowserHistory:

    def __init__(self, homepage: str):
        self.dummy = Node(0)
        self.head = Node(homepage)
        self.dummy.next = self.head
        self.currPage = self.head

    def visit(self, url: str) -> None:
        newNode = Node(url)
        if self.currPage.next:
            self.currPage.next.prev = None

        self.currPage.next = newNode
        newNode.prev = self.currPage
        self.currPage = newNode

    def back(self, steps: int) -> str:
        while steps and self.currPage and self.currPage.prev:
            self.currPage = self.currPage.prev
            steps -= 1
        
        return self.currPage.val
        
    def forward(self, steps: int) -> str:
        while steps and self.currPage and self.currPage.next:
            self.currPage = self.currPage.next
            steps -= 1
        
        return self.currPage.val
        
    



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)