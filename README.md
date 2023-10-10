# tb-sqli-tool

A very basic python3 script for performing time based SQL Injection. Changes to the payload and location of such payload need to manually added by the user on the code.


## Usage

```
tb-sqli-tool$ python3 brute.py -h
usage: brute.py [-h] [-u URL] [-t TIME]

A Python script to help with SQLi.
The payload needs to be changed manually as well as the post data or request type
If the payload needs to be inserted into the url then you must also make these changes to the script

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Specify the url to attack
  -t TIME, --time TIME  Specify the time to wait in seconds
```


```
tb-sqli-tool$ python3 brute.py -u http://exposed_url.com/login -t 3
```
