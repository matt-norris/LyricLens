import lyricsgenius
import pandas as pd

genius = lyricsgenius.Genius("q9WFPfJovwifqrnkrxvkv2GH5EuP4kLrZ7ll31H57tHSzaIESIkbMDVVTKSKTglv")
genius.remove_section_headers = True  # Remove section headers (e.g. [Chorus]) from lyrics when searching
genius.skip_non_songs = False  # Include hits thought to be non-songs (e.g. track lists)
genius.excluded_terms = ["(Remix)", "(Live)"]  # Exclude songs with these words in their title


def get_top_songs_of_artist(artist_name, limit=3):
    """
    This function gets the top songs of a specified artist.

    Parameters:
        artist_name (str): The name of the artist.
        limit (int, optional): The maximum number of top songs to return. Defaults to 10.

    Returns:
        song_data_list (list): A list of dictionaries, where each dictionary contains details of a song.
    """

    # Using the Genius object, search for the artist by name.
    # The 'max_songs' parameter limits the number of songs to get for the artist,
    # and the 'sort' parameter sorts the songs by popularity.
    artist = genius.search_artist(artist_name, max_songs=limit, sort='popularity')

    # Get the list of Song objects for this artist.
    top_songs = artist.songs

    # Initialize an empty list to store the song data.
    song_data_list = []

    # Loop over each song in the list of top songs.
    for song in top_songs:
        # For each song, create a dictionary containing the artist name, song title, and song lyrics.
        # Append this dictionary to the list of song data.
        song_data_list.append({
            'artist': artist_name,
            'song': song.title,
            'lyrics': song.lyrics
        })

    # Return the list of song data.
    return song_data_list


# Specify the artist name for which you want to get the top songs.
# In this case, the artist is Kanye West, but you can replace this with the name of any artist.
artist_name = 'Kanye West'

# Call the 'get_top_songs_of_artist' function, passing in the artist name.
# This function returns a list of dictionaries, where each dictionary contains details of a song.
# The result is stored in the 'song_data_list' variable.
song_data_list = get_top_songs_of_artist(artist_name)

# Convert the list of song data into a pandas DataFrame.
# Each row of the DataFrame corresponds to a song, and the columns are 'artist', 'song', and 'lyrics'.
df = pd.DataFrame(song_data_list)

# Write the DataFrame to a CSV file named 'top_artist_songs.csv'.
# The 'index=False' argument prevents pandas from writing row indices into the CSV file.
df.to_csv('top_artist_songs.csv', index=False)

# Initialize an empty dictionary to store the word count.
word_count = {}
stop_words = ([u'your', u'yours', u'yourself', u'yourselves', u'he', u'him', u'his', u'himself', u'she',
u"she's", u'her', u'hers', u'herself', u'it', u"it's", u'its', u'itself', u'they', u'them',
u'their', u'theirs', u'themselves', u'what', u'which', u'who', u'whom', u'this',
u'that', u"that'll", u'these', u'those', u'am', u'is', u'are', u'was', u'were', u'be',
u'been', u'being', u'have', u'has', u'had', u'having', u'do', u'does', u'did', u'doing',
u'a', u'an', u'the', u'and', u'but', u'if', u'or', u'because', u'as', u'until',
u'while', u'of', u'at', u'i', u'in', u'my'])
# Loop over each song's lyrics in the DataFrame.
for lyrics in df['lyrics']:
    # Convert the lyrics to lower case and split them into words.
    # The 'split' function splits a string into a list of words based on whitespace.
    words = lyrics.lower().split()

    # Loop over each word in the list of words
    for word in words:
        # Only count the word if it is not a stop word
        if word not in stop_words:
            # If the word is already in the dictionary, increment its count
            if word in word_count:
                word_count[word] += 1
            # If the word is not in the dictionary, add it to the dictionary with a count of 1
            else:
                word_count[word] = 1

# Sort the word count dictionary by count in descending order.
# The 'items' function returns a list of tuples, where each tuple is a (word, count) pair.
# The 'sorted' function sorts this list of tuples based on the count (i.e., the second element of each tuple).
# The 'reverse=True' argument makes the sort order descending.
sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# Print the 10 most popular words in the top songs of the artist.
print("Most popular words in the top songs of the artist:")
for word, count in sorted_word_count[:10]:
    print(f"{word}: {count}")
