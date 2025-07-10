# Quiz App
def quiz():
    def ask(q, a):
        return input(q) == a
    score = 0
    if ask("Capital of India? ", "Delhi"): score += 1
    if ask("2 + 2 = ? ", "4"): score += 1
    return score

print("Total Score:", quiz())
