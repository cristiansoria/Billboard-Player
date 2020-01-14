from selenium import webdriver
import re
import pandas as pd
import time
songs = {}
from selenium.webdriver.common.keys import Keys


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def playSong(song):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    browser = webdriver.Chrome('$PATH', chrome_options=options)
    browser.get("https://soundcloud.com")
    try:
        search = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/span/span/form/input")
        but = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/span/span/form/button")
        print(song)
        search.send_keys(str(song))
        but.click()
        print("Loading song...")
        time.sleep(2)
        button = browser.find_element_by_class_name("soundTitle__playButton")
        print("Playing preview...")
        button.click()
        time.sleep(10)
        button.click()
        keep_going = input("Keep listening? (y/n): ")
        if str(keep_going) == "y":
            button.click()
            time.sleep(20)
        browser.close()
        more = input("Would you like to go back? (y/n): ")
        if str(more) == "y":
            same = input("Would you like the same chart or different? (s/d):")
            if(str(same)) == "d":
                checkCharts()
            else:
                print(df)
                num = input("Would you like to listen to one of them? If so which one: ")
                song = str(songs.get(int(num)))
                playSong(song)
        else:
            print("Have a good day!")


    except:
        print("error")

def checkCharts():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    browser = webdriver.Chrome('$PATH', chrome_options=options)
    try:
        year = input("Select a year from 1958 - 2018 : ")
        browser.get("https://www.billboard.com/archive/charts/"+str(year))
        genre = {}

        genre = list(browser.find_elements_by_class_name("chart-group__title"))
        for i in range(len(genre)-1):
            print(str(i+1) + ". " + str(genre[i].text))

        menu_input = int(input("What genre would you like to view: "))
        menu_input -=1
        chart_groups = browser.find_elements_by_class_name("chart-group")
        unlisted_categories = str(chart_groups[int(menu_input)].text)
        listed_categories = unlisted_categories.split("\n")
        for i in range(len(listed_categories)-1):
            print(str(i+1) + ". " + str(listed_categories[i+1]))

        category_input = input("Please select sub-category: ")
        choice = listed_categories[int(category_input)]
        path = browser.find_elements_by_link_text(choice)
        link = browser.find_element_by_link_text(path[0].text).get_attribute("href")

        browser.get(link)

        info = list(browser.find_elements_by_tag_name("td"))
        counter = 1
        date = {}
        run = True
        songs.clear()
        while(run):
            print("Gathering Information...")
            for i in range(len(info)-1):
                if hasNumbers(info[i].text) and not hasNumbers(info[i+1].text):
                    pass
                elif not hasNumbers(info[i].text) and not hasNumbers(info[i+1].text):
                    songs[counter] = str(info[i].text) + "  by  " + str(info[i+1].text)
                    counter+=1
            run = False

        global df
        df = pd.DataFrame(songs.keys(), songs.values())
        print(df)

        num = input("Would you like to listen to one of them? If so which one: ")
        browser.close()
        if hasNumbers(num):
            song = str(songs.get(int(num)))
            playSong(song)
        else:
            print("Have a great day!")
    except:
        print("error")


checkCharts()
