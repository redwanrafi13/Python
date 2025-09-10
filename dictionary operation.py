students={
    "101": {"name": "Nishaj","age": "12","grade": "6"},
    "102": {"name": "Rahim","age": "13","grade": "7"},
    "103": {"name": "Karim","age": "12","grade": "6"}
}

print("original Dictionary")
print(students)

#accessing items

print("\n access student 101:", students["101"])
print("get with .get():", students.get("102") )

#adding items

students["104"]= {"name": "Hasan","age": "14","grade": "8"}
print("\n after adding new student")
print(students)

#UPDATING ITEMS

students["103"]["age"] = 13
print("\nAfter updating student 103's age:")
print(students)

#REMOVING ITEMS

#pop by key
removed= students.pop("102")
print("\nafter removed student 102:",removed )
print(students)

#DICTIONARY METHODS

print("\nKeys:", students.keys())
print("values:", students.values())
print("items:",students.items()) 