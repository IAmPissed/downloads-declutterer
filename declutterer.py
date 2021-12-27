from dotenv import load_dotenv


import os
import time
import shutil

load_dotenv()

# Downloads Folder Path
downloads = os.getenv('SOURCE_FOLDER_PATH')
    

def move_files():   

    for item in os.listdir(downloads):
        if os.path.isfile(f'{downloads}\\{item}'):
            extention = os.path.splitext(f'{downloads}\\{item}')[1]
            source_path = f'{downloads}\\{item}'

            if extention == '.txt':
                dst_path = f'{downloads}\\Documents\\Text\\{item}'
            elif extention == '.pdf':
                dst_path = f'{downloads}\\Documents\\PDF\\{item}'
            elif extention == '.pptx':
                dst_path = f'{downloads}\\Documents\\PowerPoint\\{item}'
            elif extention == '.mkv' or extention == '.mp4':
                dst_path = f'{downloads}\\Videos\\{item}'
            elif extention == '.zip':
                dst_path = f'{downloads}\\Compressed\\{item}'
            elif extention == '.xlsx':
                dst_path = f'{downloads}\\Documents\\Excel\\{item}'
            elif extention == '.docx':
                dst_path = f'{downloads}\\Documents\\Word\\{item}'
            elif extention == '.png' or extention == '.jpg' or extention == '.svg':
                dst_path = f'{downloads}\\Images\\{item}'
            elif extention == '.exe':
                dst_path = f'{downloads}\\Programs\\{item}'
            elif extention == '.mp3':
                dst_path = f'{downloads}\\Audio\\{item}'
            
            shutil.move(source_path, dst_path)



if __name__ == '__main__':
    move_files()