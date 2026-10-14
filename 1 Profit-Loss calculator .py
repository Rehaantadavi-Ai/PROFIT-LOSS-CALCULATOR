history=[]

while True:
    break_=False
    history_=[]
    history_2=[]
    history_3=[]
    
    print("1.Profit Loss calculation \n2.History \n3.Exit" )

    choice=int(input("choose what you want to do (1/2/3): "))

    if choice==1:
        print("")
    elif choice==2:
        for x in history:
            print(x)
            continue
    elif choice==3:
        break_==True
    else:
        print("choose appropriate option")
        continue

    if break_==True:
        break

    name=input("Enter name of your item: ").upper()
    cp=int(input("Enter your cost price $"))
    sp=int(input("Enter your selling price $"))
    history_.append(name)
    history_2.append("Cost price=")
    history_2.append(cp)
    history_2.append("selling price=")
    history_2.append(sp)


    #print("$"+str(sp-cp)+" Profit"if cp<sp else("$"+str(cp-sp)+ " Loss"if cp>sp else "No net profit or loss")+" wasted effort and time")
    if cp<sp:
        n=("$"+str(sp-cp)+" Profit")
        history_3.append(n)
        print(n)

    elif sp<cp:
        n=("$"+str(cp-sp)+" Loss")
        history_3.append(n)
        print(n)
    else:
        n=("No net profit")
        history_3.append(n)
        print(n)

    history.append(history_)
    history.append(history_2)
    history.append(history_3)


    while True:
        
        choice=str(input("Do you want to continue? (y/n)")).lower()

        if choice in ("y","yes"):
            break
        elif choice in ("n","no"):
            print("Thank you for visiting")  
            break_=True
            break
        else:
            print("choose appropriately")
            continue
    if break_==True:
        break   