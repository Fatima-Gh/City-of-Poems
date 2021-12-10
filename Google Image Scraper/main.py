# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:02:06 2020

@author: OHyic

"""
#Import libraries
from GoogleImageScrapper import GoogleImageScraper
import os
import pandas as pd


df = pd.read_csv('tokens_counter.csv')

    
if __name__ == "__main__":
    #Define file path
    webdriver_path = os.path.normpath(os.getcwd()+"\\webdriver\\chromedriver.exe")
    image_path = os.path.normpath(os.getcwd()+"\\photos")
        
    tokens = df['Word']
    print(tokens)

    #Add search terms into array
    search_keys = tokens 

    #Parameters
    number_of_images = 100
    headless = True
    min_resolution=(0,0)
    max_resolution=(9999,9999)

    #Main program
    for search_key in search_keys:
        try:
            image_scrapper = GoogleImageScraper(webdriver_path,image_path,search_key,number_of_images,headless,min_resolution,max_resolution)
            image_urls = image_scrapper.find_image_urls()
            image_scrapper.save_images(image_urls)
        except Exception as e:
            print('~~ Error --> ', str(e))
            pass
    
    #Release resources    
    del image_scrapper