# Craigslist Automation
The goal of this project is to automate the process of posting advertisements on craigslist.

## Steps:
1. Use requests module to grab the landing page html 
2. Use bs4 to find all the links of the available local posting locations
3. Clean up the link data using string replace (and regex if necessary)
4. Make a separate list for the links and for the locations.
5. Loop thru the locations list to find a zip code for each location on the list. (Use either requests or selenium web driver, NOT ahk/pmc or other basic automation software which are too finiky wrt page loading times) [I used selenium for practice, though requests may be better option, since you don't really need an actual web browser]
6. Create a dataframe in pandas with each of the lists (location, link, zip) and set the index column as the location.
8. Store the dataframe as a pickle file.
9. Reload the pickle file some time later along with all the appropriate posting data (login info, ad content, etc.)
10. Use selenium to navigate to a location's link then automate a series of clicks to post an ad to that particular location.
11. Loop through multiple locations and email/password combinations to batch post.
12. Renew ads automatically with selenium.
