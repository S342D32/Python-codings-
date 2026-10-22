
def FractionalKnapsack(arr, w):
    arr.sort(key=lambda x: x.value / x.weight, reverse=True)

    currValue = 0
    finalValue = 0

    for i in range(len(arr)):
        if currValue + arr[i].weight <= w:
            currValue += arr[i].weight
            finalValue += arr[i].value
        else:
            remaining = w - currValue
            cost = (arr[i].value / arr[i].weight) * remaining
            finalValue += cost
            break

    return finalValue


class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

arr = [
    Item(100, 20),
    Item(60, 10),
    Item(100, 50),
    Item(200, 50)
]

w = 90

print(FractionalKnapsack(arr, w))