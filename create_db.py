from database import cursor,connection


cursor.execute(
    '''
        CREATE TABLE book (
            id real integer,
            author text,
            title text,
            isbn text
        )
    '''
)


connection.commit()