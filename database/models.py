from datetime import datetime
import random
import re
# import bcrypt


class Movie:
	def __init__(self, title, genre, trailer, author='IamJesco'):
		self.id = random.randint(1000000, 10000000)
		self.title = title
		self.slug = re.sub('[ ]', '-', self.title.lower())
		self.genre = genre
		self.trailer = trailer
		self.author = author
		self.published = datetime.utcnow()

	def create_json(self):
		return {
			'id': self.id,
			'title': self.title,
			'slug': self.slug,
			'genre': self.genre,
			'trailer': self.trailer,
			'author': self.author,
			'published': self.published
		}