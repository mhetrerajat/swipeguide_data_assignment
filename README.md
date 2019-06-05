# SwipeGuide Data Engineering Assignment

Problem Statement -> [Here](sg-data-challenge.md)

![Python](https://img.shields.io/badge/python-3.7-blue.svg)

![Code Coverage](coverage.svg)

### Requirements

- Python 3.7

### Approach

- Clean all columns.
  
  - Remove capitalization, punctuations and slugify `content` column
  
  - Add extra column by converting values of `timestamp` column to datetime

- Get all events with type `pageview` for each user and for each page view consider the time frame between current page view time and last 30 minutes from page view time or last page view by user (whichever is maximum), and calculate all search events during this period.

- Calculate distance between query terms of current search event and previous search event. Here, Levenshtein Distance is being used to calculate distance between two strings. Eliminate all search terms whose distance is less particular threshold, here 0.6. 

- The empty query string is being eliminated before calculating recommended tags for page view url

- Above couple of steps performed repeatedly for each pageview event and userid pair. The processed search events gives tags for page view url.



 NOTE:

- Pipenv is required to run this project. Installation instruction for pipenv can be found [here](https://github.com/pypa/pipenv)
- Otherwise, virtualenv can be used. **requirements.txt** also is given. Installation instruction for virtualenv can be found [here](https://github.com/pypa/virtualenv)

### Get Started

- Initialize environment
  
  ```bash
  cd swipeguide_data_assignment
  pipenv shell
  pipenv install -r requirements.txt
  ```

- Run recommender
  
  ```bash
  python run.py sample_data.json
  ```

### Real World Scenarios

Extension to above problem statement considering the real world scenarios are

- Length of session can be dynamic i.e Instead of considering fixed duration of 30 minutes, session can be calculate based on few conditions - 
  
  - Lot of consecutive search events will be within short time period, because when user want to search for something they will search or type for their query in short period of time without any major time pause until they find out the results they were looking for or give up in frustration. So the time difference between two consecutive queries can be considered to be within certain threshold.
  
  - The user can have multiple information needs within the time threshold, and we cannot identify them as different sessions by time partitioning only. For this case, we can use edit distance similarity consecutive queries to identify different information needs.

- The recommended tags are nothing but the significant queries that affect the user behavior, here user visits (pageview event) the URL. The segregation between the tags and a bunch of keystrokes dependents multiple factors like how user types query. The typing scenarios can be like - 
  
  - Types query incrementally without a reformulation until finding the desired result and do pageview event.
  
  - Types query incrementally and then presses backspace to clear few or all characters. This case could happen when user want to rephrase his/her query
  
  - Copy paste query from somewhere else and then make few changes to it 
  
  - Types query incrementally and then presses backspace to clear few characters and then adding new characters

- The user historical activity can be used to check the trust factor of user inputs. i.e Older the user (more historical activity) higher the weight of tags calculated from his/her query streams. This may help in finding out authenticated and quality tags for the URL. This technique can only be used when a particular URL has a lot of page views and search events across users. 

- If a URL has a lot of tags only from search streams, then the page's content can be used to find out the most relevant words that describe/represent the page content and then take the intersection of these words with search stream only tags to find out the top recommended tags. The relevant words for a page can be calculated with techniques like TF-IDF.

### Test

To run all test cases

```bash
# Current Working Directory -> swipeguide_data_assignment

make test # Runs all test cases
make report # Runs all test cases and generates test coverage report
```

