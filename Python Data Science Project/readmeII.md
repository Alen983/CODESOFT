## Beautiful Soup.  
Beautiful Soup is a Python library for pulling data out of HTML and XML files. This is accomplished by representing the HTML as a set of objects with methods used to parse the HTML. We can navigate the HTML as a tree and/or filter out what we are looking for.  

#### Soupified Action
First,Entire HTML element is stored as string to variable html.  
To parse a document, pass it into the **BeautifulSoup** constructor, the **BeautifulSoup** object, which represents the document as a nested data structure:  
```soup = BeautifulSoup(html, "html.parser")```  

#### Soup kicking in'
First, the document is converted to Unicode, (similar to ASCII), and HTML entities are converted to Unicode characters. Beautiful Soup transforms a complex HTML document into a complex tree of Python objects. The BeautifulSoup object can create other types of objects. In this lab, we will cover BeautifulSoup and Tag objects that for the purposes of this lab are identical, and NavigableString objects.  

We can use the method prettify() to display the HTML in the nested structure:  
```print(soup.prettify())```  

[Soup recipie in detail](https://labs.cognitiveclass.ai/v2/tools/jupyterlab?ulid=ulid-ba67a5a5eb98df57e67bad3aa7cd10d886d03949)


<hr>

## Project Overview
For this project, you will assume the role of a Data Scientist / Data Analyst working for a new startup investment firm that helps customers invest their money in stocks. Your job is to extract financial data like historical share price and quarterly revenue reportings from various sources using Python libraries and webscraping on popular stocks. After collecting this data you will visualize it in a dashboard to identify patterns or trends. The stocks we will work with are Tesla, Amazon, AMD, and GameStop
