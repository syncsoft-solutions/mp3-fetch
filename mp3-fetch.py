"""
Downloads all mp3 file from a given web page.
"""
from bs4 import BeautifulSoup, SoupStrainer
import requests
from six.moves import urllib
import os, shutil
import sys
import warnings
import download

warnings.filterwarnings("ignore", category=UserWarning, module='bs4')


if __name__ == '__main__':
    args = sys.argv
    if len(args) < 3:
        print('Wrong number of inputs. Please specify the url then the folder to save the mp3 files.')
    else:
        url = args[1]
        dir_path = os.getcwd()
        sub_folder = os.path.join(args[2])

        page = requests.get(url)

        if os.path.isdir(sub_folder):
            pass
        else:
            os.mkdir(sub_folder)

        data = page.text

        print('Download started...')
        print('Downloading files to ' + args[2])

        soup = BeautifulSoup(data, features="html.parser")

        filenames = []
        for link in soup.find_all('a'):
            li = link.get('href')
            ext = li[len(li) - 3:]

            if ext == 'mp3':
                download_link = url + li
                # Download the file
                fname = sub_folder + li
                # filename, headers = urllib.request.urlretrieve(download_link)
                download.download(download_link, os.path.join(sub_folder, li))
                # os.rename(filename, os.path.join(sub_folder, li))
                print('Music downloaded successfully: ' + li)
