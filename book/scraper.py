from .reques_manager import Request
from bs4 import BeautifulSoup
from .models import Book


# Scraping first five pages
for page in range(5):
    url = f'https://www.goodreads.com/search?page={page+1}&q=book&qid=tNFlYDVEba&tab=books'
    
    request = Request(url=url)

    # Get all titles
    titles = list()

    title_boxes = request.get_all(
        html_tag='a',
        tag_id_by='class',
        tag_id='bookTitle'
    )

    for title in title_boxes:
        titles.append(title.find('span').text)

    # Get all writers
    writers = list()

    writer_boxes = request.get_all(
        html_tag='a',
        tag_id_by='class',
        tag_id='authorName'
    )

    for writer in writer_boxes:
        writers.append(writer.find('span').text)

    # Get all ratings
    ratings = list()

    rating_boxes = request.get_all(
        html_tag='span',
        tag_id_by='class',
        tag_id='minirating'
    )

    for rating in rating_boxes:
        ratings.append(rating.text)

    # Get all number of editions
    editions = list()

    edition_boxes = request.get_all(
        html_tag='a',
        tag_id_by='class',
        tag_id='greyText'
    )

    for edition in edition_boxes:
        # Extract number from text and cast to int
        temp = edition.text
        index = temp.find(' ')
        temp = temp[:index]
        editions.append(int(temp))

# Add scraped data to database
for i in len(titles):
    Book.objects.create(
        title=titles[i],
        writer=writers[i],
        rating=ratings[i],
        number_of_editions=editions[i],
    )

