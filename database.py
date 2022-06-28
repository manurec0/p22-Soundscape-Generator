import freesound as freesound
import os, sys

FREESOUND_API_KEY = os.getenv('FREESOUND_API_KEY', None)  #Set API key as environment variable in order to be able to look for sounds in freesound.org
if FREESOUND_API_KEY is None:
    print("You need to set your API key as an evironment variable",)
    print("named FREESOUND_API_KEY")
    sys.exit(-1)

"""""
Find the API documentation at http://www.freesound.org/docs/api/.

Apply for an API key at http://www.freesound.org/api/apply/.
"""

FILES_DIR = 'files database'  # Place where to store the downloaded files. Will be relative to the current folder.
DATAFRAME_FILENAME = 'dataframe.csv'  # File where we'll store the metadata of our sounds collection
FREESOUND_STORE_METADATA_FIELDS = ['id', 'name', 'username', 'previews', 'license',
                                   'tags']  # Freesound metadata properties to store

freesound_client = freesound.FreesoundClient()
freesound_client.set_token(FREESOUND_API_KEY)
if not os.path.exists(FILES_DIR): os.mkdir(FILES_DIR)

"""
This file contains some basic functions in order to search sounds in freesound.org and create the previews.
All files will be stored in the directory FILES_DIR which is set by default to .../files database.
"""


def query_freesound(query, filter, num_results):
    """Queries freesound with the given query and filter values.
    """

    pager = freesound_client.text_search(
        query=query,
        filter=filter,
        fields=','.join(FREESOUND_STORE_METADATA_FIELDS),
        group_by_pack=1,
        page_size=num_results
    )
    return [sound for sound in pager]


def generate_queries(sounds, filter, num_results):
    """Generate an array of the sound instances for any given array of strings.
    """
    freesound_queries = []
    for i in sounds:
        query = i
        freesound_queries.append(
            {
                'query': query,
                'filter': filter,
                'num_results': num_results,
            }
        )
    sounds = sum(
        [query_freesound(query['query'], query['filter'], query['num_results']) for query in freesound_queries],
        [])
    return sounds


def retrieve_sound_preview(sound, directory):
    """Download the high-quality OGG sound preview of a given Freesound sound object to the given directory.
    """
    return freesound.FSRequest.retrieve(
        sound.previews.preview_hq_ogg,
        freesound_client,
        os.path.join(directory, sound.previews.preview_hq_ogg.split('/')[-1])
    )


def generate_previews(sounds, filter, num_results, directory):
    """Save previews in the given directory.
    """
    sounds = generate_queries(sounds, filter, num_results)
    for count, sound in enumerate(sounds):
        retrieve_sound_preview(sound, directory + '/')


def sounds_not_database(sound, path):
    filter = 'channels:2'
    num_results = 10
    query = sound
    freesound_query =  {
            'query': query,
            'filter': filter,
            'num_results': num_results,
        }
    if filter is None:
        filter = 'duration:[0 TO 30]'  # Set default filter
    pager = freesound_client.text_search(
        query=query,
        filter=filter,
        fields=','.join(FREESOUND_STORE_METADATA_FIELDS),
        group_by_pack=1,
        page_size=num_results
    )
    sounds = [sound for sound in pager]
    generate_previews(sounds, filter, 1, path + '/' + 'nonDBsounds')