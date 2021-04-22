# Useful media:
    # Python post requests: https://gist.github.com/JeffPaine/3145490
    # Intro: https://medium.com/analytics-vidhya/getting-started-with-github-api-dc7057e2834d
    # Token: 

import json
import requests


user = "jacobPenney"
repo = "texts"
token = ""
issue_number = 2
request_headers = { "Authorization" : "token {}".format( token ) } 
 
url_base = "https://api.github.com/"
issues_api = "repos/%s/%s/issues" % ( user, repo ) 
labels_api = issues_api + "%s/labels" % ( issue_number )


def main(  ):

    menu_choice = input("Would you like to:\n 1) Create an issue\n 2) Add labels\n")
    
    if menu_choice == "1":
        create_issue()

    elif menu_choice == "2":
        add_labels()

    elif menu_choice == "3":
        remove_labels() 

    # print( menu_choice )




def create_issue():
    user = "jacobPenney"
    repo = "texts"
    token = ""
    request_headers = { "Authorization" : "token {}".format( token ) } 
     
    url_base = "https://api.github.com/"
    issues_api = "repos/%s/%s/issues" % ( user, repo ) 
 
    issue = {
                'title': "This is another test",
                'labels': ["bug"]
            }

    
    payload = json.dumps( issue )

    request_outcome = requests.post( url_base + issues_api, data=payload,
                                     headers = request_headers )

    print( request_outcome.json() )  




def add_labels():
    user = "jacobPenney"
    repo = "texts"
    token = ""
    issue_number = 1
    request_headers = { 
                        'Content-Type': 'application/json',
                        "Authorization" : "token {}".format( token ) 
                      } 
     
    url_base = "https://api.github.com/"
    labels_api = "repos/%s/%s/issues/%s/labels" % ( user, repo, issue_number ) 

    label_input = input( "\nWhat labels to include? " )

    payload = json.dumps( [label_input] )

    request_outcome = requests.put( url_base + labels_api, payload,
                                     headers = request_headers )

    print( request_outcome.json() )   




def remove_labels():
    user = "jacobPenney"
    repo = "texts"
    token = ""
    issue_number = 1
    request_headers = { 
                        'Content-Type': 'application/json',
                        "Authorization" : "token {}".format( token ) 
                      } 
     
    url_base = "https://api.github.com/"
    labels_api = "repos/%s/%s/issues/%s/labels" % ( user, repo, issue_number ) 

    # label_input = input( "\nWhat labels to delete? " )

    # payload = json.dumps( label_input )

    request_outcome = requests.delete( url_base + labels_api, headers = request_headers )

    print( request_outcome.json() )    




if __name__ == "__main__":
    main()





# owner = argv[0]
# repo_name = argv[1]
# username =  argv[0]
# passwd = argv[1] 
