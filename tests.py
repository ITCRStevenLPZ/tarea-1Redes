with open('Inbox/passwords.txt', "rb") as f:
    for line in f:
        line = line.rstrip()
        print(line)
        parts = line.split(b":")
        print(parts)