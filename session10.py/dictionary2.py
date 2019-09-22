person = {
    "name": "Pham Cao Duy",
    "age": 16,
}
print(person)
person["age"] += 1
print(person)
a = ("key 'name' exists in my dictionary -")
b = ("key 'nationality'does not exist in my dictionary -")
if 'name' in person:
    print(a,"true")
    if 'nationality' not in person:
        print(b,"true")