import telegram_send
import urllib.request
import time

URL = 'http://www00.unibg.it/struttura/strutturasm.asp?corso=8458'


def main():
        old_html = None #urllib.request.urlopen(URL).read()

        while True:
                time.sleep(15)
                new_html = urllib.request.urlopen(URL).read()
                if new_html != old_html:
                        telegram_send.send(messages=('Esiti disponibili ' + URL,))
                        old_html = new_html


if __name__ == '__main__':
        main()

