def score(capital, distance, people, date):
    result = 0
    if capital > 30000:
        result += 0.3
    elif capital > 100000:
        result += 0.65
    elif capital > 300000:
        result += 1
    if distance < 200:
        result += 1
    elif distance < 600:
        result += 0.65
    elif distance < 1000:
        result += 0.3
    if people > 15:
        result += 0.3
    elif people > 50:
        result += 0.65
    elif people > 100:
        result += 1
    if date > 1:
        result += 0.3
    elif date > 3:
        result += 0.65
    elif date > 5:
        result += 1
    return result
