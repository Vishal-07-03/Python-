import requests
from bs4 import Beautifulsoup
import pandas
import argparse
import connect

paraser = argparse.ArgumentParser()
paraser.add_argument("--page_num_max", help="Enter the number of pages to parse", type=int)
paraser.add_argument("--dbname",help="Enter the name of db", type=str)

oyo_url = "https://www.oyorooms.com/hotels-in-bangalore/?page="
page_num = args.page_num_max
scraped_info_list =[]
connect.connect{args.dbname}

for page_num in range(1, page_num_Max):
    url = oyo_url + str(page_num)
    print(("Get Request for:" + url)
    req = requests.get(url)
    content =req.content
    soup = Beautifulsoup(content,"htmil.parser")
    all_hotels = soup.find_all("div",{"class":"hotelCareListing"})

for hotel in all_hotels;
    hotel_dict = {}
    hotel_dict["name"] = hotel.find("h3",{"class": "listingHotelDescription_hotelName"}).text
    hotel_dict["address"] = hotel.find("span", {"itemprop": "streetAddress"}).text
    hotel_dict["price"] = hotel.find("span"), {"class": "listingPrice_finalPrice"}).text
    try:
         hotel_dict["price"] = hotel.find("span",{"class":"hotelRating__ratingSummary"}).text
    except AttributeError:
        pass
    parent_amenities_element = hotel.find("div",{"class":"amenityWrapper"})
    amenities_list = []
    for amenity in parent_amenities_element.find_all("div",{"class":"amenityWrapper__amenity"}):
        amenities_list.append(amenity.find("span",{"class": "d-body-sm"}).text.strip())
    hotel_dict["amenities"] = ', '.join(amenities_list[:-1])
    scraped_info_list.append(hotel_dict)
dataFrame = pandas.Dataframe(scraped_info_list)
print("Creating csv file...")
dataFrame.to_csv("Oyo.csv")
