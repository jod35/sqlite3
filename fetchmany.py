from database import connection,cursor

for i in cursor.execute(
    '''
        SELECT author FROM book WHERE author = "Ssali Jonathan"
    
    '''

).fetchmany():
    print(i)