def form(name, surname, year_of_birth, city, email, phone):
    return f"Name is {name} Surname is {surname} Year of birth is {year_of_birth} City is {city} Email is {email} Phone is {phone}"


print(form(name="John", surname="Anderson", year_of_birth="1990", city="Minneapolis", email="john@gmail.com",
           phone="555 555 55"))
