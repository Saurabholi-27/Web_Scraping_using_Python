# This program take the url from the client and scrap the data form the booking.com

#importing important libraries
import requests
from bs4 import BeautifulSoup
import lxml
import csv
import time
import random


#Testing url's
#url_text = 'https://www.booking.com/searchresults.en-gb.html?ss=Gurgaon&ssne=Gurgaon&ssne_untouched=Gurgaon&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaGyIAQGYAQm4ARfIAQzYAQHoAQGIAgGoAgO4Ap3z374GwAIB0gIkNGY0ZjgyYTctOTkyZi00Mzk3LWJkYjgtMzkzYzQ0YmVmYWVj2AIF4AIB&sid=09a56be760ee16d1d27e38fa6908bba1&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=-2096897&dest_type=city&checkin=2025-04-02&checkout=2025-04-03&group_adults=2&no_rooms=1&group_children=0'
#mumbai_url = 'https://www.booking.com/searchresults.en-gb.html?ss=Mumbai%2C+Maharashtra%2C+India&ssne=Gurgaon&ssne_untouched=Gurgaon&label=gen173nr-1BCAEoggI46AdIM1gEaGyIAQGYAQm4ARfIAQzYAQHoAQGIAgGoAgO4AsKU5L4GwAIB0gIkNTU4ZjQzOGItZjE5Yy00YzA5LTk4MjQtYTIyNDk2OTI5NzVl2AIF4AIB&sid=09a56be760ee16d1d27e38fa6908bba1&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=-2092174&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=01ee2961a1b70644&ac_meta=GhAwMWVlMjk2MWExYjcwNjQ0IAAoATICZW46A211bUAASgBQAA%3D%3D&checkin=2025-04-02&checkout=2025-04-03&group_adults=2&no_rooms=1&group_children=0'

# Define a function for scraping
def web_scrapper1(web_url, f_name):
    
    #greetings to the user
    print("Thank you sharing the url and file name!\n⌛\nReading the content")
    
    #processing/scraping the url
    num = random.randint(3,7)
    time.sleep(num)

    #requesitng to server
    header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
    response = requests.get(web_url, headers=header)

    #checking the connection
    if response.status_code == 200:
        print("Connected to the website")
        html_content = response.text


        #creating Soup
        soup = BeautifulSoup(html_content,'lxml')


        #main container
        hotel_divs = soup.find_all('div' , role="listitem")

        with open(f'{file_name}.csv', 'w', encoding = 'utf-8') as file_csv:
            writer = csv.writer(file_csv)

            #adding header
            writer.writerow(['Hotel_Name', 'Locality', 'Price', 'Rating', 'Score', 'Review', 'Link'])

        #logic for scraping
            for hotel in hotel_divs:
                hotel_name = hotel.find('div', class_="f6431b446c a15b38c233").text.strip()
                hotel_name if hotel_name else "N/A" # If not found, set rating to "N/A"

                location = hotel.find('span', class_="aee5343fdb def9bc142a").text.strip()
                location if location else "N/A" # If not found, set rating to "N/A"

                price = hotel.find('span', class_="f6431b446c fbfd7c1165 e84eb96b1f").text.replace('₹ ', '')
                price if price else "N/A" # If not found, set rating to "N/A"

                rating_element = hotel.find('div', class_="a3b8729ab1 e6208ee469 cb2cbb3ccb") # Assign the result of find to a variable
                rating = rating_element.text.strip() if rating_element else "N/A" # If not found, set rating to "N/A"

                score_element = hotel.find('div', class_="a3b8729ab1 d86cee9b25") # Assign the result of find to a variable
                score = score_element.text.strip().split(' ')[-1] if score_element else "N/A" # If not found, set rating to "N/A"

                review_element = hotel.find('div', class_="abf093bdfe f45d8e4c32 d935416c47")  # Assign the result of find to a variable
                review = review_element.text.strip().split(' ')[0] if review_element else "N/A" # Check if the element was found before accessing .text

                link = hotel.find('a', href=True).get('href') 
                link if link else "N/A" # If not found, set rating to "N/A"

                #saving the file in csv
            
                writer.writerow([hotel_name, location, price, rating, score, review, link])


    else:
        print(f"Connection Failed!{response.status_code}")


#if using this script directly than below code will be excuted
if __name__== '__main__':

    url = input("Please enter url! :")
    file_name = input("Please enter the file name! :")

    #calling the function
    web_scrapper1(url, file_name)