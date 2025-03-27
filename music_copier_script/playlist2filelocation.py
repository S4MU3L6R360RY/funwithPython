from bs4 import BeautifulSoup

def extract_text_from_html(xml_file, txt_file):
    # Read the XML/HTML content from the file
    with open(xml_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Use BeautifulSoup to parse the content and extract text
    soup = BeautifulSoup(content, 'html.parser')
    text = soup.get_text()

    # Save the extracted text into a .txt file
    with open(txt_file, 'w', encoding='utf-8') as file:
        file.write(text)

if __name__ == "__main__":
    xml_file = '&myplaylistforwork.xspf'  # Replace with your HTML/XML file path
    txt_file = 'music_files.txt'    # Replace with your desired output file path

    extract_text_from_html(xml_file, txt_file)
    print(f"Text content extracted and saved to {txt_file}")
