from database import cursor,connection


for i in cursor.execute(
    '''
        SELECT author FROM book WHERE author = "Ssali Jonathan"
    
    '''

):
    print(i)