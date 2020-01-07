# short
**short** is a URL shortener service

## Features
- [x] Basic URL shortener functionality
- [x] Use a database to store the shortened URLs instead of keeping it in memory
    - [ ] Add database error handling
- [ ] Check that the data received is a valid URL
- [ ] Use a random generated ID for the shortened URLs instead of using an incremental number
- [ ] Add a frontend functionality to allow creating the short URLs from the browser itself
- [ ] Custom error webpages
- [ ] Make the app user aware
- [ ] Allow users to create custom named shortened URLs

## How to run
Before running **short** its dependencies have to be met.
### Install dependencies
To install **short**'s dependencies just run the following command:
```bash
pip install -r requirements.txt
```
### Running short
To run **short** run the following command:
```bash
python run.py
```
