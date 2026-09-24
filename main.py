from pathlib import Path
import shutil
import os
folder_path = input("Enter folder path: ")
p = Path(folder_path)
(p/'Image').mkdir(parents=True, exist_ok=True)
(p/'Video').mkdir(parents=True, exist_ok=True)
(p/'Document').mkdir(parents=True, exist_ok=True)
(p/'Python').mkdir(parents=True, exist_ok=True)
(p/'Other').mkdir(parents=True, exist_ok=True)
files = list(p.rglob('*'))
for item in files:
    if item.is_file():
        if item.suffix == '.py':
            destination = 'Python'
        elif item.suffix == '.mp4' or item.suffix == '.avi' or item.suffix == '.mov':
            destination = 'Video'
        elif item.suffix == '.jpg' or item.suffix == '.jpeg' or item.suffix == '.png':
            destination = 'Image'
        elif item.suffix == '.xlsx' or item.suffix == '.xls' or item.suffix == '.doc' or item.suffix == '.docx' or item.suffix == '.pdf' or item.suffix == '.txt':
            destination = 'Document'
        else:
            destination = 'Other'
        if item.parent == p/destination:
            continue
        print(item.name, '->', destination)
        d_path = p/destination/item.name
        if d_path.exists():
            print(f'{item.name} already exists in {destination}\n what do you want to do?')
            replace_file = input('Replace existing file? (y/n): ')
            if replace_file == 'y':
                os.remove(d_path)
                shutil.move(item, p/destination)
                print('item replaced')
            elif replace_file == 'n':
                rename_file = input('Rename existing file? (y/n): ')
                if rename_file == 'y':
                    counter = 1
                    new_name = item.stem + '_' + str(counter) + item.suffix
                    new_path = p/destination/new_name
                    while new_path.exists():
                        counter += 1
                        new_name = item.stem + '_'+ str(counter) + item.suffix
                        new_path = p / destination / new_name
                    shutil.move(item, new_path)
                    print('Name changed to ' + new_name)
                elif rename_file == 'n':
                    print('file skip')
                    continue
        else:
            shutil.move(item, p / destination)

#git practice