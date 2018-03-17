dic = {
"eny" : "Em người yêu",
"any" : "Anh người yêu",
"cl" : "con lợn",
"hc" : "học",
"ik" : "đi",
}
while True:
    search = input('Your code: ')
    if search in dic:
        print(dic[search])
    else:
        print('Not found')
        choice = input(' Would you like to update? Y or N?:').lower()
        if choice == 'y':
            dic[search] = input('Meaning: ')
            print(dic)
        else:
            break
