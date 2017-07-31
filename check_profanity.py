import urllib

def read_text():
    quotes = open("/Users/lquintanilla/Desktop/quotes.txt")
    contents_of_file = quotes.read()
    # print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    # print(output)
    connection.close()
    if "true" in output:
        print("Shit Alert!")
    elif "false" in output:
        print("No profanity found!")
    else:
        print("could not read the document, try again!")
    
read_text()
