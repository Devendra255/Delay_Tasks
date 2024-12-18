''' 
5. A transport company charges the fare according to following table:
Distance    Charges
1-50        8 Rs./Km
51-100      10 Rs./Km
> 100       12 Rs/Km
'''

distance = int(input("Enter the distance: "))

if distance <= 0:
    print("Invalid distance")
elif distance <= 50:
    fare = distance * 8
    print("Total fare:", fare)
elif distance > 50 and distance <= 100:
    fare = distance * 10
    print("Total fare:", fare)
else:
    fare = distance * 12
    print("Total fare:", fare)