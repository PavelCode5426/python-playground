def get_urls():
    urls = []
    stop = False

    while not stop:
        url = input("URL: ")
        if url == "":
            stop = True
        else:
            urls.append(url)
    return urls
