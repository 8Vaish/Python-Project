
"""SMS"""
print("\n\nStudent Management System \n\n")
C = 1
q = []
w = []
x = []
p = []
a = []
g = []

while C == 1:

    print("INSTRUCTIONS:")
    print("Press:1 To Upload a Student info")
    print("Press:2 To Display a Student info")
    print("Press:3 To Display all Students info")
    print("Press:4 To Delete a Student info")
    print("Press:5 to Update Students info")
    print("Press:6 to Exit")

    e = int(input("\nEnter your choice: "))
    class Student():
        """Student"""

        if e == 1:
            print("You selected to uplaod a Student info\n")

            print("Please enter the neccesary info")
            i = input("Roll no : ")
            w.append(i)
            na = input("Student Name : ")
            q.append(na)
            br = input("Branch : ")
            x.append(br)
            ph = input("Phone Number : ")
            p.append(ph)
            ad = input("Address : ")
            a.append(ad)
            gr = input("Grade : ")
            g.append(gr)

            print("\nData Entered Sucessfully\n")

            print("If you want to exit then press 1")
            y = int(input("Else press 0 to return to INSTRUCTIONS : "))
            print("\n\n")

            if y == 1:
                print("\nThank You")

            else:
                print()


        elif e == 2:
            print("You selected to View a Students info \n")

            i = int(input("Enter roll number of student whose info you want to display : "))
            print("\nStudent Name : ", q[i - 1])
            print("Roll no : ", w[i - 1])
            print("Branch : ", x[i - 1])
            print("Phone Number : ", p[i - 1])
            print("Address : ", a[i - 1])
            print("Grade :", g[i - 1])
            print("\n")

            print("If you want to exit then press 1")
            y = int(input("Else press 0 to return to INSTRUCTIONS : "))
            print("\n\n")

            if y == 1:
                print("\nThank You")

            else:
                print("")



        elif e == 3:
            print("You Selected to View all Students info \n")
            lr = int(input("Enter last roll number : "))
            print("\n\n")

            for i in range(0, lr):
                print("Student Name : ", q[i])
                print("Roll qo : ", w[i])
                print("Branch : ", x[i])
                print("Phone Number : ", p[i])
                print("Address : ", a[i])
                print("Grade :", g[i])
                print("\n")

            print("If you want to exit then press 1")
            y = int(input("Else press 0 to return to INSTRUCTIONS : "))
            print("\n\n")

            if y == 1:
                print("\nThank You")


            else:
                print()

        elif e == 4:
            print("You selected to Delete a Student info \n")

            i = int(input("Enter roll number of student whose details you want to delete : "))

            q[i - 1] = None
            w[i - 1] = None
            x[i - 1] = None
            p[i - 1] = None
            a[i - 1] = None
            g[i - 1] = None
            print("\nData Deleted Sucessfully\n")

            print("If you want to exit then press 1")
            y = int(input("Else press 0 to return to INSTRUCTIONS : "))
            print("\n\n")

            if y == 1:
                print("\nThank You")

            else:
                print("")



        elif e == 5:
            print("You selected to Update Student's Info\n")

            i = int(input("Enter roll number of student whose info you want to update : "))
            q[i - 1] = input("Student Name : ")
            w[i - 1] = input("Roll no : ")
            x[i - 1] = input("Branch : ")
            p[i - 1] = input("Phone Number : ")
            a[i - 1] = input("Address : ")
            g[i - 1] = input("Grade : ")
            print("\nData Updated Sucessfully\n")

            print("If you want to exit then press 1")
            y = int(input("Else press 0 to return to INSTRUCTIONS  : "))
            print("\n\n")

            if y == 1:
                print("\nThank You")

            else:
                print("")



        elif e == 6:
            print("\nThankYou")
            print("Exiting\n")
            c = 0