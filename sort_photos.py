import os
import shutil
from sys import argv
import exifread
import datetime

script, src = argv
src_files = os.listdir(src)

for file_name in src_files:
    if file_name.endswith('.JPG'):
        fullname = os.path.join(src, file_name)

# find the creation date of the file. Set it to new_date
        foto = open(fullname, "rb")
        data = exifread.process_file(foto, stop_tag="Image Datetime")
        date = data["Image DateTime"]
        datetaken = datetime.datetime.strptime(date.values, '%Y:%m:%d %H:%M:%S')
        day = str(datetaken.day).zfill(2)
        month = str(datetaken.month).zfill(2)
        new_date = day + "-" + month
        foto.close()

# make a folder and copy the file to it. Remove the file from original folder
        new_folder = os.path.join(src, new_date)
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
            shutil.copy(fullname, new_folder)
            os.remove(fullname)
        elif os.path.exists(new_folder):
            shutil.copy(fullname, new_folder)
            os.remove(fullname)

# if file is not a .JPG, copy to "Movie" folder
    else:
        videoname = os.path.join(src, file_name)
        video_folder = os.path.join(src, "Movies")
        if not os.path.exists(video_folder):
            os.makedirs(video_folder)
            shutil.copy(videoname, video_folder)
            os.remove(videoname)
        elif os.path.exists(video_folder):
            shutil.copy(videoname, video_folder)
            os.remove(videoname)

# rename folders to day1, day2, etc
list_maps = os.listdir(src)
day_count = 1
for file in list_maps:
    if file != "Movies":
        os.rename(os.path.join(src, file), os.path.join(src, "Day " + str(day_count)))
        day_count += 1
