import os, sys
from xml.dom.minidom import parse
file_path = {
    "linux" : lambda path, file: f"{path}/{file}",
    "windows" : lambda path, file: f"{path}\{file}"
}

def parseConfig(path):
    try:
        with parse(path) as conf:
            ret = list()
            f = conf.getElementsByTagName("file")
            for i in range (0,len(f)):
                ret.append(list())
                ret[i].append(f[i].getAttribute("source_path"))
                ret[i].append(f[i].getAttribute("destination_path"))
                ret[i].append(f[i].getAttribute("file_name"))
        return ret
    except:
        print("invalid config file")
        return

def moveFile(attr, current_os):
    if len(attr) == 0:
        print("empty config file")
        return
    for a in attr:
        if len(a) != 3:
            print("invalid config")
            continue
        if (os.path.exists(file_path[current_os](a[0], a[2])) and os.path.exists(a[1])) != True:
            print("file or directory not exist")
            continue
        os.replace(file_path[current_os](a[0], a[2]), file_path[current_os](a[1], a[2]))
        if os.path.exists(file_path[current_os](a[1], a[2])) == True:
            print(f"file was moved to {a[1]}")
        else:
            print("something was wrong and file was not moved")
            
    

if __name__ == "__main__":
    try:
        moveFile(parseConfig("./config.xml"), sys.platform)
    except:
        print("☝")