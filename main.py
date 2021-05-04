import pandas as pd # pip install pandas
from faker import Faker # pip install Faker
from collections import defaultdict
# import random


# first initialize our Faker instance that we’ll be using to get our dummy data
fake = Faker()
# input a number & file name
xRows = int(input("Enter number of rows: "))
xName = (input("Please enter table name: "))

#fake = Faker(["fr_FR", "it_IT", "de_DE", "el_GR"])
# we’ll use fake_data to create our dictionary. defaultdict(list) will create a dictionary that will create key-value pairs that are not currently stored within the dictionary when accessed. Essentially, you do not need to define any keys within your dictionary
fake_data = defaultdict(list)
# let’s decide on the kind of data that we’re going to take from the Faker instance to be stored in the fake variable
# loop a thousand times to access these methods and then add them to our dictionary
for i in range(xRows):
    fake_data["first_name"].append( fake.first_name() )
    fake_data["last_name"].append( fake.last_name() )
    fake_data["occupation"].append( fake.job() )
    fake_data["dob"].append( fake.date_of_birth() )
    fake_data["country"].append( fake.country() )
    fake_data["city"].append( fake.city() )

# Now, since we have all our random data within our dictionary fake_data. We need to package this data into our pandas dataframe
df_fake_data = pd.DataFrame(fake_data)
# Save the generated list to a csv with no index
df_fake_data.to_csv("{}.csv".format(xName),index=False)
