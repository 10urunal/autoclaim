import cloudscraper
import time
from bs4 import BeautifulSoup
import threading


class Autoclaim(threading.Thread):
    def __init__(self, site, cookies, token, delay):
        threading.Thread.__init__(self)
        self.site = site
        self.cookies = cookies
        self.delay = delay
        self.token = token

    def run(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        if str(self.site).find("DOGE") > 0:
            cookies = {'DOGEToken': self.token, 'PHPSESSID': self.cookies}
        elif str(self.site).find("STRAT") > 0:
            cookies = {'STRATToken': self.token, 'PHPSESSID': self.cookies}
        elif str(self.site).find("LTC") > 0:
            cookies = {'LTCToken': self.token, 'PHPSESSID': self.cookies}
        elif str(self.site).find("WAVES") > 0:
            cookies = {'WAVESToken': self.token, 'PHPSESSID': self.cookies}
        elif str(self.site).find("ZEC") > 0:
            cookies = {'ZECToken': self.token, 'PHPSESSID': self.cookies}
        elif str(self.site).find("BCN") > 0:
            cookies = {'BCNToken': self.token, 'PHPSESSID': self.cookies}
        elif str(self.site).find("DASH") > 0:
            cookies = {'DASHToken': self.token, 'PHPSESSID': self.cookies}
        elif str(self.site).find("DGB") > 0:
            cookies = {'DGBToken': self.token, 'PHPSESSID': self.cookies}
        elif str(self.site).find("PPC") > 0:
            cookies = {'PPCToken': self.token, 'PHPSESSID': self.cookies}
        elif str(self.site).find("XRP") > 0:
            cookies = {'XRPToken': self.token, 'PHPSESSID': self.cookies}
        elif str(self.site).find("LSK") > 0:
            cookies = {'LSKToken': self.token, 'PHPSESSID': self.cookies}
        elif str(self.site).find("BCH") > 0:
            cookies = {'BCHToken': self.token, 'PHPSESSID': self.cookies}
        elif str(self.site).find("ETH") > 0:
            cookies = {'ETHToken': self.token, 'PHPSESSID': self.cookies}
        elif str(self.site).find("XMR") > 0:
            cookies = {'XMRToken': self.token, 'PHPSESSID': self.cookies}
        elif str(self.site).find("NEO") > 0:
            cookies = {'NEOToken': self.token, 'PHPSESSID': self.cookies}
        while True:
            scraper = cloudscraper.CloudScraper()
            try:
                conn_ = scraper.post(self.site, headers=headers, cookies=cookies)
            except Exception as e:
                print(e)
            soup = BeautifulSoup(conn_.text, "html.parser")
            if conn_.status_code == 200:
                try:
                    name = soup.title
                    print(name.string + "  " + "Success Claim")
                except Exception:
                    print(self.site + "  " + "Success Claim")
            else:
                name = soup.title
                print(name.string + "  " + "Fail Claim")
            time.sleep(self.delay)


f = open('Token.txt', 'r').readlines()
for x in range(len(f)):
    data = f[x].split(",")
    buff = Autoclaim(site=data[0], token=data[1], cookies=data[2], delay=int(data[3]))
    buff.start()
