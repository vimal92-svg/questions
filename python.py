#Write a function called split which will take two iterables as input - One called items and another called ratios. It should return an iterable of iterables which contains random elements from items in the proportions as indicated in ratios. You should round up or down to make sure all elements are there in the return value.
#answer
import random
import math

def split(items, ratios):
    result = []
    total_elements = len(items)
    total_ratios = sum(ratios)
    
    for ratio in ratios:
        num_elements = math.ceil(ratio / total_ratios * total_elements)
        selected = random.choices(items, k=num_elements)
        result.append(selected)
        items = [item for item in items if item not in selected]
        total_elements -= num_elements
        total_ratios -= ratio
    
    return result
#split([1,2,3,4,5,6,7,8,9,10], [0.5, 0.4, 0.1])
import random
import math

def split(items, ratios):
    result = []
    total_elements = len(items)
    total_ratios = sum(ratios)
    
    for ratio in ratios:
        num_elements = math.ceil(ratio / 100 * total_elements)
        selected = random.sample(items, k=num_elements)
        result.append(selected)
        items = [item for item in items if item not in selected]
        total_elements -= num_elements
        total_ratios -= ratio
    
    return result
#[[4,2,3,9,10], [1,5,6,8], [7]]
import random

def split(items, ratios):
    result = []
    total_elements = len(items)
    total_ratios = sum(ratios)

    for ratio in ratios:
        num_elements = round(ratio / total_ratios * total_elements)
        selected = random.sample(items, k=num_elements)
        result.append(selected)
        items = [item for item in items if item not in selected]
        total_elements -= num_elements
        total_ratios -= ratio

    return result

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ratios = [50, 40, 10]
result = split(items, ratios)
print(result)
# split([1,2,3,4,5,6,7,8,9,10], [0.25, 0.5, 0.25])
import random
import math

def split(items, ratios):
    result = []
    total_elements = len(items)
    total_ratios = sum(ratios)
    
    for ratio in ratios:
        num_elements = math.floor(ratio * total_elements)
        selected = random.sample(items, k=num_elements)
        result.append(selected)
        items = [item for item in items if item not in selected]
        total_elements -= num_elements
        total_ratios -= ratio
    
    return result

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ratios = [0.25, 0.5, 0.25]
result = split(items, ratios)
print(result)
# [[2,3,5], [1,4,6,7,9], [8,10]]
import random

def split(items, ratios):
    result = []
    total_elements = len(items)
    total_ratios = sum(ratios)
    
    for ratio in ratios:
        num_elements = round(ratio * total_elements)
        selected = random.sample(items, k=num_elements)
        result.append(selected)
        items = [item for item in items if item not in selected]
        total_elements -= num_elements
        total_ratios -= ratio
    
    return result

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ratios = [0.25, 0.5, 0.25]
result = split(items, ratios)
print(result)
#Write a function called split which will take two iterables as input - One called items and another called ratios. It should return an iterable of iterables which contains random elements from items in the proportions as indicated in ratios. You should round up or down to make sure all elements are there in the return value.
#1
import requests
from bs4 import BeautifulSoup
import urllib.parse
import os

# Define the URL of the webpage to scrape
url = "https://www.gettyimages.in/photos/aamir-khan-actor"

# Send a GET request to the URL and retrieve the webpage content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Create a directory to store the downloaded images
directory = "aamir_khan_images"
os.makedirs(directory, exist_ok=True)

# Find all the image elements on the webpage
image_elements = soup.find_all('img')

# Counter to keep track of downloaded images
counter = 1

# Loop through each image element and download the smaller image
for img in image_elements:
    # Get the source URL of the image
    img_url = img.get('src')
    
    # Ignore empty or non-image URLs
    if img_url and img_url.startswith("https://media.gettyimages.com/photos/") and img_url.endswith((".jpg", ".jpeg", ".png")):
        # Remove query parameters from the image URL
        img_url = urllib.parse.urlsplit(img_url)._replace(query='').geturl()
        
        # Download the image
        response = requests.get(img_url)
        
        # Generate the filename for the downloaded image
        filename = os.path.join(directory, f"aamir_khan_{counter}.jpg")
        
        # Save the image to the specified directory
        with open(filename, "wb") as file:
            file.write(response.content)
        
        print(f"Downloaded image {counter}")
        counter += 1

print("All images downloaded successfully!")
#2
import requests
from bs4 import BeautifulSoup
import urllib.parse
import os

# Define the URL of the webpage to scrape
url = "https://www.gettyimages.in/photos/aamir-khan-actor"

# Send a GET request to the URL and retrieve the webpage content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Create a directory to store the downloaded images
directory = "images"
os.makedirs(directory, exist_ok=True)

# Find all the image elements on the webpage
image_elements = soup.find_all('img')

# Counter to keep track of downloaded images
counter = 1

# Loop through each image element and download the smaller image
for img in image_elements:
    # Get the source URL of the image
    img_url = img.get('src')

    # Ignore empty or non-image URLs
    if img_url and img_url.startswith("https://media.gettyimages.com/photos/") and img_url.endswith((".jpg", ".jpeg", ".png")):
        # Remove query parameters from the image URL
        img_url = urllib.parse.urlsplit(img_url)._replace(query='').geturl()

        # Extract the pathname of the URL without the "/photos" prefix
        pathname = urllib.parse.urlsplit(img_url).path
        filename = os.path.join(directory, os.path.basename(pathname))

        # Download the image
        response = requests.get(img_url)

        # Save the image to the specified directory
        with open(filename, "wb") as file:
            file.write(response.content)

        print(f"Downloaded image {counter}")
        counter += 1

print("All images downloaded successfully!")
#3
import requests
from bs4 import BeautifulSoup
import urllib.parse
import os
import hashlib

# Define the URL of the webpage to scrape
url = "https://www.gettyimages.in/photos/aamir-khan-actor"

# Send a GET request to the URL and retrieve the webpage content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Create a directory to store the downloaded images
directory = "images"
os.makedirs(directory, exist_ok=True)

# Find all the image elements on the webpage
image_elements = soup.find_all('img')

# Counter to keep track of downloaded images
counter = 1

# Loop through each image element and download the smaller image
for img in image_elements:
    # Get the source URL of the image
    img_url = img.get('src')

    # Ignore empty or non-image URLs
    if img_url and img_url.startswith("https://media.gettyimages.com/photos/") and img_url.endswith((".jpg", ".jpeg", ".png")):
        # Remove query parameters from the image URL
        img_url = urllib.parse.urlsplit(img_url)._replace(query='').geturl()

        # Extract the pathname of the URL without the "/photos" prefix
        pathname = urllib.parse.urlsplit(img_url).path
        filename = os.path.join(directory, os.path.basename(pathname))

        # Download the image
        response = requests.get(img_url)

        # Save the image to the specified directory
        with open(filename, "wb") as file:
            file.write(response.content)

        # Calculate and print the checksum of the downloaded image
        checksum = hashlib.md5(response.content).hexdigest()
        print(f"Downloaded image {counter} - Checksum: {checksum}")
        counter += 1

print("All images downloaded successfully!")
#The attached file called unemployment-rate.csv contains a list of employment ratios for various countries for various years. Each entry looks like this
import argparse
import csv

def calculate_statistics(data, country, operation, from_year, to_year):
    filtered_data = [row for row in data if row['Country'] == country and from_year <= int(row['Year']) <= to_year]
    values = [float(row['Value']) for row in filtered_data]

    if operation == 'min':
        result = min(values)
    elif operation == 'max':
        result = max(values)
    else:
        result = sum(values) / len(values)

    return result

def main():
    parser = argparse.ArgumentParser(prog='statistics.py', description='Perform operations on data')
    parser.add_argument('--country', required=True, help='Country to perform operation for')
    parser.add_argument('-o', choices=['avg', 'min', 'max'], default='avg', help='Operation to perform on dates')
    parser.add_argument('--from', dest='from_year', type=int, required=True, help='Starting year (inclusive)')
    parser.add_argument('--to', dest='to_year', type=int, required=True, help='Ending year (inclusive)')
    parser.add_argument('input_file', help='Input file path')

    args = parser.parse_args()

    with open(args.input_file, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    result = calculate_statistics(data, args.country, args.o, args.from_year, args.to_year)
    print(f"Result: {result}")

if __name__ == '__main__':
    main()
