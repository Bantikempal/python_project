from models.repos.tracks_repo import TracksRepo

def view_Tracks():
    """Fetches and displays all Tracks."""
    try:
        tr = TracksRepo()
        gat = tr.get_all_tracks()
        if not gat:
            print("NO Tracks found.")
        else:
            for li in gat:
                print(f"ID: {li.Tracksid}, Name: {li.Tracksname}")
    except Exception as e:
        print(f"An error occurred: {e}")

def hello():
    print("Hello user")

if __name__ == "__main__":
    view_Tracks()