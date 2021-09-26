from database import cursor,connection


books=[
    {
        "id":1,
        "author":"John The Baptist",
        "title":"Jesus is coming",
        "isbn":"odfjweodjwpojdpqowj"
    },

     {
        "id":2,
        "author":"Moses",
        "title":"Learn Javascript",
        "isbn":"odfjweodjwpojdpqowj"
    },

     {
        "id":1,
        "author":"Maria",
        "title":"Learn SQLite",
        "isbn":"odfjweodjwpojdpqowj"
    },
]


for book in books:


    cursor.execute(
    '''
        INSERT INTO book VALUES (?,?,?,?)
    ''',(book['id'],book['author'],book['title'],book['isbn'])
    )

connection.commit()