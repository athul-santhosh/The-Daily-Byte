def popsicle_stand(customers):
    five , ten,twenty = 0,0,0
    for customer in customers:
        if customer == 5:
            five += 1
        elif customer == 10:
            if five < 1:
                return False
            five -= 1
            ten += 1
        elif customer == 20:
            if five >= 1 and ten >= 1:
                five -= 1
                ten -= 1
            elif five > 3:
                five -= 3
            else:
                return False
            twenty += 1
        print(five,ten,twenty)


    return True

print(popsicle_stand([5, 10]))
print(popsicle_stand([5,10,10,10]))
print(popsicle_stand([5,5,5,10,20]))