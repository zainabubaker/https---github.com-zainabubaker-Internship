import requests
import os
import zipfile
from io import BytesIO

MOODLE_URL = 'http://localhost'
TOKEN = 'dd0a42612742c518ad7d43ca195d2803'
COURSE_ID = '2'
DOWNLOAD_DIR = 'moodle_files'

def download_and_extract_zip(url, extract_to):
    print(f'Downloading ZIP file: {url}')
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with zipfile.ZipFile(BytesIO(response.content)) as zip_ref:
            zip_ref.extractall(extract_to)
        print(f'Extracted contents to: {extract_to}')
    except requests.exceptions.RequestException as e:
        print(f'Failed to download {url}: {e}')
    except zipfile.BadZipFile as e:
        print(f'Failed to extract ZIP file: {e}')

def download_course_files(course_id):
    url = f'{MOODLE_URL}/webservice/rest/server.php'
    params = {
        'wstoken': TOKEN,
        'wsfunction': 'core_course_get_contents',
        'moodlewsrestformat': 'json',
        'courseid': course_id
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    course_contents = response.json()
    if 'exception' in course_contents:
        print(f"Error: {course_contents['message']}")
        return

    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)

    print(f'Course Contents: {course_contents}')
    for section in course_contents:
        if 'modules' in section:
            for module in section['modules']:
                if 'contents' in module:
                    for content in module['contents']:
                        file_url = content['fileurl']
                        file_name = content['filename']
                        file_path = os.path.join(DOWNLOAD_DIR, file_name)
                        #Check if the file is zip
                        if file_name.endswith('.zip'):
                            download_and_extract_zip(f'{file_url}&token={TOKEN}', DOWNLOAD_DIR)
                        else:
                            download_file(f'{file_url}&token={TOKEN}', file_path)

def download_file(url, file_path):
    print(f'Downloading: {url}')
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f'Downloaded: {file_path}')
    except requests.exceptions.RequestException as e:
        print(f'Failed to download {url}: {e}')

def main():
    print(f'Current Working Directory: {os.getcwd()}')
    download_course_files(COURSE_ID)
    print(f'Files are downloaded to: {os.path.join(os.getcwd(), DOWNLOAD_DIR)}')

if __name__ == '__main__':
    main()