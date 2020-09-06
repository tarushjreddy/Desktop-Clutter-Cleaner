import shutil
import os
print("omsairam")

files = os.listdir()

files.remove("main.py")
print(files)


def CreateFiles(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


CreateFiles('Images')
CreateFiles('Audios')
CreateFiles('Videos')
CreateFiles('Documents')
CreateFiles('Others')

ImgExts = [".png", ".jpg", ".svg"]

images = [file for file in files if os.path.splitext(file)[
    1].lower() in ImgExts]

DocExts = [".pdf", ".txt", ".word", ".ppt", ".text",
           ".ptx", "exl", ".exel", ".doc", ".docx"]

documents = [file for file in files if os.path.splitext(file)[
    1].lower() in DocExts]

VideoExts = [".mp4", ".mov"]

Videos = [file for file in files if os.path.splitext(file)[
    1].lower() in VideoExts]

AudioExts = [".mp3", ".flv"]

audio = [file for file in files if os.path.splitext(file)[
    1].lower() in AudioExts]


def move(foldername, files):
    for file in files:

        os.replace(file, f"{foldername}/{file}")


# print(Audio)
others = []

for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in ImgExts) and (ext not in DocExts) and (ext not in VideoExts) and (ext not in AudioExts) and os.path.isfile(file):
        others.append(file)
print(others)
# for audio in audiof:
#     os.replace(audio, f"Audios/{audiof}")

move("Audios", audio)
move("Images", images)
move("Videos", Videos)
move("Documents", documents)
move("others", others)
