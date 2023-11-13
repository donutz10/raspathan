# Athan Alert for Raspberry Pi

This Python script is designed to fetch Islamic prayer times for Doha, Qatar, from a specified website and alert the user at each prayer time by playing a specific **Athan** file.

## Features
Fetches prayer times from a specified URL using web scraping techniques.
Plays a distinct audio file when it is time for each prayer.
At 11:59 PM each day, the script waits for 5 minutes and then refreshes the prayer times for the next day.
Different **Athan**  files are played for Fajr and other prayer times.

## Requirements
Python 3.x
Libraries: requests, lxml, pygame
Internet connection to fetch the latest prayer times.

### Installation
Before running the script, ensure you have Python installed on your system and the required libraries. You can install the libraries using pip:

```
pip install requests lxml pygame
```

1. Place the script in a desired directory.
2. Ensure that the **Athan** files 1.wav (for Dhuhr, Asr, Maghrib, Isha) and 2.wav (for Fajr) are in the same directory as the script or provide the full path in the script.
3. Run the script using Python:

```
python prayer_times_alert.py
```
The script will continuously run, checking the current time against the fetched prayer times. Ensure to terminate the script manually when it is no longer needed.

## How It Works
* The script first fetches the current day's prayer times from "https://www.islamicfinder.org/world/qatar/" using the lxml library.
* It then enters a loop, checking the current time every minute.
* When the current time matches a prayer time, the script plays the corresponding audio file (2.wav for Fajr and 1.wav for other prayers).
* At 11:59 PM, the script sleeps for 5 minutes and then refreshes the prayer times for the next day.
## Changing the City Location
1. **Identify the New City URL:**
     - Visit the Islamic Finder website or the specific website from which the script fetches prayer times.
     - Navigate to the page that displays prayer times for the desired city.
     - Copy the URL of this page.


2. **Update the Script:**

   - Open the Python script in a text editor.
   - Find the line that sets the prayer_url. It will look something like this:

```
prayer_url = "https://www.islamicfinder.org/world/qatar/290030/doha-prayer-times/"
```
   **Replace this URL with the URL of the new city's prayer times page.**

### Grabbing the Correct Selector
To update the selectors (XPath) in the script for a new city, follow these steps:

1. **Open the Web Page in a Browser:**
   - Open the prayer times page of the new city in a web browser.
2. **Use Developer Tools to Inspect Elements:**

   - Right-click on the prayer time you want to fetch (e.g., Fajr time) and select "Inspect" or "Inspect Element". This opens the developer tools and highlights the HTML element corresponding to that prayer time.

   - Look for a unique identifier or a consistent pattern in the HTML structure that you can use to write an XPath. It could be an **id**, a **class**, or a specific HTML tag structure.

3. **Write the XPath:**

    - Based on the HTML structure, write an XPath that uniquely identifies the prayer time element.
For example, if the Fajr time is in a **'td'** tag under a **'table'** with a **'specific id'**, the XPath might look like:
```
//*[@id="specific-table-id"]/tbody/tr[2]/td[2]

```
**Repeat this process for each prayer time.**

4. **Update the XPaths in the Script:** 

     - In the script, locate the xpaths dictionary.
     - Update the XPaths for each prayer time with the new ones you've written.
## Final Note
This script is specifically tailored for Doha, Qatar. Modifications would be required to adapt it for other locations.
The accuracy of the prayer times is dependent on the source website. Ensure that the website is reliable and up-to-date.
Running this script continuously may consume system resources. It's advisable to run it on a dedicated device.

Remember, web scraping depends heavily on the specific structure of the web page. Any changes to the website's layout may require updates to the XPaths. Also, ensure that your use of the website's data is in compliance with their terms of service or any usage policies they might have.