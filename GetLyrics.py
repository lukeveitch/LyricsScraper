from bs4 import BeautifulSoup
import requests

print('\n------------------Get the lyrics to a song---------------------\n')
print('\nHello kind one0! Please do one of the following: \n')
print('\nClick:\n1 to find the lyrics to a song \n0 to exit\n')
while True:
    choice = input('>>')
    if choice =='0':
        break
    if choice == '1':
        name = input('Name of the Artist: ').lower().replace(" ","")
        song = input('Name of the Song: ').lower().replace(" ","").replace("'","")

        url = 'https://www.azlyrics.com/lyrics/' + name + "/" + song + '.html'

    # Beautiful soup webscraper
        try:
            result = requests.get(url)  # always need to do a get request
            content = result.text       # read the content as text
            soup =  BeautifulSoup(content, 'html.parser') # use the html parser
            for lyrics in soup.find_all("div", {"class":None}):
                    print(lyrics.text)
            more = input('Would you like to find another song? (y/n)')
            if more == 'y':
                continue
            break
        except:
            print('Error')
            break
    else:
        print('1 to get lyrics, 0 to exit')
       