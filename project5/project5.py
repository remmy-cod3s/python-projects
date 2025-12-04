print("Welcome to Remon's to-do app")
def app():
    Monday = []
    Tuesday = []
    Wednesday = []
    Thursday = []
    Friday = []
    Saturday = []
    Sunday = []
    day = input("What day of the week is it?:\n ")
    counter = 0
    if day.lower() == "monday":  
        ask2 = "yes"
        while ask2 == "yes":
            ask = input("what would you like to accomplish today?:\n ")
            counter+=1
            Monday.append(f"{counter}) {ask}")
            ask2 = input("Would you like to add another task, yes or no ?:\n ")
            if ask2 == "yes":
                continue
            else:
                break
        print(f"your tasks for {day} are as follows: ")
        for task in Monday:
            print(task+"\n") 
               
    elif day.lower() == "tuesday": 
        ask2 = "yes"
        while ask2 == "yes":   
            ask = input("what would you like to accomplish today?:\n ")
            counter+=1
            Tuesday.append(f"{counter}){ask}")
            ask2 = input("Would you like to add another task, yes or no ?:\n ")
            if ask2 == "yes":
                continue
            else:
                break
        print(f"your tasks for {day} are as follows: ")
        for task in Tuesday:
            print(task+"\n")   
             
    elif day.lower() == "wednesday":
        ask2 = "yes"
        while ask2 == "yes":    
            ask = input("what would you like to accomplish today?:\n ")
            counter+=1
            Wednesday.append(f"{counter}){ask}")
            ask2 = input("Would you like to add another task, yes or no ?:\n ")
            if ask2 == "yes":
                continue
            else:
                break
        print(f"your tasks for {day} are as follows: ")
        for task in Wednesday:
            print(task+"\n")  
              
    elif day.lower() == "thursday":
        ask2 = "yes"
        while ask2 == "yes":    
            ask = input("what would you like to accomplish today?:\n ")
            counter+=1
            Thursday.append(f"{counter}){ask}")
            ask2 = input("Would you like to add another task, yes or no ?:\n ")
            if ask2 == "yes":
                continue
            else:
                break
        print(f"your tasks for {day} are as follows: ")
        for task in Thursday:
            print(task+"\n")    
            
    elif day.lower() == "friday":
        ask2 = "yes"
        while ask2 == "yes":  
            ask = input("what would you like to accomplish today?:\n ")
            counter+=1
            Friday.append(f"{counter}){ask}")
            ask2 = input("Would you like to add another task, yes or no ?:\n ")
            if ask2 == "yes":
                continue
            else:
                break
        print(f"your tasks for {day} are as follows: ")
        for task in Friday:
            print(task+"\n")    
            
    elif day.lower() == "saturday":
        ask2 = "yes"
        while ask2 == "yes":   
            ask = input("what would you like to accomplish today?:\n ")
            counter+=1
            Saturday.append(f"{counter}){ask}")
            ask2 = input("Would you like to add another task, yes or no ?:\n ")
            if ask2 == "yes":
                continue
            else:
                break
        print(f"your tasks for {day} are as follows: ")
        for task in Saturday:
            print(task+"\n")    
    elif day.lower() == "sunday":    
        ask2 = "yes"
        while ask2 == "yes":
            ask = input("what would you like to accomplish today?:\n ")
            counter+=1
            Sunday.append(f"{counter}){ask}")
            ask2 = input("Would you like to add another task, yes or no ?:\n ")
            if ask2 == "yes":
                continue
            else:
                break  
        print(f"your tasks for {day} are as follows: ")
        for task in Sunday:
            print(task+"\n")         
                
app()