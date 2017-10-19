def hotel_cost(nights):
    cost = 70.0 * nights
    return cost

def plane_ticket_cost(city, planeclass):
    #while city != "New York" && city != "Auckland" && city != "Venice" && city != "Glasgow":
        #print("Unsupported destination.")
        #print("Supported destionations: New York; Auckland; Venice; Glasgow.")
        #city = input("Please enter a destination: ")
    if city == "New York":
        basecost = 2000.0
    elif city == "Auckland":
        basecost = 790.0
    elif city == "Venice":
        basecost = 154.0
    elif city == "Glasgow":
        basecost = 65.0
    else:
        basecost = 0.0

    if planeclass == "Economy":
        costmult = 1.0
    elif planeclass == "Premium Economy":
        costmult = 1.3
    elif planeclass == "Business Class":
        costmult = 1.6
    elif planeclass == "First Class":
        costmult = 1.9
    else:
        costmult = 0.0

    cost = basecost * costmult
    return cost

def rental_car_cost(days):
    cost = 30.0 * days
    if days >= 7:
        cost = cost - 50.0
    elif days >= 3:
        cost = cost - 30.0
    return cost

def total_cost(city, planeclass, days):
    nights = days - 1
    hotelcost = hotel_cost(nights)
    planecost = plane_ticket_cost(city, planeclass)
    carcost = rental_car_cost(days)
    totalcost = hotelcost + planecost + carcost
    print(f"The cost of the plane ticket is £{planecost}.")
    print(f"The cost of the hotel is £{hotelcost}")
    print(f"the cost of the rental car is £{carcost}")
    print(f"The total cost is £{totalcost}")

print("Supported Destinations: New York; Auckland; Venice; Glasgow. These are case sensitive.")
city = input("Where do you want to travel? ")
print("Supported Classes: Economy; Premium Economy; Business Class; First Class. These are case sensitive.")
planeclass = input("What class do you want to travel on? ")
days = int(input("How many days do you want to go for? "))
total_cost(city, planeclass, days)
