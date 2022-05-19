import freesound as freesound
import os

FREESOUND_API_KEY = 'xTdc6oqv5FLJQCmdcD8kRKnzuYnScA6vrkXBs36v'
FILES_DIR = 'files database'  # Place where to store the downloaded files. Will be relative to the current folder.
DATAFRAME_FILENAME = 'dataframe.csv'  # File where we'll store the metadata of our sounds collection
FREESOUND_STORE_METADATA_FIELDS = ['id', 'name', 'username', 'previews', 'license', 'tags']  # Freesound metadata properties to store

freesound_client = freesound.FreesoundClient()
freesound_client.set_token(FREESOUND_API_KEY)
if not os.path.exists(FILES_DIR): os.mkdir(FILES_DIR)

sound_tags = ["birds"]

def query_freesound(query, filter, num_results=10):
    """Queries freesound with the given query and filter values.
    If no filter is given, a default filter is added to only get sounds shorter than 30 seconds.
    """

    pager = freesound_client.text_search(
        query=query,
        filter=filter,
        fields=','.join(FREESOUND_STORE_METADATA_FIELDS),
        group_by_pack=1,
        page_size=num_results
    )
    return [sound for sound in pager]


def generate_queries(sounds):
    freesound_queries = []
    filter = 'channels:1 type:wav tag:field-recording'
    for i in sounds:
        query = i
        freesound_queries.append(
            {
                'query': query,
                'filter': filter,
                'num_results': 5,
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



sounds = generate_queries(sound_tags)
for count, sound in enumerate(sounds):
    print('Downloading sound with id {0} [{1}/{2}]'.format(sound.id, count + 1, len(sounds)))
    retrieve_sound_preview(sound, 'files database'+'/')

