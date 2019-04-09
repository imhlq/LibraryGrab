# Good Luck

from database import Database

db = Database()
#db.getByGenre('羞耻')
result = db.getAllRank(8.5)   # 8 star 以上
print(result)
with open('result.txt', 'w', encoding='utf8') as fp:
    fp.writelines(result)
