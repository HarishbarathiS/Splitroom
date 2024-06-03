# backend logic : 

# get name and store it in a list
def getNames(n):
    names = []
    for i in range(n):
        name = input(f"Enter name {i+1} : ")
        names.append(name)
    return names

# get details about the expense 
def getDeets():
    deets = []
    Date = input("Date of expense : ")
    type = input("Type of expense : ")
    total = int(input("Total amount spent : "))
    deets.extend([Date,type,total])
    return deets

# get deets of people who contributed for the expense
def PaidBy(names):
    paid = {}
    print("Contribution : (name - amount)")
    while True:
        Name_amt = input()
        if Name_amt:
            Name_amt = Name_amt.split(" ")
            paid[Name_amt[0]] = int(Name_amt[1])
        else:
            break
    return paid
    
def SplitEqually(total,n,paid,names):
    # amt each person has to pay
    split = total/n;
    for name in names:
        # if name is not in contributed list, name = 0
        if name not in paid:
            paid[name] = 0.0
        # paid[name] - amt each person has to get/pay 
        paid[name] -= split
    # sort the dict according to value  
    sorted_paid = {k : v for k,v in sorted(paid.items(), key=lambda item : item[1],reverse=True)}
    # converting dictionary into list of tuples
    dict_items = list(sorted_paid.items())
    # create two iterators
    i = 0
    j = len(dict_items) - 1


    while i < j:
        # tuples are immutable hence we have to break down, modify and store 
        i_item = dict_items[i]
        i_key,i_value = i_item

        j_item = dict_items[j]
        j_key,j_value = j_item 
        flag = 1
        # if the amt to be payed is < than amt to be received 
        if i_value + j_value > 0:
            i_value = round(i_value + j_value,2)
            print(f"{j_key} owes {i_key} ${round(-j_value,2)}")
            j_value = 0
        else:
            j_value = round(j_value + i_value,2)
            print(f"{j_key} owes {i_key} ${round(i_value,2)}")
            i_value = 0;
            flag = 0

        # update modified value
        m_i_item = (i_key,i_value)
        m_j_item = (j_key,j_value)
        dict_items[i] = m_i_item
        dict_items[j] = m_j_item

        # updation of iterators
        if flag:
            j -= 1
        else:
            i += 1


print("Welcome to Splitroom")
n = int(input("Enter number of people : "))
names = getNames(n)
deets = getDeets()
paid = PaidBy(names)
SplitEqually(deets[2],n,paid,names)
