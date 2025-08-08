from views.artists_view import main1
from views.albums_view import main2  
# from views.customers_view import main3
# from views.employees_view import main4
# from views.tracks_view import main5

while True:
    print("1. Manage Artists")
    print("2. Manage Albums")
    print("3. Manage Customers")
    print("4. Manage Employees")
    print("5. Manage Tracks")
    print("0. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        main1()
    elif choice == '2':
        main2()
    
    elif choice == '0':
        print("Exit.")
        break
    else:
        print(".")