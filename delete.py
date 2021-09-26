from database import cursor , connection

cursor.execute(
    '''
     DELETE FROM book WHERE id = 1
    '''
)

connection.commit()