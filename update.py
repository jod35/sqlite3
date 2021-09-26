from database import cursor,connection

cursor.execute(
    '''
        UPDATE book SET author = "Sssali Jonathan" WHERE author = "Ssali Jonathan"
    
    '''
)

connection.commit()