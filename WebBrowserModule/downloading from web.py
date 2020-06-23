import requests   # third party module for downloading the web pages and files

res = requests.get(r'https://automatetheboringstuff.com/files/rj.txt')    # returns response object
print(res.status_code)   # status of the download, 200 is success
print(res.headers['content-type'])   # returns the type of the content
res.raise_for_status()  # exception will be raised if the download is failed
print(res.text)    # returns the entire text content


# to copy the web content in a text file
webContent = open('myWebContent.txt', 'wb')
for chunk in res.iter_content(100000):
    print(len(chunk))
    webContent.write(chunk)



