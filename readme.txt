The goal is to automate the process of posting tutoring ads on craigslist.

Steps:
1. Use requests module to grab the landing page html 
2. Use bs4 to find all the links in the available posting locations
3. Clean up the link data using string replace (and regex only if necessary)
4. Make a separate list for the links and for the locations. Consider connecting them with a dictionary (zip)
5. Loop thru the locations list finding a zip code for each location on the list (use either python requests or selenium web driver NOT ahk or pmc which are too finiky wrt load times) [I used selenium for practice, though requests may be better option since you don't really need an actual web browser]
6. Create a dataframe in pandas with each of the lists (location, link, zip) and set the index column as the location.
8. Store the dataframe pickle file.
9. Use selenium to navigate to a location's link then automate a series of clicks to post an ad to that particular location.
