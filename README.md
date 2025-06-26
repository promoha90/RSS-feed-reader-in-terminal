# 📰 RSS News Reader (Python)

A simple RSS feed reader written in Python. This script lets you input multiple RSS feed URLs and choose how many articles you'd like to see from each one. It fetches and parses the feed, displaying key information from each article in the console.

## 📌 Features

- Accepts multiple RSS URLs entered manually by the user.
- Handles connection and XML parsing errors gracefully.
- Allows user-defined number of articles per feed.
- Displays article title, link, description, creator (if available), and publication date.
- Shows any errors encountered during feed processing.

## 💻 Requirements

- Python 3.6+
- [`requests`](https://pypi.org/project/requests/) library (Install it via: `pip install requests`)

## 🚀 How to Use

1. Clone the repository or download the script:

```bash
git clone https://github.com/promoha90/rss-feed-reader-in-terminal.git
cd rss-feed-reader-in-terminal
```

2. Enter one or more RSS feed URLs when prompted.

```bash
python main.py
```

3. Press Enter without typing anything to finish entering URLs.

4. Enter the number of articles you want to display per feed.

5. The script will display each article's details in the terminal.

### EXAMPLE
```bash
Introduce an rss url (When finished, press enter): https://example.com/rss.xml
Introduce an rss url (When finished, press enter): 

Introduce a number of articles you want to see from each url: 3

Title:  Latest Tech News
Link:   https://example.com/article1
Description:  A summary of the most recent innovations...
Creator:  John Doe
Publication Date:  Thu, 20 Jun 2024 10:00:00 GMT
----------------------------------------
```

## ⚠️ Notes
The script does not require URLs to end in .xml, as long as the content is valid RSS.

Some feeds may not include all fields (e.g., <creator> or <description>); in those cases, "N/A" will be displayed.

Invalid URLs or connection issues will be reported after processing all feeds.

## 🧪 Sample RSS Feeds to Try
[BBC News](https://feeds.bbci.co.uk/news/rss.xml)

[NYT](https://rss.nytimes.com/services/xml/rss/nyt/World.xml)

## 📄 License
This project is licensed under the MIT [License](/LICENSE). See the LICENSE file for details.
