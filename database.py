# Database
import sqlite3
class Database:
    
    def __init__(self, filename = 'avData.db'):
        self.filename = filename

    def create(self):
        db = sqlite3.connect(self.filename)
        c = db.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS GENRE
         (en TEXT primary key,
          cn TEXT)
        ''')

        c.execute('''CREATE TABLE IF NOT EXISTS AV
         (ID TEXT primary key,
          avcode TEXT UNIQUE,
          date TEXT,
          rate REAL,
          olrate REAL,
          genre TEXT,
          actor TEXT)
        ''')

        db.commit()
        db.close()
    
    def insert(self, avcode, avinfo):
        db = sqlite3.connect(self.filename)
        c = db.cursor()

        c.execute('INSERT OR IGNORE INTO AV(ID, avcode, date, rate, olrate, genre, actor) VALUES (?, ?, ?, ?, ?, ?, ?)', [
            avinfo['识别码'], avcode, avinfo['发行日期'], avinfo['使用者评价'], avinfo['拥看比'], avinfo['类别'], avinfo['演员']
        ])

        db.commit()
        db.close()

    def insertAll(self, avs):
        for key, value in avs.items():
            self.insert(key, value)

    def getAllRank(self, min_rate=0):
        db = sqlite3.connect(self.filename)
        c = db.cursor()
        i = 0
        res = []
        for row in c.execute('SELECT * FROM AV WHERE rate > {} ORDER BY rate DESC, olrate DESC'.format(min_rate)):
            print(row)
            res.append(str(row) + '\n')
            i += 1
        db.close()
        print('Found %d results' % i)
        return res

    def getByGenre(self, genre):
        db = sqlite3.connect(self.filename)
        c = db.cursor()
        i = 0
        for row in c.execute('SELECT * FROM AV WHERE genre LIKE "%{}%" ORDER BY rate DESC, olrate DESC'.format(genre)):
            print(row)
            i += 1
        db.close()
        print('Found %d results' % i)

    def myFavor(self, *para):
        db = sqlite3.connect(self.filename)
        c = db.cursor()
        i = 0
        for row in c.execute('SELECT * FROM AV WHERE {} ORDER BY {}'.format(para[0], para[1])):
            print(row)
            i += 1
        db.close()
        print('Found %d results' % i)