def write_to_csv():
    with open('douban_books.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(['a', '1', '1', '2', '2'])
        
def write_to_file(file_name,data):
    file_object = codecs.open(file_name, 'w','utf-8')
    file_object.write(data)
    file_object.close( )
    
def add_books():
    bookList = []
    bookList.append(BookInfo(title="滚蛋吧!肿瘤君",rates = "9.3", votes="10879",imgUrl="http://img4.douban.com/lpic/s20742806.jpg",tag=""))
    bookList.append(BookInfo(title="你一生的故事",rates = "9.0", votes="1047",imgUrl="http://img3.douban.com/lpic/s28033064.jpg",tag=""))
    bookList.append(BookInfo(title="百年孤独",rates = "9.2", votes="61296",imgUrl="http://img3.douban.com/lpic/s6384944.jpg",tag=""))
    bookList.append(BookInfo(title="白夜行",rates = "9.1", votes="137860",imgUrl="http://img3.douban.com/lpic/s4610502.jpg",tag=""))
    bookList.append(BookInfo(title="小王子",rates = "9.0", votes="185703",imgUrl="http://img4.douban.com/lpic/s1237549.jpg",tag=""))
    BookInfo.objects.bulk_create(bookList)