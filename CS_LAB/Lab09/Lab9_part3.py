from Date import Date

if __name__ == "__main__":
    file = open('birthdays.txt')
    birthday_list = []
    lines = file.readlines()
    for line in lines:
        temp = line.split()
        tempD = Date(int(temp[0]),int(temp[1]),int(temp[2]))
        birthday_list.append(tempD)

    early = birthday_list[0]
    late = birthday_list[0]
    most = 13*[0]
    for d in birthday_list:
        if(d < early):
            early = d
        if(late < d):
            late = d
        most[int(d.month)] += 1

    print(early.__str__())
    print(late.__str__())
    print(most.index(max(most)))
    