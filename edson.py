from faker import Faker

mike = Faker()
for i in range(10):
    print(mike.name(), mike.date_of_birth(), mike.address())
