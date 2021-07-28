# Appstore rating / review collection
Collect appstore ratings from url

**Important: you must use the URL of each rating page, not the main page of the app :e.g:https://apps.apple.com/us/app/apple-store/id375380948#see-all/reviews**

**Also, recommend not utilizing the data other than academic or personal research purpose, which can possibly infringe any rights of other service provider**

# Usage
* Please update your chrome webdriver with your chrome version: https://chromedriver.chromium.org/downloads
* Suggest using pipenv or conda virtual environment
* Default duration for scrolling (to load more reviews) is set as 100 seconds. You can change the duration of data collection as you want


```
>>cd "route directory"
>>pip install -r requirements.txt
```

* in 'links.txt', please put list of urls (app rating page. See example txt file), e.g:https://apps.apple.com/us/app/apple-store/id375380948#see-all/reviews 

```
>>python collect.py
```
or you can also use ipynb
