import requests
import re


def get_chapter_list(url):

    if url == "":
        url = "https://bato.to/series/7606"
    
    response = requests.get(url)
    # Extraire tous les liens de chapitres du HTML
    chapter_links = re.findall(
        r'<a href="(/chapter/\d+)" class="visited chapt"><b>(.*?)</b>.*?</a>',
        response.text
    )
    return chapter_links


def extract_href_and_b_content(a_tag):
    # Utilise une expression régulière pour extraire href et le contenu de <b>
    href_match = re.search(r'href="([^"]+)"', a_tag)
    b_content_match = re.search(r'<b>(.*?)</b>', a_tag)
    href = href_match.group(1) if href_match else None
    b_content = b_content_match.group(1) if b_content_match else None
    return href, b_content

def download_images_from_chapter():
    str = requests.get("https://bato.to/chapter/144497")

    match = re.search(r'const imgHttps = \[(.*?)\];', str.text, re.DOTALL)
    if match:
        str = match.group(1)
        str.replace("const imgHttps =[", "")
        str.replace("]", '')
        tab = str.split(",")
        
        for i in tab:
            response = requests.get(i.strip().strip('"'))
            with open(f'image_{tab.index(i)}.jpg', 'wb') as f:
                f.write(response.content)
        print("Images downloaded successfully")
    else:
        print("Not found")

# Exemple d'utilisation :


chapters = get_chapter_list("")

for item in chapters:
    href, b_content = extract_href_and_b_content(item)
    print("href:", "https://bato.to" + href)
    print("b_content:", b_content)