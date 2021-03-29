import hashlib
import sys
import secrets

d = {True: "OK",False: "FAIL"}


def input_file(file):
    with open(file, 'r') as f:
        lines = f.read().splitlines()
        f.close()
    return lines

def get_hash(path, mod):
    try:
        with open(path, 'rb') as f:
            if mod == "md5":
                m = hashlib.md5()
            elif mod == "sha1":
                m = hashlib.sha1()
            else:
                return
            while True:
                data = f.read(8192)
                if not data:
                    break
                m.update(data)
            return m.hexdigest()
    except FileNotFoundError:
        return "NOT FOUND"

if __name__ == '__main__':
    if sys.argv[1] == "get-hash" and len(sys.argv) > 3:
        print(get_hash(sys.argv[2], sys.argv[3]))

    elif len(sys.argv) == 3:
        with open(sys.argv[1], 'r') as f:
            files = f.read().splitlines()
            f.close()
        for file in files:
            file = file.split(" ")
            out = get_hash(f"{sys.argv[2]}/{file[0]}", file[1])
            if out != "NOT FOUND":     
                out = d[secrets.compare_digest(file[2], out)]
            print(f"{file[0]} {out}")