# grab-data-from-web-site-and-make-excel-files
Grab some data from a web site and make an excel with that data.

This mini project built in python is designed to work automatically. It get data from an url that has employee information with a custom stored id, then I extract it from his html tags with BeautifulSoup library. 

Once we get the data we want from getContentFromUrl, this program calls another script 'excel.py' wich creates excel files from each request. We use xlsxwriter library to make those files.

Finally, a custom flow  (Microsoft Flow, not shown in this repo) is automatically run in wich get those excel files, get the email of the employee, and sending a custom email with the attached excel file.  
