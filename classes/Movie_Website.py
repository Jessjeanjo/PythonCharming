#!/usr/local/bin/python


from __future__ import print_function
from fresh_tomatoes import open_movies_page

class Movie(object):
    '''

    '''
    def __init__(self,movie_name, movie_storyline, movie_photo, movie_trailer):
        self.__movieTitle = movie_name
        self.__movieStoryLine = movie_storyline
        self.__moviePhoto = movie_photo
        self.__movieTrailer = movie_trailer

    def get_movie_title(self):
        return self.__movieTitle

    def get_storyline(self):
        return self.__movieStoryLine

    def get_movie_photo(self):
        return self.__moviePhoto

    def get_trailer_url(self):
        return self.__movieTrailer


def create_movie_object(movie_name, movie_storyline, movie_photo, movie_trailer):
    return Movie(movie_name, movie_storyline, movie_photo, movie_trailer)

def add_movie_list(movie_lissy, movie_object):
    movie_lissy.append(movie_object)

def get_movie_info():
    movie_name = raw_input("\nName of your movie: ")
    movie_storyline = raw_input("Movie storyline: ")
    movie_photo = raw_input("URL link of the movie's photo: ")
    movie_trailer = raw_input("URL link of the movie's trailer: ")

    return movie_name, movie_storyline, movie_photo, movie_trailer

def main():

    movie_lissy = []
    counter = int(raw_input("How many movies are adding?"))
    for i in range(counter):
        movie_n, movie_s, movie_p, movie_t = get_movie_info()
        movie_object = create_movie_object(movie_n, movie_s, movie_p, movie_t)
        add_movie_list(movie_lissy, movie_object)

    open_movies_page(movie_lissy)


if __name__ == '__main__':
    main()
