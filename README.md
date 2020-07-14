# Web Scraping, Data Wrangling and Analysis on Goodreads List

### Goodreads is a website where readers can rate and review the books they read. My interest in reading is what motivated me to scrape Goodreads. The aim of this project was to scrape, clean and analyse data from the Top 1000 books of the Decade: 2010's. Data has been scraped from the [‘Best Books of the Decade: 2010's’](https://www.goodreads.com/list/show/4093.Best_Books_of_the_Decade_2010_s?page=1) list using the python library BeautifulSoup.

### This project will be a multi-parter :
* Data Collection : Building a scraper to collect and organize data from Reading Lists on Goodreads.
* Data Cleaning : Cleaning and organising the scraped data.
* Visualization and Analysis: Detailed visualization and analysis of the cleaned books data.

___

### Code and Resources Used

#### Python Version : 3.8.2
#### Libraries Used : pandas, numpy, matplotlib, seaborn, plotly, cufflinks, chart_studio, bs4, random, time
#### Data : [Best Books of the Decade: 2010's](https://www.goodreads.com/list/show/4093.Best_Books_of_the_Decade_2010_s?page=1)

### P.S - To access the interactive version of the plots, please checkout the link mentioned at the bottom of this page.
___
## Data Collection :
### Data has been collected from the [‘Best Books of the Decade: 2010's’](https://www.goodreads.com/list/show/4093.Best_Books_of_the_Decade_2010_s?page=1) list.
#### Below is an example of the list page.

![List Image]()

#### Here we can see few of the elements that we collect for analysis such as :
* Book Title
* Series Name
* Author Name
* Average Rating
##### among others.
#### In order to collect more detailed information about each book we access each individual book's url :

![Book Image]()

#### Here we can see few of the elements that we collect for analysis such as :
* Book Description
* Awards
* Genres
##### among others.

#### Total 1000 books have been scraped from 10 pages of the list.

___

## Data Cleaning :
### The collected data consisted of missing values and unclean data. Various cleaning operations were performed using pandas library such as :
* Average Ratings, Number of ratings, etc columns which were in string format were converted to int and float.
* Columns containing unwanted characters such as 'avg rating', 'really liked it', 'score: ' were removed.
* Titles column was separated into 'Book Title' and 'Series Title' columns.
* Awards column was converted to Number of Awards.

___

## Data Analysis :

* [Distribution of Average Rating]()
* [Distribution of Genre]()
* [Wordclouds for Book Titles, Author names and Description]()
* Distribution of Number of Pages and further analysis can be found in the jupyter notebook.
### Average Rating :
![Average Rating Histogram](https://raw.githubusercontent.com/ritik-k/good_reads/master/gifs/avg_r.gif)

[Static Image](https://github.com/ritik-k/good_reads/blob/master/images/avg_r.png)
#### We can see that the majority of the books have received a rating between 4.03 and 4.07. We can also see that the average ratings follow a normal distribution.
#### Above histogram give us a good indication of the distribution of the data but it don't give us much information about the outliers. We can use Boxplot to examine the outliers.
![Rating boxplot](https://raw.githubusercontent.com/ritik-k/good_reads/master/gifs/avg_r_b.gif)

[Static Image](https://raw.githubusercontent.com/ritik-k/good_reads/master/images/avg_r_b.png)

#### From the above boxplot we can infer that :
* Median Average Rating = 4.05
* IQR (Middle 50 percent) = 0.38

#### Two highest rated books:
* White boy in Watts - 5.0
* Shadow Team GB - 4.85

#### Two lowest rated books:
* The Finkler Question - 2.79
* The Secret Lives of People - 3.08

### Genre :
![Genre](https://raw.githubusercontent.com/ritik-k/good_reads/master/gifs/genre.gif)

[Static Image](https://raw.githubusercontent.com/ritik-k/good_reads/master/images/genre.png)
#### From the above histogram we can infer that the most popular genres are :
* Fantasy - 23.5% 
* Fiction - 22.1%
* Young Adult - 13.8%

#### These 3 Genres account for nearly 60% of total books.

### Wordcloud :
#### Book Title :
![titles]()
#### We set min_word_length = 4 to discard words such as 'the, is, it, an, etc'

#### Author :
![author]()
#### The abover wordcloud contains names of some legendary authors such as : Stephen King and Rick Riordan and certain generic names such as John, David, Robert and James.


#### Description:
![Description]()

___
### Usage and Interactive plots:
#### This project is best viewed in a notebook viewer, which can be accessed [here](https://nbviewer.jupyter.org/github/ritik-k/good_reads/blob/master/good_reads_analysis.ipynb). In this notebook, you will find a walk through of the work done, interactive plots and the respective code.