{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import Dependecies \n",
    "from bs4 import BeautifulSoup \n",
    "from splinter import Browser\n",
    "import pandas as pd \n",
    "import requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "expected an indented block (<ipython-input-7-bcf5b4a4555c>, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-7-bcf5b4a4555c>\"\u001b[0;36m, line \u001b[0;32m2\u001b[0m\n\u001b[0;31m    executable_path = {\"executable_path\": \"chromedriver.exe\"}\u001b[0m\n\u001b[0m                  ^\u001b[0m\n\u001b[0;31mIndentationError\u001b[0m\u001b[0;31m:\u001b[0m expected an indented block\n"
     ]
    }
   ],
   "source": [
    "def init_browser(): \n",
    "executable_path = {\"executable_path\": \"chromedriver.exe\"}\n",
    "return Browser(\"chrome\", **executable_path, headless=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrape():\n",
    "    browser = init_browser()\n",
    "    mars_facts_data = {}\n",
    "\n",
    "    nasa = \"https://mars.nasa.gov/news/\"\n",
    "    browser.visit(nasa)\n",
    "    time.sleep(2)\n",
    "\n",
    "    html = browser.html\n",
    "    soup = bs(html,\"html.parser\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unexpected indent (<ipython-input-9-85f021164a8b>, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-9-85f021164a8b>\"\u001b[0;36m, line \u001b[0;32m2\u001b[0m\n\u001b[0;31m    news_paragraph = soup.find(\"div\", class_=\"article_teaser_body\").text\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mIndentationError\u001b[0m\u001b[0;31m:\u001b[0m unexpected indent\n"
     ]
    }
   ],
   "source": [
    "news_title = soup.find(\"div\",class_=\"content_title\").text\n",
    "    news_paragraph = soup.find(\"div\", class_=\"article_teaser_body\").text\n",
    "    mars_facts_data['news_title'] = news_title\n",
    "    mars_facts_data['news_paragraph'] = news_paragraph "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "mars_info = {}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "unexpected EOF while parsing (<ipython-input-13-64128bcaaf99>, line 28)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-13-64128bcaaf99>\"\u001b[0;36m, line \u001b[0;32m28\u001b[0m\n\u001b[0;31m    return mars_info\u001b[0m\n\u001b[0m                    ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m unexpected EOF while parsing\n"
     ]
    }
   ],
   "source": [
    "def scrape_mars_news():\n",
    "    try: \n",
    "\n",
    "        # Initialize browser \n",
    "        browser = init_browser()\n",
    "\n",
    "        #browser.is_element_present_by_css(\"div.content_title\", wait_time=1)\n",
    "\n",
    "        # Visit Nasa news url through splinter module\n",
    "        url = 'https://mars.nasa.gov/news/'\n",
    "        browser.visit(url)\n",
    "\n",
    "        # HTML Object\n",
    "        html = browser.html\n",
    "\n",
    "        # Parse HTML with Beautiful Soup\n",
    "        soup = BeautifulSoup(html, 'html.parser')\n",
    "\n",
    "\n",
    "        # Retrieve the latest element that contains news title and news_paragraph\n",
    "        news_title = soup.find('div', class_='content_title').find('a').text\n",
    "        news_p = soup.find('div', class_='article_teaser_body').text\n",
    "\n",
    "        # Dictionary entry from MARS NEWS\n",
    "        mars_info['news_title'] = news_title\n",
    "        mars_info['news_paragraph'] = news_p\n",
    "\n",
    "        return mars_info"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "unexpected EOF while parsing (<ipython-input-14-9fa19db5fe88>, line 35)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-14-9fa19db5fe88>\"\u001b[0;36m, line \u001b[0;32m35\u001b[0m\n\u001b[0;31m    return mars_info\u001b[0m\n\u001b[0m                    ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m unexpected EOF while parsing\n"
     ]
    }
   ],
   "source": [
    "def scrape_mars_image():\n",
    "\n",
    "    try: \n",
    "\n",
    "        # Initialize browser \n",
    "        browser = init_browser()\n",
    "\n",
    "        #browser.is_element_present_by_css(\"img.jpg\", wait_time=1)\n",
    "\n",
    "        # Visit Mars Space Images through splinter module\n",
    "        image_url_featured = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "        browser.visit(image_url_featured)# Visit Mars Space Images through splinter module\n",
    "\n",
    "        # HTML Object \n",
    "        html_image = browser.html\n",
    "\n",
    "        # Parse HTML with Beautiful Soup\n",
    "        soup = BeautifulSoup(html_image, 'html.parser')\n",
    "\n",
    "        # Retrieve background-image url from style tag \n",
    "        featured_image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]\n",
    "\n",
    "        # Website Url \n",
    "        main_url = 'https://www.jpl.nasa.gov'\n",
    "\n",
    "        # Concatenate website url with scrapped route\n",
    "        featured_image_url = main_url + featured_image_url\n",
    "\n",
    "        # Display full link to featured image\n",
    "        featured_image_url \n",
    "\n",
    "        # Dictionary entry from FEATURED IMAGE\n",
    "        mars_info['featured_image_url'] = featured_image_url \n",
    "        \n",
    "        return mars_info"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "unexpected EOF while parsing (<ipython-input-15-f61b6885f2bd>, line 36)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-15-f61b6885f2bd>\"\u001b[0;36m, line \u001b[0;32m36\u001b[0m\n\u001b[0;31m    return mars_info\u001b[0m\n\u001b[0m                    ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m unexpected EOF while parsing\n"
     ]
    }
   ],
   "source": [
    "def scrape_mars_weather():\n",
    "\n",
    "    try: \n",
    "\n",
    "        # Initialize browser \n",
    "        browser = init_browser()\n",
    "\n",
    "        #browser.is_element_present_by_css(\"div\", wait_time=1)\n",
    "\n",
    "        # Visit Mars Weather Twitter through splinter module\n",
    "        weather_url = 'https://twitter.com/marswxreport?lang=en'\n",
    "        browser.visit(weather_url)\n",
    "\n",
    "        # HTML Object \n",
    "        html_weather = browser.html\n",
    "\n",
    "        # Parse HTML with Beautiful Soup\n",
    "        soup = BeautifulSoup(html_weather, 'html.parser')\n",
    "\n",
    "        # Find all elements that contain tweets\n",
    "        latest_tweets = soup.find_all('div', class_='js-tweet-text-container')\n",
    "\n",
    "        # Retrieve all elements that contain news title in the specified range\n",
    "        # Look for entries that display weather related words to exclude non weather related tweets \n",
    "        for tweet in latest_tweets: \n",
    "            weather_tweet = tweet.find('p').text\n",
    "            if 'Sol' and 'pressure' in weather_tweet:\n",
    "                print(weather_tweet)\n",
    "                break\n",
    "            else: \n",
    "                pass\n",
    "\n",
    "        # Dictionary entry from WEATHER TWEET\n",
    "        mars_info['weather_tweet'] = weather_tweet\n",
    "        \n",
    "        return mars_info\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrape_mars_facts():\n",
    "\n",
    "    # Visit Mars facts url \n",
    "    facts_url = 'http://space-facts.com/mars/'\n",
    "\n",
    "    # Use Panda's `read_html` to parse the url\n",
    "    mars_facts = pd.read_html(facts_url)\n",
    "\n",
    "    # Find the mars facts DataFrame in the list of DataFrames as assign it to `mars_df`\n",
    "    mars_df = mars_facts[0]\n",
    "\n",
    "    # Assign the columns `['Description', 'Value']`\n",
    "    mars_df.columns = ['Description','Value']\n",
    "\n",
    "    # Set the index to the `Description` column without row indexing\n",
    "    mars_df.set_index('Description', inplace=True)\n",
    "\n",
    "    # Save html code to folder Assets\n",
    "    data = mars_df.to_html()\n",
    "\n",
    "    # Dictionary entry from MARS FACTS\n",
    "    mars_info['mars_facts'] = data\n",
    "\n",
    "    return mars_info\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrape_mars_hemispheres():\n",
    "\n",
    "    try: \n",
    "\n",
    "        # Initialize browser \n",
    "        browser = init_browser()\n",
    "\n",
    "        # Visit hemispheres website through splinter module \n",
    "        hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "        browser.visit(hemispheres_url)\n",
    "\n",
    "        # HTML Object\n",
    "        html_hemispheres = browser.html\n",
    "\n",
    "        # Parse HTML with Beautiful Soup\n",
    "        soup = BeautifulSoup(html_hemispheres, 'html.parser')\n",
    "\n",
    "        # Retreive all items that contain mars hemispheres information\n",
    "        items = soup.find_all('div', class_='item')\n",
    "\n",
    "        # Create empty list for hemisphere urls \n",
    "        hiu = []\n",
    "\n",
    "        # Store the main_ul \n",
    "        hemispheres_main_url = 'https://astrogeology.usgs.gov' \n",
    "\n",
    "        # Loop through the items previously stored\n",
    "        for i in items: \n",
    "            # Store title\n",
    "            title = i.find('h3').text\n",
    "            \n",
    "            # Store link that leads to full image website\n",
    "            partial_img_url = i.find('a', class_='itemLink product-item')['href']\n",
    "            \n",
    "            # Visit the link that contains the full image website \n",
    "            browser.visit(hemispheres_main_url + partial_img_url)\n",
    "            \n",
    "            # HTML Object of individual hemisphere information website \n",
    "            partial_img_html = browser.html\n",
    "            \n",
    "            # Parse HTML with Beautiful Soup for every individual hemisphere information website \n",
    "            soup = BeautifulSoup( partial_img_html, 'html.parser')\n",
    "            \n",
    "            # Retrieve full image source \n",
    "            img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']\n",
    "            \n",
    "            # Append the retreived information into a list of dictionaries \n",
    "            hiu.append({\"title\" : title, \"img_url\" : img_url})\n",
    "\n",
    "        mars_info['hiu'] = hiu\n",
    "        \n",
    " # Return mars_data dictionary \n",
    "\n",
    "        return mars_info\n",
    "    finally:\n",
    "\n",
    "        browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
