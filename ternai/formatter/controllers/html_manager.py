import json
import time
from bs4.element import Comment
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


#This handles loading the site in Selenium and getting the html 
def process_website(url:str): 
    #We have a URL let's make it happen
    raw_html = load_html(url=url)
    html_text = text_from_html(raw_html)
    return html_text

#use selenium to get the HTML
def load_html(url:str): 
    # Options for the Chrome driver
    options = Options()

    # Disable JavaScript and images
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_argument("--headless=new")
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(3)
    page_source = driver.page_source
    return page_source



def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = bs4.BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  

    return_text = ""
    for item in visible_texts: 
         
         item = item.strip()
         if item != "":
            return_text = return_text + " " + item.strip()

    return return_text


def remove_newline_elements(html:str): 
    # Fetch the HTML content of the webpage
    soup = bs4.BeautifulSoup(html, 'html.parser')

    def clean_element(element):
        # Recursively remove elements containing only a newline
        for child in list(element.children):
            if isinstance(child, str) and child.strip() == "":
                # Remove string if it's only whitespace or a newline
                child.extract()
            elif child.name:
                # Recursively clean child elements
                clean_element(child)

    clean_element(soup)
    return str(soup)

#Pull out everything but the HTML tags that add context
def get_clean_html(url):
    # Fetch the HTML content of the webpage
    
    soup = bs4.BeautifulSoup(url, 'html.parser')

    def process_element(element):
        # Skip processing the head and footer elements
        if element.name in ['head', 'footer']:
            return ""

        output = ""
        if element.name:
            # Include the tag name and class names if specified
            class_names = " ".join(element.get("class", []))
            if class_names:
                output += f"<{element.name} class='{class_names}'>\n"
            else:
                output += f"<{element.name}>\n"

        for child in element.children:
            if isinstance(child, str):
                # Directly include non-empty strings
                child_text = child.strip()
                if child_text:
                    output += child_text + "\n"
            else:
                # Recursively process child elements
                child_output = process_element(child)
                if child_output.strip():
                    # Include child output only if it's not empty
                    output += child_output

        if element.name:
            # Close the tag
            output += f"</{element.name}>\n"
        return output

    clean_html = process_element(soup)
    clean_html = remove_newline_elements(clean_html)

    return clean_html
