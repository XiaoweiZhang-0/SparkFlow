from faker import Faker

## This function will generate fake twitter post data for testing
## TODO: Add more data types(1.userName, 2.dateTime, 3.text)
def generate_data():
    fake = Faker(use_weighting=True)
    ## Set seed to get the same data every time
    Faker.seed(4321)

    for _ in range(100):
        print(
            'name:', fake.name(),
            'created_at:', fake.date_time_this_month(),
            'text:', fake.text(),
        )

## generate_data()