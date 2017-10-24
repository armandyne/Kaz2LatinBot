import sqlite3

class SQLiteHelper:
    def __init__(self, dbName):
        self.connection = sqlite3.connect(dbName)        
        self.cursor = self.connection.cursor()
    
    def close(self):
        self.connection.close()
    
    def save_request(self, message, message_id, first_name, username, date, text):                    
        self.cursor.execute('''INSERT INTO requests(json,
                                                    message_id,  
                                                    from_user_first_name,                                                  
                                                    from_user_username,
                                                    date,
                                                    text)
                                VALUES(?,?,?,?,?,?) ''', 
                                (message,
                                 message_id,
                                 first_name,
                                 username,
                                 date,
                                 text
                                 ))
        self.connection.commit()
            