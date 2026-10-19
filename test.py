from datetime import date

birth_date = str(date(1996, 7, 15))

print(type(birth_date))

print(birth_date)

file = open("test.txt", "w")

file.write(birth_date)

file.close()

date_text = "1996-07-15"

date_parts = date_text.split("-")

birth_date = date(
    int(date_parts[0]),
    int(date_parts[1]),
    int(date_parts[2])
)

print(birth_date)