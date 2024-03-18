
# Book Scraper With Django

This project helps to manage easer and better scraped data from a specific website. You can store scraped information in a database and also if you want you can select as much as datas to download them in a csv file.


## Acknowledgements

 - [w3schools website](https://www.w3schools.com/)
 - [Django Documentation](https://docs.djangoproject.com/en/5.0/topics/db/queries/)



## Authors

- [Macan Mehri](https://github.com/macanMehri)


## Deployment

To deploy this project run

```bash
  pip install -r requirements.txt
```
Rename sample_settings.py file to local_settings.py.
Put you secret key here
```bash
  SECRET_KEY = 'your secret key'
```
Add a custom admin path here
```bash
  ADMIN_PATH = 'custom admin path/'
```
Rename sample_headers.py to local_headers.py and add your user Agent here
```bash
  HEADERS = {
    'USER_AGENT': 'your user agent'
}
```


## Run Locally

Clone the project

```bash
  git clone https://github.com/macanMehri/BookScraper.git
```

Go to the project directory

```bash
  cd book_scraper
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python manage.py runserver
```


## Features

- Ease of use
- User friendly
- Cross platform
- Warm environment
- Scrape very fast
