
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Things you need to install the software and how to install them

```
pip install selenium
pip install pandas
```
You will also need your own version of your browser's driver (Some links provided below):
 ```
 https://chromedriver.storage.googleapis.com/index.html?path=79.0.3945.36/
 https://github.com/SeleniumHQ/selenium/wiki/FirefoxDriver
 https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari
 ```
 After installing replace $PATH on line 17 and 59 with the driver's path (Google Driver is standard):
 ```
     browser = webdriver.Chrome('$PATH', chrome_options=option)
 ```

## Running the tests

Simply run program...

```
python3 Billboard_Player.py
```

### Testing

Sample Output

```
% python3 Billboard_Player.py
Billboard_Player.py:59: DeprecationWarning: use options instead of chrome_options
  browser = webdriver.Chrome('/Users/Downloads/chromedriver', chrome_options=options)
Select a year from 1958 - 2018 : 2016
1. Rock
2. Pop
3. Holiday
4. Overall Popularity
5. Country
6. R&B/Hip-Hop
7. Other Genres
8. International
9. Christian
10. Dance/Electronic
11. Album Sales
12. Gospel
13. Hot 100 Breakouts
14. Latin
15. Social
What genre would you like to view: 5
1. Bluegrass Albums
2. Country Digital Song Sales
3. Top Country Albums
4. Country Airplay
5. Hot Country Songs
6. Country Streaming Songs
Please select sub-category: 5
Gathering Information...
                                                    0
Die A Happy Man  by  Thomas Rhett                   1
You Should Be Here  by  Cole Swindell               2
Humble And Kind  by  Tim McGraw                     3
Somewhere On A Beach  by  Dierks Bentley            4
H.O.L.Y.  by  Florida Georgia Line                  5
Peter Pan  by  Kelsea Ballerini                     6
Forever Country  by  Artists Of Then, Now & For...  7
Setting The World On Fire  by  Kenny Chesney Fe...  8
Blue Ain't Your Color  by  Keith Urban              9
Would you like to listen to one of them? If so which one: 1
Billboard_Player.py:17: DeprecationWarning: use options instead of chrome_options
  browser = webdriver.Chrome('/Users/cristiansoria/Downloads/chromedriver', chrome_options=options)
Die A Happy Man  by  Thomas Rhett
Loading song...
Playing preview...
Keep listening? (y/n): y
Would you like to go back? (y/n): y
Would you like the same chart or different? (s/d):s
                                                    0
Die A Happy Man  by  Thomas Rhett                   1
You Should Be Here  by  Cole Swindell               2
Humble And Kind  by  Tim McGraw                     3
Somewhere On A Beach  by  Dierks Bentley            4
H.O.L.Y.  by  Florida Georgia Line                  5
Peter Pan  by  Kelsea Ballerini                     6
Forever Country  by  Artists Of Then, Now & For...  7
Setting The World On Fire  by  Kenny Chesney Fe...  8
Blue Ain't Your Color  by  Keith Urban              9
Would you like to listen to one of them? If so which one: 9
Blue Ain't Your Color  by  Keith Urban
Loading song...
Playing preview...
Keep listening? (y/n): n
Would you like to go back? (y/n): n
Have a good day!
```

