usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "admin" and passwordInput == "qwer":
    print(" ---------------------------------")
    print("     Welcome To Mirage Shop      ")
    print("     Please Select The Order     ")
    print(" ---------------------------------")
    print("1.Reading Book       x 1 :   150 ฿ ")
    print("2.Writing Book       x 1 :   200 ฿ ")
    print("3.Geography Book     x 1 :   450 ฿ ")
    print("4.Science Book       x 1 :   210 ฿ ")
    print("5.Psychology Book    x 1 :   175 ฿ ")
    print(" ---------------------------------")
    order = int(input("Your Order >> "))
    if order == 1:
        item1 = int(input("How many do you want? >> "))
        print("Your Selected Order is Reading Book x",item1)
        result1 = 150*item1
        print("==================================")
        print("Total Price :",result1,"฿")
        print("==================================")
    elif order == 2:
        item2 = int(input("How many do you want? >> "))
        print("Your Selected Order is Writing Book x",item2)
        result2 = 200*item2
        print("==================================")
        print("Total Price :",result2,"฿")
        print("==================================")
    elif order == 3:
        item3 = int(input("How many do you want? >> "))
        print("Your Selected Order is Geography Book x",item3)
        result3 = 450*item3
        print("==================================")
        print("Total Price :",result3,"฿")
        print("==================================")
    elif order == 4:
        item4 = int(input("How many do you want? >> "))
        print("Your Selected Order is Science Book x",item4)
        result4 = 210*item4
        print("==================================")
        print("Total Price :",result4,"฿")
        print("==================================")
    elif order == 5:
        item5 = int(input("How many do you want? >> "))
        print("Your Selected Order is Psychology Book x",item5)
        result5 = 175*item5
        print("==================================")
        print("Total Price :",result5,"฿")
        print("==================================")
    else:
        print("Error!! Please Try Again.")
else:
    print("Error!! Please Try Again.")