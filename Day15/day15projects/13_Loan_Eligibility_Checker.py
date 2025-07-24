class LowCreditScoreError(Exception): pass

def check_loan(income, score):
    try:
        assert income > 0
        if score < 600:
            raise LowCreditScoreError("Credit too low")
        print("Eligible")
    except Exception as e:
        print(e)