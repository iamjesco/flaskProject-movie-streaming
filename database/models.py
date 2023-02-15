from datetime import datetime
import random
import re
# import bcrypt


class Movie:
	def __init__(self, title, genre, starring, released, trailer, thumbnail, filename, author='IamJesco'):
		self.id = random.randint(1000000, 10000000)
		self.title = title
		self.slug = re.sub('[ ]', '-', self.title.lower())
		self.genre = genre
		self.starring = starring
		self.released = released
		self.trailer = trailer
		self.thumbnail = thumbnail
		self.filename = filename
		self.author = author
		self.published = datetime.utcnow()

	def create_json(self):
		return {
			'id': self.id,
			'title': self.title,
			'slug': self.slug,
			'genre': self.genre,
			'starring': self.starring,
			'released': self.released,
			'trailer': self.trailer,
			'thumbnail': self.thumbnail,
			'filename': self.filename,
			'author': self.author,
			'published': self.published
		}