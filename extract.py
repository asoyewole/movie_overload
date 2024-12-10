import requests
import os
import gzip
import shutil


def download(url, file_path):
    '''Function to extract movie data in its raw zipped form and save in a specified path
    PARAMETERS
    url - url for the compressed file to be downloaded
    file_path - path to save the compressed file
    '''

    with open(file_path, 'wb') as f:
        r = requests.get(url)
        f.write(r.content)
    print(f'downloaded {file_path} successfully')


def decompress(zipped_file_path, dest_file_path):
    with gzip.open(zipped_file_path, 'rb') as f_in:
        with open(dest_file_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    print(f'file {dest_file_path.split("/")[-1]} extracted successfully')



# URL strings for all the warehouse files
url_str = "https://datasets.imdbws.com/"

files = ['name.basics',
         'title.akas',
         'title.basics',
         'title.crew',
         'title.episode',
         'title.principals',
         'title.ratings']

extension = ".tsv.gz"


# List comprehension of urls
url_path = [url_str+file+extension for file in files]

# create file paths to download into
file_path_start = os.path.join('data', 'zipped_data')
file_path_end = [f'{file}{extension}' for file in files]
file_path = [os.path.join(file_path_start, path_end)
             for path_end in file_path_end]

url_file_dict = dict(zip(url_path, file_path))

# For key, value in dict: a = key, b = key[value]
for url in url_file_dict:
    download(url=url, file_path=url_file_dict[url])

# create filepaths to extract into
dest = os.path.join('data', 'extracted_data')
dest_file_path = [f'{file}.tsv' for file in files]
dest_file_path = [os.path.join(dest, file) for file in dest_file_path]
                
file_path_dict = dict(zip(file_path, dest_file_path))

for files in file_path_dict:
    decompress(files, file_path_dict[files])


