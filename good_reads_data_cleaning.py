import pandas as pd

books = pd.read_csv('good_reads.csv', index_col=0)

books['series'] = books['series'].str.rstrip(')')

books[['avg_rating','no_of_ratings']] = books['avg_rating'].str.split('—', expand=True)

books['avg_rating'] = books['avg_rating'].apply(lambda x : x.rstrip(' avg rating').lstrip('really liked it ').lstrip('was amazing '))

books['avg_rating'] = books['avg_rating'].astype(float)

books['no_of_ratings'] = books['no_of_ratings'].apply(lambda x : x.rstrip(' ratings').replace(',',''))

books['no_of_ratings'] = books['no_of_ratings'].astype(int)

books['score'] = books['score'].apply(lambda x : x.lstrip('score: ').replace(',',''))

books['score'] = books['score'].astype(int)

books[['temp','no_of_votes']] = books['no_of_votes'].str.split('and', expand=True)

books['no_of_votes'] = books['no_of_votes'].apply(lambda x : x.rstrip(' people voted').replace(',',''))

books['no_of_votes'] = books['no_of_votes'].astype(int)

books.drop('temp',axis = 1, inplace=True)

books = books[['titles',
                'series',
                'author',
                'avg_rating',
                'no_of_ratings',
                'no_of_reviews',
                'score',
                'no_of_votes',
                'no_of_awards',
                'pages',
                'genre',
                'language',
                'description',
                'urls']]

books.to_csv('good_reads_cleaned.csv')