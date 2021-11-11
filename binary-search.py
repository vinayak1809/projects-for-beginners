l = [15, 7, 5, 10, 6, 4, 85, 21, 36, 32, 52]
l.sort()
print(l)

en = int(input("enter the number you want index for : "))


def find(l, en):

    low = 0
    high = len(l)-1

    while (low <= high):
        midl = (low + high) / 2
        mid = round(midl)

        if en == l[mid]:
            print(mid)
            break
        elif en < l[mid]:
            high = mid-1

        elif en > l[mid]:
            low = mid+1


find(l, en)
