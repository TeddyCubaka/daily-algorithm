def open_or_senior(data):
    return ["Senior" if person[0] >= 55 and person[1] > 7 else "Open" for person in data]

# an example
# print(open_or_senior([[18, 20], [45, 2], [61, 12], [88, 8], [21, 21], [78, 9]]))