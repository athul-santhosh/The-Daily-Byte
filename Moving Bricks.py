def Transport(bricks):
    if not bricks : return None

    heapify(bricks)

    wheel_barrow = 0
    number_of_bricks = 0
    while wheel_barrow < 5000 and len(bricks) != 0:
        
        load = heappop(bricks)
        wheel_barrow += load
        number_of_bricks += 1
        #print(wheel_barrow)
        #print(number_of_bricks)
    
    if wheel_barrow >= 5000:
        return number_of_bricks -1
    return number_of_bricks

#     1000       2000          2800
# x---------x----------------x-------------------------------x
# x-----------------------------------------x # = break condition 

#                 5000


print(Transport([1000, 1000, 1000, 2000]))
print(Transport([1000, 200, 150, 200]))