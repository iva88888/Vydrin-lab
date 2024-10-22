# TODO Найдите количество книг, которое можно разместить на дискете
volume_disk = 1.44
pages_book = 100
lines_page = 50
symbols_line = 25
bytes_symbols = 4

volume_disk_bytes = volume_disk * 1024 * 1024
total_of_symbols = symbols_line * lines_page * pages_book
volume_book_bytes = total_of_symbols * bytes_symbols

number_of_books = int (volume_disk_bytes // volume_book_bytes)

print("Количество книг, помещающихся на дискету:", number_of_books)