from models.repos.tracks_repo import TracksRepo
from models.tracks import Tracks    

def view_all_Tracks():
    """Fetches and displays all Tracks."""
    try:
        tr = TracksRepo()
        gat = tr.get_all_tracks()
        if not gat:
            print("NO Tracks found.")
        else:
            for li in gat:
                print(f"ID: {li.Tracksid}, Name: {li.Tracksname}, Album ID: {li.albumid}, Media Type ID: {li.Mediatypeid}, Genre ID: {li.genreid}")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_track():
    pass

def create_Tracks():
    pass

def update_Tracks():
    pass

def delete_Tracks():
    pass

def main():
    print("1. View All Tracks")
    print("2. View Track")
    print("3. Create Track")
    print("4. Update Track")
    print("5. Delete Track")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        view_all_Tracks()
    elif choice == '2':
        view_track()
    elif choice == '3':
        create_Tracks()
    elif choice == '4':
        update_Tracks()
    elif choice == '5':
        delete_Tracks()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()

