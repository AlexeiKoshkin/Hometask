class Home:
    def __init__(self, square, floor):
        self.square = square
        self.floor = floor
    def open(self):
        print("Открыть окна")
    def close(self):
        print("Закрыть окна")

dom1 = Home(1000, 5)
print(dom1.square)
print(dom1.floor)
dom1.open()
dom1.close()

dom2 = Home(5000, 25)
print(dom2.square)
print(dom2.floor)
dom2.open()
dom2.close()