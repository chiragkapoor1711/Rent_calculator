rent=int(input("enter the total Rent of hostel/falt/pg = "))
food=int(input("enter the amonut of food orederd = "))
electricity_spend=int(input("enter the toatl bill of electricty spend = "))
charge_per_unit=int(input("enter the charge per unit = "))
persons=int(input("enter the no. of person living in the room = "))

total_bill = electricity_spend * charge_per_unit
output=(rent + food + total_bill)/persons
print("each person will pay",output)