def logged(func):
    def wrapper(*args,**kwargs):
        print("Action ho raha hai")
        return func(*args,**kwargs)
    return wrapper

class Cricketer():
    def __init__(self, name, runs=0):
        self.name = name
        self.runs = runs
    @logged
    def add_runs(self,runs):
        self.runs += runs
        print(f"{self.name}: {self.runs} runs")

class Captain(Cricketer):
    def __init__(self, name, runs=0):
        super().__init__(name, runs)
    def toss_win(self):
        return "Toss win@"
        