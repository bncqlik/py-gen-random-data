import pandas as pd # pip install pandas
from faker import Faker # pip install Faker
from collections import defaultdict
import random

# https://faker.readthedocs.io/en/master/providers/baseprovider.html
# Providers: https://github.com/fzaninotto/Faker#faker-internals-understanding-providers
# first initialize our Faker instance that we’ll be using to get our dummy data
fake = Faker()
# fake = Faker(["fr_FR", "it_IT", "de_DE", "el_GR"]) # for using specific locale(s)

# input a number & file name
xRows = int(input("Enter number of rows: "))
xName = input("Please enter table name: ")

# we’ll use fake_data to create our dictionary. defaultdict(list) will create a dictionary that will create key-value pairs that are not currently stored within the dictionary when accessed. Essentially, you do not need to define any keys within your dictionary
fake_data = defaultdict(list)

# let’s decide on the kind of data that we’re going to take from the Faker instance to be stored in the fake variable
# loop a thousand times to access these methods and then add them to our dictionary
for _ in range(xRows):
    # fake random locale in every row
    # https://stackoverflow.com/questions/65504692/get-random-locale-with-python-faker-lib
    # random.choices(fake.locales)[0]
    
    #fake_data["first_name"].append( fake.first_name() )
    #fake_data["last_name"].append( fake.last_name() )
    fake_data["full_name"].append( fake.name() )
    fake_data["occupation"].append( fake.job() )
    #fake_data["dob"].append( fake.date_of_birth() )
    fake_data["city"].append( fake.city() )
    fake_data["postcode"].append( fake.postcode() )
    #fake_data["street_address"].append( fake.street_address() )
    fake_data["country"].append( fake.country() )
    fake_data["country_code"].append( fake.country_code() )
    fake_data["license_plate"].append( fake.license_plate() )
    #fake_data["iban"].append( fake.iban() )
    #fake_data["swift"].append( fake.iban() )  # (length=None, primary=None, use_dataset=False) eg.fake.swift(length=8, use_dataset=True)
    #fake_data["ean"].append( fake.ean() )  # like barcode eg. ean(length=13, prefixes=('45', '49'))
    #fake_data["color_name"].append( fake.color_name() )
    fake_data["company"].append( fake.company() )
    #fake_data["bs"].append( fake.bs() ) # Bases: faker.providers.BaseProvider
    #fake_data["company_suffix"].append( fake.company_suffix() ) # eg. example ‘Ltd’
    fake_data["credit_card_number"].append( fake.credit_card_number() )
    #fake_data["credit_card_security_code"].append( fake.credit_card_security_code() )
    #fake_data["credit_card_provider"].append( fake.credit_card_provider() )
    fake_data["credit_card_expire"].append( fake.credit_card_expire() )
    #fake_data["cryptocurrency_name"].append( fake.cryptocurrency_name() )
    #fake_data["currency_name"].append( fake.currency_name() )
    fake_data["pricetag"].append( fake.pricetag() )
    #fake_data["date"].append( fake.date() ) # date(pattern='%Y-%m-%d', end_datetime=None)
    fake_data["date_between"].append( fake.date_between(start_date='-5y', end_date='today') )
    #fake_data["date_this_century"].append( fake.date_this_century(before_today=True, after_today=False) )
    #fake_data["date_time_between_dates"].append( fake.date_time_between_dates(datetime_start=None, datetime_end=None, tzinfo=None) )
    #fake_data["file_path"].append( fake.file_path(depth=3, category='video') )
    #fake_data["coordinate"].append( fake.coordinate() )
    fake_data["latitude"].append( fake.latitude() )
    fake_data["longitude"].append( fake.longitude() )
    #fake_data["local_latlng"].append( fake.local_latlng(coords_only=False) )  
    #fake_data["company_email"].append( fake.company_email() )
    fake_data["email"].append( fake.email(domain=None) )
    #fake_data["domain_name"].append( fake.domain_name(levels=1) )
    #fake_data["hostname"].append( fake.hostname(levels=1) )
    #fake_data["image_url"].append( fake.image_url(width=None, height=None) )
    #fake_data["ipv4"].append( fake.ipv4(network=False, address_class=None, private=None) )
    #fake_data["ipv6"].append( fake.ipv6(network=False) )
    #fake_data["safe_domain_name"].append( fake.safe_domain_name() )
    #fake_data["uri"].append( fake.uri() )
    fake_data["user_name"].append( fake.user_name() )
    #fake_data["isbn10"].append( fake.isbn10(separator='-') )
    fake_data["paragraph"].append( fake.paragraph(nb_sentences=2) )
    #fake_data["text"].append( fake.text(max_nb_chars=200, ext_word_list=None) )
    #fake_data["binary"].append( fake.binary(length=1048576) )
    #fake_data["boolean"].append( fake.boolean(chance_of_getting_true=50) )
    fake_data["phone_number"].append( fake.phone_number() )
    #fake_data["ssn"].append( fake.ssn() )
    #fake_data["android_platform_token"].append( fake.android_platform_token() )
    fake_data["user_agent"].append( fake.user_agent() )
    #fake_data["windows_platform_token"].append( fake.windows_platform_token() )




# Now, since we have all our random data within our dictionary fake_data. We need to package this data into our pandas dataframe
df_fake_data = pd.DataFrame(fake_data)
# Save the generated list to a csv with no index
df_fake_data.to_csv("{}.csv".format(xName),index=False)
