# LyricLens

LyricLens is a Python-based application that uses Genius API and web scraping techniques to analyze the lyrics of popular songs from a specific artist. It retrieves data about the most popular songs from an artist, compiles a CSV file with the artist name, song name, and song lyrics, and then analyzes the lyrics to identify the most frequently used words.

## Features

- Retrieves song data from Genius API.
- Scrapes lyrics from Genius website.
- Creates a CSV file with song data and lyrics.
- Analyzes lyrics to identify the most frequently used words.
- Filters out common English "stop words" during analysis.

## Installation and Setup

1. Clone the repository.

```
git clone https://github.com/your_username/LyricLens.git
```

2. Install required Python packages.

```
pip install -r requirements.txt
```

3. Obtain an API access token from Genius and replace `API_ACCESS_TOKEN` in the `lyriclens.py` file with your token.

4. Run the script and provide the artist's name as an argument.

```
python lyriclens.py 'Kanye West'
```

## Usage

After running the script with an artist's name as an argument, the script will:

- Retrieve data for the most popular songs of that artist from the Genius API.
- Scrape the lyrics for each song from the Genius website.
- Create a CSV file named `top_artist_songs.csv` in the current directory with columns for the artist's name, song name, and song lyrics.
- Analyze the lyrics to identify the most frequently used words (excluding common English "stop words").
- Print the ten most frequently used words in the artist's songs and their count.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

Please note that this project is released with a Contributor Code of Conduct. By participating in this project you agree to abide by its terms.
