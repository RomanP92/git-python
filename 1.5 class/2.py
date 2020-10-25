class Buffer:
    def __init__(self):
        self.lst = []
        self.summ = 0
        

    def add(self, *a):
        self.lst += a
        return self.lst

        

    def get_current_part(self):
        while len(self.lst) >= 5:
            for i in self.lst[:5]:
                self.summ += i
            print(self.summ)
            self.summ = 0
            self.lst = self.lst[5:]
        return self.lst