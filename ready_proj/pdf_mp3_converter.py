from gtts import gTTS
import pdfplumber
from art import tprint
from pathlib import Path


def pdf_to_mp3_conv(filepath: str = r"D:\Video courses\GB Python\Django\2\Лекция 2. Методичка.pdf",
                    language: str = 'ru'):
    if Path(filepath).is_file() and Path(filepath).suffix == '.pdf':
        print(f'[+] Original file: {Path(filepath).name}')
        print('[+] Processing')

        with pdfplumber.open(filepath) as pdf:
            all_pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(all_pages).replace('\n', '')
        audio = gTTS(text=text, lang=language)
        filename = Path(filepath).stem
        audio.save(f'{filename}.mp3')

        return f'File {Path(filepath).name} was successfully saved! Congratulations!'

    else:
        return f'{Path(filepath).stem} does not exist! Check the path!'


def main():
    tprint('PDF>>TO>>MP3', font='bulkhead')
    file = input('\nEnter the path to your file: ')
    language = input("\nChoose the language, for example 'en' or 'ru': ")
    print(pdf_to_mp3_conv(filepath=file, language=language))


if __name__ == '__main__':
    main()
