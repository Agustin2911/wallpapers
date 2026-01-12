import os 


dir=os.listdir()
arch=open("README.md","w",encoding="UTF-8")
for i in dir:
    
    if i!="readme.py":
        text=f"![{i}]({i})\n"
        arch.write(text)

arch.close()
