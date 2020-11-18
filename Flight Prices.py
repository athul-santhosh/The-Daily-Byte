def flight_tickets(prices):


    prices = sorted(prices,key = lambda x:max(x[0],x[1]))

    office_A = 0
    office_B = 0
    ticket = 0

    print(prices)

    for flights in prices:
        flight_A = flights[0]
        flight_B = flights[1]
        if flight_A <= flight_B and office_A <= (len(prices)// 2) + 1:
            office_A += 1
            ticket  += flight_A
        else:
            office_B += 1
            ticket += flight_B

    return ticket

print(flight_tickets([[300,200], [30,60] ,[50,50], [40,30]]))
