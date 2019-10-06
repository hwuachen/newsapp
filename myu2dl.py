import os

def main():
    with open('mylist.txt', mode='r') as lists:
        for item in lists:
            filename = item.replace("https://youtu.be/", "https://www.youtube.com/watch?v=")
            print("filename=",filename)
            cmd = "youtube-dl " + filename
            print(cmd)
            os.system(cmd) 

main()