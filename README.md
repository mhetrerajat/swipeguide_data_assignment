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

### Test

To run all test cases

```bash
# Current Working Directory -> swipeguide_data_assignment

make test # Runs all test cases
make report # Runs all test cases and generates test coverage report
```

### Documentation

To generate documentation for Code base:

```bash
# Current Working Directory -> swipeguide_data_assignment

cd docs
make docs # Generates documentation
make view # Opens in browser
```
