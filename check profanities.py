import urllib
def read_text():
    quotes=open(r"C:\Users\tan\Documents\python learning\movie_quotes.txt")
    contents_of_file= quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)
    pirate(contents_of_file)
    
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output=connection.read()
    if "true" in output:
        print("Profanity alert!")
    elif "false" in output:
        print("document is clean")
    else:
        print("could not scan document")
    connection.close()
def pirate(text_to_pirate):
    connection =urllib.urlopen("http://isithackday.com/arrpi.php?text="+text_to_pirate)
    output=connection.read()
    print(output)

read_text()
