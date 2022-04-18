"""
Created by hu-jinwen on 2022/4/3
"""
have_ticket = True
knife_length = int(input("announce the length:"))
if have_ticket:
    print("pass the ticket checking")
    if knife_length > 20:
        print("throw away your knife please, your knife length is %d " % knife_length)
    else:
        print("pass the luggage checking")


else:
    print("buy ticket please")

