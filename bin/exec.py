import sys
import datetime
import os
format_time=datetime.datetime.now().strftime('%Y-%m-%d')
FILE_PATH=r"{0}\words\word.txt-{1}.txt".format(os.environ["WR_HOME"],format_time)
if(sys.argv[1]=="put"):
    with open(FILE_PATH,"a") as f:
        line=" ".join(sys.argv[2:])
        line+="\n"
        f.write(line)
elif(sys.argv[1]=="delete"):
    lines=None

    with open(FILE_PATH,"r") as f:
        lines=f.readlines()

    with open(FILE_PATH,"w") as f:
        f.writelines(lines[:-1])
elif(sys.argv[1]=="get"):
    if(not os.path.exists(FILE_PATH)):
        print("You haven't put a single new word today.")
        exit(1)
    with open(FILE_PATH,"r") as f:
        lines=f.readlines()
        for line in lines:
            print(line)
