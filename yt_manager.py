import sqlite3

try:
    conn = sqlite3.connect('videos.db')
    print("\n[INFO] Database connected successfully.")
except sqlite3.Error as e:
    print("[ERROR] Database connection error:", e)

cursor = conn.cursor()

# Check if table already exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='videos'")
table_exists = cursor.fetchone()

# Create the table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

if not table_exists:
    print("[INFO] Table 'videos' created successfully.")
else:
    print("[INFO] Table 'videos' already exists.")

# Utility functions
def list_videos():
    print("\n" + "=" * 19 + " Video List " + "=" * 19)
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()
    
    if videos:
        print(f"{'ID':<5} {'Name':<30} {'Duration':<10}")
        print("-" * 50)
        for video in videos:
            print(f"{video[0]:<5} {video[1]:<30} {video[2]:<10}")
    else:
        print("No videos found.")
    print("=" * 50)


def add_video(name, time):
    try:
        cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
        conn.commit()
        print("\n[INFO] Video added successfully.")
    except sqlite3.Error as e:
        print("[ERROR] Error adding video:", e)

def update_video(video_id, new_name, new_time):
    try:
        cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
        conn.commit()
        print("\n[INFO] Video updated successfully.")
    except sqlite3.Error as e:
        print("[ERROR] Error updating video:", e)

def delete_video(video_id):
    try:
        cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
        conn.commit()
        print("\n[INFO] Video deleted successfully.")
    except sqlite3.Error as e:
        print("[ERROR] Error deleting video:", e)

def main():
    while True:
        print("\n========== YouTube Manager ==========")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit")
        print("=====================================")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("\nEnter the video name: ").strip()
            time = input("Enter the video duration (e.g., HH:MM:SS): ").strip()
            add_video(name, time)
        elif choice == '3':
            try:
                video_id = int(input("\nEnter the video ID to update: "))
                name = input("Enter the new video name: ").strip()
                time = input("Enter the new video duration (e.g., HH:MM:SS): ").strip()
                update_video(video_id, name, time)
            except ValueError:
                print("[ERROR] Invalid ID. Please enter a number.")
        elif choice == '4':
            try:
                video_id = int(input("\nEnter the video ID to delete: "))
                delete_video(video_id)
            except ValueError:
                print("[ERROR] Invalid ID. Please enter a number.")
        elif choice == '5':
            print("\n[INFO] Exiting application. Goodbye!")
            break
        else:
            print("[ERROR] Invalid choice. Please select a valid option (1-5).")

    conn.close()

if __name__ == "__main__":
    main()
