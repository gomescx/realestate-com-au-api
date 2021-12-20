
from realestate_com_au import RealestateComAu

api = RealestateComAu()

# Get property listings
# listings = api.search(locations=["seventeen seventy, qld 4677"], channel="buy", keywords=["tenant"], exclude_keywords=["pool"])
listings = api.search(locations=["Braddon, ACT 2612"], channel="buy")

import csv

field_names = ['id', 'url', 'suburb', 'state', 'postcode', 'short_address', 'full_address', 'property_type', 'price', 'bedrooms', 'bathrooms', 'parking_spaces', 'building_size', 'building_size_unit', 'land_size', 'land_size_unit', 'listing_company_id', 'listing_company_name', 'listing_company_phone', 'auction_date', 'sold_date', 'description']
with open('Listings.csv', 'w', newline='', encoding="utf-8") as csvfile:
    dict_writer = csv.writer(csvfile)
    dict_writer.writerow(field_names)
    for d in listings: 
        dict_writer.writerow(d.__dict__.values())