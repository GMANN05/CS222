import urllib
import json
import urllib.request
import sys


def search():
    #check article name
    if len(sys.argv) < 2:
        print("No valid input string, Error code 1")
        exit(1)

    search_string = sys.argv[1]
    url = "https://www.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "format": "json",
        "titles": search_string,
        "prop": "revisions|redirects",
        "rvprop": "timestamp|user|comment",
        "rdprop": "title",
        "rvlimit": 30,
        "redirects": True,
        "rvslots": "main",
        "formatversion": "2"
    }

    params_encoded = urllib.parse.urlencode(params)
    full_url = f"{url}?{params_encoded}"

    #wikipedia API data fetch
    try:
        with urllib.request.urlopen(full_url) as response:
            data = response.read().decode('utf-8')
            json_data = json.loads(data)
    except urllib.error.URLError:
        print("Invalid Network Connection, Error Code 3")
        exit(3)

    #missing pages
    pages = json_data.get("query", {}).get("pages", [])
    if not pages:
        print("Page Not Found, Error Code 2")
        exit(2)

    #print redirect information
    redirects = json_data.get("query", {}).get("redirects", [])
    if redirects:
        for redirect in redirects:
            print(f"Redirected from: {redirect['from']}\nRedirected to: {redirect['to']}")
    else:
        print("No Redirects")

    #print revisions information
    for page in pages:
        revisions = page.get("revisions", [])
        if revisions:
            for revision in revisions:
                user = revision.get("user", "Unknown User")
                timestamp = revision.get("timestamp", "Unknown Time")
                comment = revision.get("comment", "No Comment")
                print(f"Username: {user} | Timestamp: {timestamp} | Comments: {comment}\n")
        else:
            print("Revisions Not Found")
    
    exit(0)

#call
search()