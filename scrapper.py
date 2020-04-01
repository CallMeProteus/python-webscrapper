
import os
import requests
from bs4 import BeautifulSoup


def main():
    while True:
        
        try:
            
            url = input('paste target url')
            if 'http://' not in url:
                url = "https://www."+ url
            try:
                data = requests.get(url)
                soup = BeautifulSoup(data.text, 'html.parser')# or html5parser, this is inbuilt
                values = [p.text for p in soup.find_all('p')]
            except:
                print('Invalid url, please check url')
                break
            
        
            try:
                filename = input('name of file')
                with open('C:\\Users\\jafet\\OneDrive\\Desktop\\County data\\'+ filename +'.txt', 'a') as f:
                    line = 0
                    for string in values:
                        print(string, file=f)
                        ##f.write(string)
                        print('Lines printed:'+ line)
                        line += 1
            except:
                print("write to file unsuccesful")
            
                
        except:
            pass
          
    

##newvar = valu[0].split()





if __name__ == "__main__":
    main()
