from playsound import playsound
import os

# Directory where music files are stored
music_directory = "P:\projects\CodeClause\music"

# Get a list of music files in the directory
music_files = [f for f in os.listdir(music_directory) if f.endswith('.mp3')]

def play_music(file_name):
    playsound(os.path.join(music_directory, file_name))

def main():
    print("Welcome to the Python Music Player!")
    
    while True:
        print("\nAvailable songs:")
        for index, song in enumerate(music_files, start=1):
            print(f"{index}. {song}")

        choice = input("Enter the number of the song to play (or 'q' to quit): ")
        
        if choice == 'q':
            break
        
        try:
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(music_files):
                selected_song = music_files[choice_index]
                play_music(selected_song)
                print(f"Now playing: {selected_song}")
            else:
                print("Invalid choice. Please select a valid song.")
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")

    print("Thank you for using the Python Music Player!")

if __name__ == "__main__":
    main()
