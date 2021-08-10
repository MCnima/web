import manage
import organize
import web


def main():
    web.web_scraping()
    manage.condition()
    manage.split()
    manage.lister()
    organize.organize()


if __name__ == '__main__':
    main()
