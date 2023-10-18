# Download script for mp3 audiofiles
# You need to change site url and folder name each time
# (site url differes a lot and there is no pattern to automate it)
import os
import requests


site_url = 'https://ipaudio.club/wp-content/uploads/APP/Algorithms%20to%20Live%20By/'
folder_name = "BRIAN CHRISTIAN – ALGORITHMS TO LIVE BY AUDIOBOOK".title()


if not os.path.exists(folder_name):
    os.makedirs(folder_name)

number = 1
while number:
    file_number = f'0{number}' if number < 10 else number
    file_url = f"{site_url}{file_number}.mp3"
    response = requests.get(file_url)

    if response.status_code == 200:
        file_name = file_url.split("/")[-1]
        file_path = os.path.join(folder_name, file_name)

        with open(file_path, "wb") as file:
            file.write(response.content)
        number +=1
        print(f"Downloaded {file_name}")
    elif response.status_code == 404:
        print("No more files to download")
        break
    else:
        print("Failed to download the file")
        break