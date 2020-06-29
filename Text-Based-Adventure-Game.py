

def question(option1, option2, op1_positive_negative, op2_positive_negative,
 win_condition):
    answer = input(f"what do you want to do ({option1}/{option2}): ")
    if (answer == option1) and (op1_positive_negative == "positive"):
        return True

    if (answer == option1) and (op1_positive_negative == "negative"):
        return False

    if (answer == option2) and (op2_positive_negative == "positive"):
        return True

    if (answer == option2) and (op2_positive_negative == "negative"):
        return False

