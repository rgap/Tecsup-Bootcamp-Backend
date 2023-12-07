

# Model
class Book(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(120))
    author = db.Column(db.String(120))
    description = db.Column(db.String(255))
    summary = db.Column(db.String(255))
    image_url = db.Column(db.String(255))

    def __init__(self, title, author, description, summary, image_url):
        self.title = title
        self.author = author
        self.description = description
        self.summary = summary
        self.image_url = image_url

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "description": self.description,
            "summary": self.summary,
            "image_url": self.image_url,
        }
