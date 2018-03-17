#person = ["Quy", 20, 0, "Ha Noi", "Vinh Phuc", 3, 10, ["Coding", "Manga", "Ping pong"]]

#dictionary
#create
person = {}
person = {
#key : value
"name" : "Quy",
"age" : 20,
"ex" : 0,
"sex" : "male"
}

#read
# key = "age"
# if key in person:
#     print(person[key])
# else:
#     print('Not found')

# for value in person.values():
#     print(value)

# for key, value in person.items():
#     print(key, value)


#update:
person['age'] += 3
print(person)

#add:
person['school'] = 'Hust'
# print(person)
