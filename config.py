class Config:
    def __init__(self, before, under, q):   
        self.before = before
        self.under = under
        self.q = q

    def __str__(self):
        s= f"Before : \n"
        for i in range(len(self.before)):
            s += f"\t - {i} tape : \n"
            for j in range(len(self.before[i])):
                s+= f"\t \t - {self.before[i][j]} \n"
        s+= f"After : \n"
        for i in range(len(self.under)):
            s += f"\t - {i} tape : \n"
            for j in range(len(self.under[i])):
                s+= f"\t \t - {self.under[i][j]} \n"
        s+= f"State : {self.q}"
        return s