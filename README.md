# p22-Soundscape-Generator

## About The Project

The soundscape generator is an application that aims to recreate a soundscape given a text sentence provided by the user. 
It uses Natural Language Processing libraries in order to extract the keywords from the text and uses them to search for sounds available in [Freesound](https://freesound.org/). 
The aim is to recreate real ambient sound, so it will only use sounds recorded on the field and will try to recreate a real environment by using stereo and mono tracks to make the user feel like they are surrounded by sound. 

### Built With
* [NLTK](https://www.nltk.org/)
* [Rake](https://pypi.org/project/rake-nltk/)
* [Pydub](https://github.com/jiaaro/pydub)
* [Freesound API](https://freesound.org/docs/api/)
* [Django](https://www.djangoproject.com/)
* [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/)

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

You will need ffmpeg in order to manipulate certain audio file formats. If you don't already have ffmpeg installed you can follow these steps:
* First you will need to [download](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z) this zip.
* Then you can extract it to your root hard drive (usually C:) and name the folder **ffmpeg**.
* Run the following command in your terminal executed as administrator:
    ```sh
    setx /m PATH "C:\ffmpeg\bin;%PATH%"
    ```
* For more information you can follow [this link](https://www.google.com/amp/s/www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/amp/).

## Installation

You can install the requirements using the text file 'requirements.txt' and using the following command in the console:
```
python requirements.txt install
```

Alternatively, you can use pip for each library:
```
pip install nltk
```
```
pip install rake-nltk
```
```
pip install pydub
```
```
pip install django
```

You will also need to download the freesound API. You can read about the API's documentation [here](https://freesound.org/docs/api/).
For that you will need to apply for an API key [here](https://www.freesound.org/apiv2/apply/).
To install the Freesound API you can clone the repo or download the zip [here](https://github.com/MTG/freesound-python.git) and run the following command:
````
python setup.py install
````
You will need to set your API key as an environment variable in order for the application to work correctly.


## Usage

For this branch you will also need to set up a virtual environment for the Django web interface to function properly.
Go to the terminal in the directory of your project and type:
```
myenv\Scripts\activate
```
Then start up the interface:
````commandline
python manage.py runserver
````
Then you will be able to see the interface in your browser in ``http://127.0.0.1:8000/``.
 There you can write a sentence describing the soundscape you want to recreate.
We recommend typing real spaces such as biomes, ecosystems and real places such as "a forest" or "night in the woods with a campfire".
Once it is done, a file will be created in the directory of the environment in the directory `.../files database` called *'mixed.wav'*. You can listen to it and save it as you like, but be sure to check out the license type the sounds used. All the information about the sounds used will be displayed in the terminal after the executtion.

## Acknowledgements

* [Freesound.org](https://freesound.org/)
* The [UPF Music Technology Group](https://www.upf.edu/web/mtg)
* [Ángel Faraldo](https://www.angelfaraldo.info/)

