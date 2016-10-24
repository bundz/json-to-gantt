class Bar:
    def __init__(self, bar):
        self.row = bar["row"]
        self.start = bar["from"]
        self.to = bar["to"]
        self.width = self.to - self.start
        self.color = bar["color"]