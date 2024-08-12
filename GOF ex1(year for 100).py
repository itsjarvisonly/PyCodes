def message():
    name = input("Give your name: ")
    age = input("Give your age: ")
    days = 100 - int(age)
    print("Years remaining for 100 years of age are: ",days)
    current_year = int(input("what is the current year: "))
    print( name ," You will be 100 in the year: ",current_year + days + 1)
message()