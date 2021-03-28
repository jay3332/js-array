from jsarray import JSArray

array = JSArray([1, 2, 3, 4, 5])

print(array.length)  # expected: 5
print(JSArray(range(5000)).length)  # expected: 5000
print(JSArray([1, 2, 3]).for_each(lambda item: print(item, end=" ")))  # expected: 1 2 3

print("\n")

print(
    array
    .filter(lambda item: item < 4)
    .map(lambda item: item**2)
    .filter(lambda item: item % 2 == 0)
    .find(lambda item: item > 3)
)  # expected: 4

print(
    JSArray(range(10000))
    .filter(lambda item: item > 1000)
    .filter(lambda item: item % 3 < 2)
    .map(lambda item: item ** 2)
    .map(lambda item: item // 12)
    .filter(lambda item: item < 100000)
    .find(lambda item: item % 2 == 1)
)  # expected: 83667

print(
    JSArray([1, 2, [3, 4], [5, 6], 7])
    .flat()  # .flat() may be a bit slow, so please be aware
)  # expected: [1, 2, 3, 4, 5, 6, 7]
