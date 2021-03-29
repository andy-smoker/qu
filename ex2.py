import hashlib
import sys
import secrets


d = {True: "OK",False: "FAIL"}

method = {
    "md5": hashlib.md5(),
    "sha1": hashlib.sha1()
}

def get_hash(path, mod):
    try:
        with open(path, 'rb') as f:
            m = method[mod]
            while True:
                data = f.read(8192)
                if not data:
                    break
                m.update(data)
            return m.hexdigest()
    except FileNotFoundError:
        return "NOT FOUND"

if __name__ == '__main__':
    if sys.argv[1] == "get-hash" and len(sys.argv) > 3: # выводи хеш определённого файла
        print(get_hash(sys.argv[2], sys.argv[3]))

    elif len(sys.argv) == 3:                # основаня функция по заданию
        with open(sys.argv[1], 'r') as f:
            files = f.read().splitlines()
        for file in files:
            file = file.split(" ")
            out = get_hash(f"{sys.argv[2]}/{file[0]}", file[1])     # получаем хеш файла при налчии
            if out != "NOT FOUND":
                out = d[secrets.compare_digest(file[2], out)]       # сравниваем хеши   
            print(f"{file[0]} {out}")