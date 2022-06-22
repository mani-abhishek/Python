# List all files of certain type in a directory using Python


import subprocess
import os


# create a directory
def create_dir(new_path):
    if not os.path.exists(new_path):
        os.mkdir(new_path)

# move file into created folder
def clean(old_path,file,new_path):
    create_dir(new_path)
    old_path = os.path.join(r"C:\Users\abhis\Downloads", file)
    process = f'''move "{old_path}" {new_path}'''
    subprocess.run(process,shell=True)






# search file according to it's type
def main():
    # return all files as a list
    for file in os.listdir(r'C:\Users\abhis\Downloads'):
        
        if file.endswith(".docx") or file.endswith(".doc"):
            new_path = r"C:\Users\abhis\Downloads\MSdocs"
            clean(r"C:\Users\abhis\Downloads",file,new_path)

        if file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".jpg"):
            new_path = r"C:\Users\abhis\Downloads\pics"
            clean(r"C:\Users\abhis\Downloads",file,new_path)

        if file.endswith(".pdf"):
            new_path = r"C:\Users\abhis\Downloads\PDF"
            clean(r"C:\Users\abhis\Downloads",file,new_path)

        if file.endswith(".mp3"):
            new_path = r"C:\Users\abhis\Downloads\Audio"
            clean(r"C:\Users\abhis\Downloads",file,new_path)
        
        if file.endswith(".mp4") or file.endswith(".mkv"):
            new_path = r"C:\Users\abhis\Downloads\Video"
            clean(r"C:\Users\abhis\Downloads",file,new_path)

        if file.endswith(".xlsx") or file.endswith(".csv"):
            new_path = r"C:\Users\abhis\Downloads\ExelSheet"
            clean(r"C:\Users\abhis\Downloads",file,new_path)
        
        if file.endswith(".zip"):
            new_path = r"C:\Users\abhis\Downloads\zipfolder"
            clean(r"C:\Users\abhis\Downloads",file,new_path)

        if file.endswith(".pptx") or file.endswith(".ppt"):
            new_path = r"C:\Users\abhis\Downloads\PPTfolder"
            clean(r"C:\Users\abhis\Downloads",file,new_path)
        
        if file.endswith(".txt"):
            new_path = r"C:\Users\abhis\Downloads\TXTFolder"
            clean(r"C:\Users\abhis\Downloads",file,new_path)
        
        if file.endswith(".exe"):
            new_path = r"C:\Users\abhis\Downloads\Setup"
            clean(r"C:\Users\abhis\Downloads",file,new_path)










if __name__ =="__main__":
    main()
