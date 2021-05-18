##while loops

# דוגמה:

# num=int(input("Enter a number: "))
#
# while(num!=7):
#     print(num*100)
#     num = int(input("Enter a number: "))

# דוגמה 2:

# counter=10
# while(counter>0):
#     print(counter*100)
#     print("Hello")
#     counter=counter-1

from time import sleep

while(True):
    print("\nMenu:\n\n1.Insert Number and ** it by 3\n2.Insert 4 IPs to a list and print it\n3.Insert 4 Entries to DNS_Dictionary and print it\n4.Check if a string is polindrom")
    choice=int(input("\nType your choice: \n "))
    if (choice==1):
        number=int(input("We will calculate your number: "))
        print("Calculating number...")
        sleep(3)
        print(number**3)
    elif (choice==2):
        ip_list=[]
        ip_list.append(input("Enter new IP: "))
        ip_list.append(input("Enter new IP: "))
        ip_list.append(input("Enter new IP: "))
        ip_list.append(input("Enter new IP: "))
        print("The new list:\n " + str(ip_list))
    elif (choice==3):
        dns_dict={}
        dns_dict.update({input("Enter a URL: "): input("Enter an IP: ")})
        dns_dict.update({input("Enter a URL: "): input("Enter an IP: ")})
        dns_dict.update({input("Enter a URL: "): input("Enter an IP: ")})
        dns_dict.update({input("Enter a URL: "): input("Enter an IP: ")})
        print("The new DNS dictionary is: \n" + str(dns_dict))
    elif (choice==4):
        word=input("Type your word: ")
        if (word==word[::-1]):
            print("This is a polindrom!")
        else:
            print("This isn't a polindrom")
    else:
        print("Pick a number between 1-4 only!!\n")

    exit=input("Would you like to exit? y/n\n")
    if(exit=="y" or exit=="yes"):
        break
    else:
        print("Welcome back!")

print("Thank you and bye bye")
