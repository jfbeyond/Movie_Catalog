# Favorite Movies Catalog

Movie website with links to my favorite movies. This project utilizes live requests to the TMDB movie database through its API.
The website functionality can be applied to any desired movie as a new API request is executed everytime the website is launched.

## Getting Started

Clone or download this project (folder: Movie_catalog) in your local machine to be able to run the website.

### Need to have/install Python 2.7.

Follow [these](https://datascience.com.co/how-to-install-python-2-7-and-3-6-in-windows-10-add-python-path-281e7eae62a) instructions for step-by-step python installation.

### Need to install TMDB API Python wrapper "tmdbsimple" by [celiao](https://github.com/celiao).

This python wrapper has defined methods for different requests to the TMDB API and takes care of the authentication through OAuth 2.0. You can install tmdbsimple by running the following command in your command line:

```
Use pip: pip install tmdbsimple 
```
Although only two methods from this TMDB API wrapper will be utilized in this project (Search() and Movies()), it is recommended to visit
the [tmdbsimple](https://github.com/celiao/tmdbsimple) repository to get a full grasp of all the methods and tools.

###  API Key

An API Key to the Movie Database will be needed to access the API. Follow these steps to obtain one:

1. Register and verify your [account](https://www.themoviedb.org/account/signup).
2. [Log into](https://www.themoviedb.org/login) your account.
3. Select the API section on the lef side of your account page.
4. Click on the link to generate a new API key and follow the instructions.

This obtained key must be placed in one of the project files as indicated next.


## Running the Movie Website

Go to the directory where the project files were downloaded. You should have:

1. media.py: This is the file that makes the calls to the Movie Database API. You must replace the API Key
you obtained previously in the second line of this file in order to enable the requests.

2. entertainment_media.py: This file will run this application by opening the movie catalog in the browser.
It contains an array with the names of my favorite movies, which can be modified to contain any movie name.

3. fresh_tomatoes.py: This is the template offered by udacity with the styles and html set up for the website.
It uses the movie array defined in entertainment_media.py. It was slightly modified to read the movie array and 
to display different background colors.

To run the application, please open entertainment_media.py in your python GUI (IDLE might be) and run the code.
A website should open in your browser with my favorites movies displaying their titles, poster pictures and the
capability of playing a trailer. Again, if you wish to see the advantage of using an API, just add or remove movie
names in the 'my_favorite' array and re-run the application.

Just give it a try!

## Authors

* **Jhon Diaz** - [jfbeyond](https://github.com/jfbeyond)

## Acknowledgments

* Udacity
* Celiao
* Inspiration

