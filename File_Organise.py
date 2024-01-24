import os

def rename_and_organise_files(directory_path):
    extension = {
        ".jpg" : "Images",
        ".png" : "Images",
        ".gif" : "Images",
        ".pdf" : "Documents",
        ".pptx" : "Documents",
        ".docx" : "Documents",
        ".mp4" : "Videos",
        ".webm" : "Videos",
        ".ogg" : "Videos",
        ".wav" : "Music",
        ".mp3" : "Music"
    }

    for file in os.listdir(directory_path):
        file_extension = os.path.splitext(file)[1]
        output_directory = extension[file_extension]
        if not os.path.exists(os.path.join(directory_path, output_directory)):
            os.mkdir(os.path.join(directory_path, output_directory))

        os.rename(os.path.join(directory_path, output_directory), os.path.join(directory_path, output_directory, file))

directory_path = "C:\Users\gamer\OneDrive\Documents\your_test\921407.jpg"
rename_and_organise_files(directory_path)