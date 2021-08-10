import requests
import time


def web_scraping():
    response = requests.get(
        'https://proxylist.geonode.com/api/proxy-list?limit=999&page=1&sort_by=lastChecked&sort_type=desc&speed'
        '=fast')
    websites_text = response.content

    def status():
        website_status = response.status_code
        if website_status == 200:
            print('Getting proxies\nPlease wait!')
            time.sleep(2)
            with open('data.txt', 'wb') as data:
                data.write(websites_text)
                data.close()
            print('Done!')
        else:
            print('We are experiencing some sort of problem to get to website.Be sure of:\n'
                  '1.Your internet is on and your internet connections quality is good'
                  '2.Your VPN is off !'
                  '3.restart program'
                  'If problem not solved site is down for maintenance.Be patient.We will come stronger!'
                  'contact us with: example.example@gmail.com')
    status()


if __name__ == '__main__':
    web_scraping()
