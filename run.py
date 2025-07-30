import requests
import re
import os
import zipfile


def extract_href_and_b_content(url):
    if url == "":
        url = "https://bato.to/series/7606"
    
    response = requests.get(url)
    # Extraire tous les liens de chapitres du HTML
    text = response.text.replace("\n","")
    match = re.findall(r'<a class="visited chapt" href="(/chapter/\d+)"[^>]*>\s*<b>(.*?)</b>.*?</a>', text, re.DOTALL)
    return match

def download_images_from_chapter(url, chapter_number):
    
    # Create a directory for the chapter
    directory_name = f"chapter_{chapter_number}"
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    else:
        print(f"Directory '{directory_name}' already exists.")
        # Remove all files in the directory
        for file in os.listdir(directory_name):
            file_path = os.path.join(directory_name, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted file: {file_path}")

    str = requests.get(url)

    match = re.search(r'const imgHttps = \[(.*?)\];', str.text, re.DOTALL)
    if match:
        str = match.group(1)
        str.replace("const imgHttps =[", "")
        str.replace("]", '')
        tab = str.split(",")
        
        for i in tab:
            response = requests.get(i.strip().strip('"'))
            with open(f'{directory_name}/{tab.index(i)+1:03d}.jpg', 'wb') as f:
                f.write(response.content)
        print("Images downloaded successfully")
    else:
        print("Not found")

def create_cbz_from_directory(directory_name):
    
    if not os.path.exists("cbz"):
        os.makedirs("cbz")
    
    cbz_filename = f"{cbz}/{directory_name}.cbz"
    with zipfile.ZipFile(cbz_filename, 'w') as cbz:
        for root, _, files in os.walk(directory_name):
            for file in sorted(files):
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, directory_name)
                cbz.write(file_path, arcname)
    print(f"CBZ file '{cbz_filename}' created successfully.")



chapters = extract_href_and_b_content("")
for item in chapters:
    href = item[0]
    b_content = item[1].replace("Chapter ", "")
    print(f"Téléchargement du chapitre {b_content}")
    download_images_from_chapter("https://bato.to" + href,b_content)

for chapter in os.listdir():
    if os.path.isdir(chapter) and chapter.startswith("chapter_"):
        create_cbz_from_directory(chapter)