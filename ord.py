import datetime

# year = input("Type in Enlistment Year in numeral format ("2025")\n")
# month = input("Type in Enlistment Month in numeral formmat ("02" , "12")\n")
# day = input("Type in Enlistment Day in numeral format ("04", "20") \n")


enlistment = datetime.date(2024, 7, 11)

#enlistment = datetime.date(year,month,day)]

duration = datetime.timedelta(days = 669)

print(enlistment + duration)
