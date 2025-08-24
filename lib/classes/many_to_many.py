class Article:
    all = []
    def __init__(self, author, magazine, title):
        if not isinstance (author, Author):
            raise TypeError("author must be an instance Author")
        if not isinstance (magazine, Magazine):
            raise TypeError("magazine must be an instance Magazine")
        if not isinstance (title, str) or not (5 <= len(title) <=50):
            raise TypeError("title must be a sring between 5 to 50 characters")
        self.author = author
        self.magazine = magazine
        if not hasattr(self, "_title"):
         self._title = title
         Article.all.append(self)
        author._articles.append(self)
        magazine._articles.append(self)



    @property
    def title(self):
        return self._title


    @property
    def author(self):
        return self._author


    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("author must be an instance Author")
        self._author = value


    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("magazine must be an instance Magazine")
        self._magazine = value


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("name must be a non-empty string")
        self._name = name
        self._articles = []


    @property
    def name(self):
        return self._name
    
    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self._articles:
            return None
        return list({article.magazine.category for article in self._articles})


class Magazine:
    _all_magazines = []
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []
        Magazine._all_magazines.append(self)


    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("name must be a string between 2 and 16 characters")
        self._name = value


    @property
    def category(self):
        return self._category


    @category.setter
    def category(self,value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("category must be a non-empty string")
        self._category = value


    def articles(self):
        return self._articles


    def contributors(self):
        return list({article.author for article in self._articles})


    def article_titles(self):
        if not self._articles:
            return None
        return[article.title for article in self._articles]


    def contributing_authors(self):
        authors_count = {}
        for article in self._articles:
            authors_count[article.author] = authors_count.get(article.author, 0) + 1
        result = [author for author, count in authors_count.items() if count >2]
        return result if result else None


    @classmethod
    def top_publisher(cls):
        if not cls._all_magazines:
            return None
        return max(cls._all_magazines, key=lambda mag: len(mag._articles), default = None)