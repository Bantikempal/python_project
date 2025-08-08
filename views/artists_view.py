from models.repos.artists_repo import ArtistsRepo
from models.artists import Artists

def view_all_artists():
    """Fetches and displays all artists."""
    try:
        ar = ArtistsRepo()
        gaa= ar.get_all_artists()
        if not gaa:
            print("No artists found.")
        else:
            for artist in gaa:
                print(f"ID: {artist.artistid}, Name: {artist.Name}")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_artists():
    try:
        aid = int(input("Enter Artist ID to view: "))
        ar = ArtistsRepo()
        artist = ar.get_artists(aid)
        if artist:
            print(f"ID: {artist.artistid}, Name: {artist.Name}")
        else:
            print("Artist not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def create_artist():
    try:
        Name = input("Enter artist name: ")
        artistid = int(input("Enter artist ID: "))
        artist = Artists(artistid=artistid, Name=Name)
        ar = ArtistsRepo()
        ar.create_artists(artist)
        print("Artist created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


def update_artist():
    try:
        aid = int(input("Enter Artist ID to update: "))
        Name = input("Enter new artist name: ")
        artist = Artists(Name=Name)
        ar = ArtistsRepo()
        ar.update_artists(aid, artist)
        print("Artist updated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_artist():
    try:
        aid = int(input("Enter Artist ID to delete: "))
        ar = ArtistsRepo()
        ar.delete_artists(aid)
        print("Artist deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main1():
    while True:
        print("Artists Management")
        print("1. View All Artists")
        print("2. View Artist by ID")
        print("3. Create Artist")
        print("4. Update Artist")
        print("5. Delete Artist")
        print("0. exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            view_all_artists()
        elif choice == '2':
            view_artists()
        elif choice == '3':
            create_artist()
        elif choice == '4':
            update_artist()
        elif choice == '5':
            delete_artist()
        elif choice == '0':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main1()
