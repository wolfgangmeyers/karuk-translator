import requests
from bs4 import BeautifulSoup
import json

# specific url looks like https://linguistics.berkeley.edu/~karuk/karuk-texts.php?text-id=ALK_14-35
def get_url(text_id):
    return f"https://linguistics.berkeley.edu/~karuk/karuk-texts.php?text-id={text_id}"

def extract_text_ids(html_content):
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all table rows in the table
    rows = soup.find_all('tr')

    text_ids = []

    for row in rows:
        tds = row.find_all('td')
        if len(tds) >= 5:
            text_id_td = tds[4]
            text_id = text_id_td.get_text(strip=True)
            text_ids.append(text_id)

    return text_ids

def parse_translations(html_content: str):
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all table rows in the table
    rows = soup.find_all('tr')

    translations = []

    for row in rows:
        tds = row.find_all('td')
        if len(tds) >= 4:
            karuk_td = tds[1]
            english_td = tds[3]

            # Extract text from Karuk td, stripping out <b> tags
            karuk_text = ''.join(karuk_td.stripped_strings)

            # Extract text from English td
            english_text = english_td.get_text(strip=True)

            # Add the translation to the list
            # translations.append([karuk_text, english_text])
            translations.append({
                'karuk': karuk_text,
                'english': english_text
            })

    return translations

def parse_translations2(html_content):
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    
    translations = []

    # Find all tables in the content
    tables = soup.find_all('table')
    
    for table in tables:
        rows = table.find_all('tr')
        if len(rows) >= 2:
            # karuk_td = rows[0].find('td', align='left')
            english_td = rows[1].find('td', align='left')

            # Extract Karuk text, stripping out <b> tags
            karuk_span = rows[0].find('span', class_='karuk')
            karuk_text = ''.join(karuk_span.stripped_strings) if karuk_span else ""

            # Extract English text
            english_text = english_td.get_text(strip=True) if english_td else ""

            # Add the translation to the list
            translations.append({
                'karuk': karuk_text,
                'english': english_text
            })

    return translations

def main():
    # this page has the text ids
    index_url = "https://linguistics.berkeley.edu/~karuk/karuk-texts.php?list=yes&full-list=yes"
    # fetch the html
    index_html = requests.get(index_url).text
    # extract the text ids
    text_ids = extract_text_ids(index_html)[1:]
    
    all_translations = []
    for text_id in text_ids:
        url = get_url(text_id)
        html_content = requests.get(url).text
        translations = parse_translations(html_content)
        if len(translations) == 0:
            translations = parse_translations2(html_content)
        print(f"Scraped {len(translations)} translations from {url}")
        all_translations.extend(translations)
        # break # remove this line to scrape all translations
    with open("karuk-translator-ui/src/translations.json", "w", encoding="utf-8") as f:
        json.dump(all_translations, f, indent=4, ensure_ascii=False)
    print(f"Saved {len(all_translations)} translations to src/translations.json")

if __name__ == '__main__':
    main()
    # html_content = requests.get("https://linguistics.berkeley.edu/~karuk/karuk-texts.php?text-id=CT-01").text
    # translations = parse_translations2(html_content)
    # for translation in translations:
    #     print(translation)

