# Appstore_rating_collection
Collect appstore ratings from url

# Usage
* Please update your chrome webdriver with your chrome version: https://chromedriver.chromium.org/downloads
* Suggest using pipenv or conda virtual environment
* You can change the duration of data collection as you want


```
pipenv --three
pip install -r requrements.txt
```

* in 'links.txt', please put list of urls (app rating page. See example txt file), e.g:https://apps.apple.com/us/app/apple-store/id375380948#see-all/reviews 

```
python collect.py
```
or you can also use ipynb
