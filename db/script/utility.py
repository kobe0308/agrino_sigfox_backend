import sqlite3

conn = sqlite3.connect('../sensorData.db')
c = conn.cursor()


def main():
    dbPath = '../sensorData.db'

    sql_create_sigfox_info_table = """ CREATE TABLE IF NOT EXISTS sigfoxInfo(
    
    
                                        ) 
    
    
                                    """





if __name__ == '__main__':
    main()
