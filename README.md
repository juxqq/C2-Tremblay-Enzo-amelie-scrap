# C2-Tremblay-Enzo-amelie-scrap
This is a script that scrapes data on French doctors from the Ameli directory and saves it as a CSV file. The script uses the Python libraries requests, re, BeautifulSoup, and pandas.

<h1>Usage</h1>
To use this script, you will need to install the required libraries. You can install them by running the following command in your terminal :<code>pip install requests re bs4 pandas</code>.<br />
Once you have installed the libraries, you can simply run the script by executing <code>python main.py</code> from the terminal. The script will scrape data on doctors from the Ameli directory and save it as a medecins.csv file.

<h1>Dependencies</h1>
This script depends on the following libraries:
<ul>
<li>requests: used to make HTTP requests to the website</li>
<li>re: used to perform regular expression operations</li>
<li>bs4: used to parse the HTML content of the pages</li>
<li>pandas: used to create a dataframe and save the data as a CSV file</li>
</ul>

<h1>Limitations</h1>
This script is limited by the structure of the website it is scraping. If the website changes its structure, the script may need to be updated accordingly. Additionally, the script is only set to scrape data on 20 pages of the directory. You can increase or decrease the number of pages by changing the range in the for url in range(20) loop.
