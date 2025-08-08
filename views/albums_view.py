from models.repos.albums_repo import AlbumsRepo
from models.albums import Albums


def view_all_Albums():
    """Fetches and displays all Albums."""
    try:
        ar = AlbumsRepo()
        gat = ar.get_all_albums()
        if not gat:
            print("NO Albums found.")
        else:
            for li in gat:
                print(f"ID: {li.albumid}, title: {li.title}, Artist ID: {li.artistid}")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_albums():   
    """fetches and displays one almbums."""
    try:
        ar = AlbumsRepo()
        aid = int(input("Enter Album ID: "))
        album = ar.get_albums(aid)
        if album:
            print(f"ID: {album.albumid}, Title: {album.title}, Artist ID: {album.artistid}")
        else:
            print("Album not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def create_albums():
    """Creates a new album."""
    try:
        title = input("Enter Album Title: ")
        artistid = int(input("Enter Artist ID: "))
        model = Albums(title=title, artistid=artistid)              
        ar = AlbumsRepo()
        ar.create_albums(model)
        print("Album created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


def update_albums():
    """Updates an existing album."""
    try:
        aid = int(input("Enter Album ID to update: "))
        title = input("Enter new Album Title: ")
        artistid = int(input("Enter new Artist ID: "))

        model = Albums(albumid=aid, title=title, artistid=artistid)
        ar = AlbumsRepo()
        ar.update_albums(aid, model)
        print("Album updated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_albums():
    """Deletes an album."""
    try:
        aid = int(input("Enter Album ID to delete: "))
        ar = AlbumsRepo()
        ar.delete_albums(aid)
        print("Album deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main2():
    while True:
        print("Albums Menu")
        print("1. View All Albums")
        print("2. View Album by ID")
        print("3. Create Album")
        print("4. Update Album")    
        print("5. Delete Album")
        print("0. Exit")

        

        choice = input("Enter your choice : ")

        if choice == '1':
            view_all_Albums()
        elif choice == '2':
            view_albums()
        elif choice == '3':
            create_albums()
        elif choice == '4':
            update_albums()
        elif choice == '5':
            delete_albums()
        elif choice == '0':
            print("Exit.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main2()

