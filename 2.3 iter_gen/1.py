class multifilter:
    def judge_half(pos, neg):
        return pos >= neg
        
    def judge_any(pos, neg):
        return pos >= 1

        
    def judge_all(pos, neg):
        return neg == 0

        
    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge
        self.j = 0
        self.i = 0
      
    def __iter__(self):
        return self

    def __next__(self):

        while len(self.iterable) > self.j:

            self.it = self.iterable[self.j]
            poz = 0
            neg = 0
            for f in self.funcs:
                if f(self.it):
                    poz += 1
                else:
                    neg += 1
            self.j += 1
            if self.judge(poz, neg):
                return self.it
        else:
            raise StopIteration