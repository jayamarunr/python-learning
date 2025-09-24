class LabourApp:

    def __init__(s):

        # initialize labour first

        s.labours=[]

    # adding method > new labour

    def add(s,n,a,sk,w):

        s.labours.append({"name":n,"age":a, "skill":sk, "wage":w, "days":0})

    # work method > record one day of work

    def work(s,n):

        for l in s.labours:

            if l['name']==n:
                
                l["days"]+=1

                print(f"{n} worked a day. Total days: {l['days']}")

    # salary method > calculate salary

    def salary(s,n):

        for l in s.labours:

            if l['name']==n:

                pay=l["wage"]*l["days"]

                print(f"{n}'s Salary = ${pay}")

    
    #view method > show all labours

    def view(s):

        for i, l in enumerate(s.labours.l):

            print(f"{i}. {l['name']} - {l['age']}yrs - {l['wage']}/day - Days:{l['days']}")


    # remove method > delete labour by name


    def remove(s,n):

        s.labours=[l for l in s.labours if l['name']!=n]

app=LabourApp()

while True:

    print("\n1. Add Labour \n2.View Labours \n3.Record Work \n4. Calculate Salary \n5.Remove Labour \n6.Exit")
    
    ch=input("Choose:")

    if ch=="1":
        
        app.add(input("Name:"),int(input("Age:")),input("skill:"),int(input("wage/day:")))

    elif ch=="2":

        app.view()

    elif ch=="3":

        app.work(input("Name:"))

    elif ch=="4":

        app.salary(input("Name:"))

    elif ch=="5":

        app.remove(input("Name:"))

    elif ch=="6":
        
        break

    else:

        print("Invalid")
        
    #program ends