# Appstore_rating_collection
Collect appstore ratings from url

# Usage
* Please update your chrome webdriver with your chrome version: https://chromedriver.chromium.org/downloads
* Suggest using pipenv or conda virtual environment
* Default is set as 100 secondsYou can change the duration of data collection as you want


```
>>cd "route directory"
>>pipenv --three
>>pipenv shell
>>pip install -r requirements.txt
```

* in 'links.txt', please put list of urls (app rating page. See example txt file), e.g:https://apps.apple.com/us/app/apple-store/id375380948#see-all/reviews 

```
>>python collect.py
```
or you can also use ipynb
