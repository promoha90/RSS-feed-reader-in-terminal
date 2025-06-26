import xml.etree.ElementTree as ET
import requests

def main():
    # Ask for URL
    urls = []
    invalids = []

    while True:
        url = input("Introduce an rss url (When finished, press enter): ")
        if not url:
            break
        urls.append(url)
    
    # Check if the integer is valid
    while True:
        numberOfNews = input("Introduce a number of articles you want to see from each url: ")
        try:
            numberOfNews = int(numberOfNews)
            if numberOfNews < 1:
                raise ValueError 
            break
        except ValueError:
            print("Please, introduce a valid integer number.")
    
    cnt = 0

    for url in urls:
        available = True

        # Request the page
        try:
            req = requests.get(url)
            req.raise_for_status()
            root = ET.fromstring(req.content)
        except Exception as e:
            invalids.append(e)
            available = False
            continue

        if available == True:
            channel = root.find('channel')
            items = channel.findall('item')

            # Print the articles
            for item in items[:numberOfNews]:
                title = item.find('title')
                link = item.find('link')
                description = item.find('description')
                creator = item.find('creator')
                pubDate = item.find('pubDate')

                print("Title: ", title.text if title is not None else "N/A")
                print("Link: ", link.text if link is not None else "N/A")
                print("Description: ", description.text if description is not None else "N/A")
                print("Creator: ", creator.text if creator is not None else "N/A")
                print("Publication Date: ", pubDate.text if pubDate is not None else "N/A")

                print("-" * 40)

                cnt += 1
    
    for invalidUrl in invalids:
        print(invalidUrl)
    
    if cnt < numberOfNews:
        print("Max articles available:", cnt)
    
   
if __name__ == "__main__":
    main()