class Song:
    count=0
    genres=[]
    artists=[]
    genre_count={}
    artists_count={}
    def __init__(self,name,artist,genre):
        self.name=name
        self.artist=artist
        self.genre=genre

        Song.add_songs_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artist_count(self.artist)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if not value or not value.strip():
            raise ValueError("Song name is required")
        self._name=value.strip()

    @property
    def artist(self):
        return self._artist

    @artist.setter
    def artist(self,value):
        if not value or not value.strip():
            raise ValueError("Artist name is required")
        self._artist=value.strip()

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self,value):
        if not value or not value.strip():
            raise ValueError("Genre of the song must be provided")
        self._genre=value.strip()


    @classmethod
    def add_songs_to_count(cls):
        cls.count +=1

    @classmethod
    def add_to_genres(cls,genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls,artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls,genre):
        cls.genre_count[genre]=cls.genre_count.get(genre,0)+1

    @classmethod
    def add_to_artist_count(cls,artist):
        cls.artists_count[artist]=cls.artists_count.get(artist,0)+1


