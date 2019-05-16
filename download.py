import sys
import requests


def download(url, filename):
    with open(filename, 'wb') as f:
        response = requests.get(url, stream=True)
        total = response.headers.get('content-length')

        if total is None:
            f.write(response.content)
        else:
            downloaded = 0
            total = int(total)
            for data in response.iter_content(chunk_size=max(int(total/1000), 1024*1024)):
                downloaded += len(data)
                f.write(data)
                done = int(50*downloaded/total)
                sys.stdout.write('\r[{}{}][{} of {} ({}%)]'
                                 .format('█' * done, '.' * (50-done),
                                         downloaded/1000, total/1000, done*2))
                sys.stdout.flush()
    sys.stdout.write('\n')