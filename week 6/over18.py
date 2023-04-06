# over 18

def eligibleOnly(allTheAges):
    eligiblePeople = {}
    for key, value in allTheAges.items():
        if value >= 18:
            eligiblePeople[key] = value
    return eligiblePeople

allAge = {
    "Oscar": 5,
    "Mayank": 10,
    "Aayush": 21
}

print(eligibleOnly(allAge), "is eligible")