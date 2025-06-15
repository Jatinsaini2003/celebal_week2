from collections import Counter

def shoe_shop():
    X = int(input())  
    sizes = list(map(int, input().split()))  
    N = int(input())  

    inventory = Counter(sizes)
    earnings = 0

    for _ in range(N):
        size, price = map(int, input().split())
        if inventory[size] > 0:
            earnings += price
            inventory[size] -= 1

    print(earnings)

if __name__ == '__main__':
    shoe_shop()
