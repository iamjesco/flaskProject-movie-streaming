from pymongo import MongoClient

# from models import Post

client = MongoClient(
	"mongodb+srv://jesco:noksWhSSOjGd88mE@iamjesco.bujsb.mongodb.net/?retryWrites=true&w=majority")
db = client.jescoflix


class Database:

	@staticmethod
	def fetch_all_movies():
		query = db.movies.find({}, {'_id': 0})
		return [movie for movie in query]

	@staticmethod
	def add_movie(movie):
		return db.movies.insert_one(movie)

	@staticmethod
	def fetch_movie(id):
		return db.movies.find_one({'id': id}, {'_id': 0})

	@staticmethod
	def update_post(id, movie):
		return db.movies.update_one({'id': id}, {'$set': movie})

	@staticmethod
	def delete_movie(id):
		return db.movies.delete_one({'id': id})

	@staticmethod
	def fetch_all_users():
		return db.users.find({})

	@staticmethod
	def fetch_user(email):
		return db.users.find_one({'email': email}, {'_id': 0})

	@staticmethod
	def create_user(user):
		return db.users.insert_one(user)

# data = Post('Mi prome poesia', 'Oooga booga mashooga nooga')

# Database.create_post(data.json())

# print(data.json())

# data = Database.fetch_one_post(6311844)
#
# print(data['id'])


# Database.update_post(8241940, 'Willy Wonka', 'mi kas tambe')

# Database.delete_post(8241940)

# print(Database.fetch_all_posts())

# movies = [movie for movie in Database.fetch_all_movies()]
# print(movies)

# print(Database.fetch_user('saegwsg@hotmail.com'))

# email = 'jesco1979@hotmail.com'
#
# user = Database.fetch_user('jesco1979@hotmail.com')
# if email not in user['email']:
# 	print('ooga')













