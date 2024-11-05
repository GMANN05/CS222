def Quicksort(c):
    if len(c) <= 1:
        return c
    else:
        pivot = c[0]
        less = [n for n in c[1:] if n <= pivot]
        greater = [n for n in c[1:] if n > pivot]
        return Quicksort(less) + [pivot] + Quicksort(greater)
def main():
    numbers = [50, 100, 20, 100, 90, 80, 40, 120, 30, 50, 10]
    print(Quicksort(numbers))
main()