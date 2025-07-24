def quiz_game():
    questions = {'Capital of India?': 'A', '2+2?': 'B'}
    for q, a in questions.items():
        try:
            ans = input(q + " [A/B/C/D]: ")
            if ans.upper() not in 'ABCD':
                raise ValueError("Invalid option")
        except Exception as e:
            print(e)