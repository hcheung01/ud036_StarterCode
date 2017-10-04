import webbrowser


# Class
class Movie():
    # Constructor
    def __init__(self, title, storyline, poster_image, trailer):
        # Instance Variables
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer

    # Instance Method
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
