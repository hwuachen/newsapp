import os

def main():
    with open('NathanSoccerGames.txt', mode='r') as lists:
        for item in lists:
            if item.startswith('#') or item.strip()=="" :
                continue
            filename = item.replace("https://youtu.be/", "https://www.youtube.com/watch?v=")
            print("filename=",filename)
            cmd = "youtube-dl " + filename.strip()
            os.system(cmd) 
            print(cmd, " is complete.")

main()