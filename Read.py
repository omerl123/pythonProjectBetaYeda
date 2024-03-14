def ReadDetails():
    with open('Details.txt', 'r') as r:
        for i in range(3):
            line = r.readline().strip()
            if not line:
                break
            else:
                if i == 0:
                    url = line.split(':', 1)[1]
                elif i == 1:
                    Email = line.split(':', 1)[1]
                elif i == 2:
                    Password = line.split(':', 1)[1]
    return(url, Email, Password)