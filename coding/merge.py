import csv

scrape = {}
with open("scrape.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        scrape[row["isbn_13"]] = row


with open("merged_vegan_books_scrape.csv", "w") as fw:
    writer = csv.writer(
        fw,
        quoting=csv.QUOTE_ALL
    )
    writer.writerow([
            "title",
            "author",
            "isbn_13",
            "book_url",
            "image_url",
            "ISBN-10",
            "Series",
            "Publication Date",
            "ISBN",
            "Large Print",
            "Publisher",
            "Pages",
            "Language",
        ],)
    with open("vegan_books.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            isbn = row[3]
            out_row = list( scrape[isbn].values())
            
            out_row.append(
                f"https://www.greenlightbookstore.com/book/{isbn}"
            )
            out_row.extend(row)
            writer.writerow(out_row)
