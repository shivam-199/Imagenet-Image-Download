import requests
import shutil
import time
from requests.exceptions import ConnectionError
with open("urls.txt") as f:
	count = 0
	for line in f:
		try:
		#start_time = time.time()
			r = requests.get(line, stream = True, headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
		    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
		    'Accept-Encoding': 'none',
		    'Accept-Language': 'en-US,en;q=0.8',
		    'Connection': 'keep-alive'})
		    #elasped_time = time.time() - start_time
			if r.status_code == 200:
				with open(str(count), 'wb') as f:
					r.raw.decode_content = True
					shutil.copyfileobj(r.raw, f)
					count = count + 1
		except ConnectionError:
			continue
close(file)

