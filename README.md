# Information_retrieval_System
Problem Statement -
You are given a data set of public review for product along with review text and score, you have
to build an IR (Information Retrieval) system. When a user can come and search their keywords
and based on that the review text with the highest review score and helpfulness should appear.
Sample row:
product/productId: B001E4KFG0
review/userId: A3SGXH7AUHU8GW
review/profileName: delmartian
review/helpfulness: 1/1
review/score: 5.0
review/time: 1303862400
review/summary: Good Quality Dog Food
review/text: I have bought several of the Vitality canned dog food products and have found them
all to be of good quality. The product looks more like a stew than a processed meat and it
smells better. My Labrador is finicky and she appreciates this product better than most

Features:
- Management command to load and index the complete dataset to database model
- UI for client for search the data and get the result (Highlighting search keyword in result
would be addon)
- Complete development track should be available on github and share github link for
submission.

Solution-

1. Please open "PRODUCT REVIEW SEARCH - Assignment.pdf" and download source file from given link.
   Please place foods.txt after untar foods.txt.gz and place it at myapp\management\Files location to load the django model
2. Please go to IRSystem\ location and follow below steps sequentially
3. Run below command
    pip install requirement.txt
4. Run the below commands to migrate the model-
    python manage.py makemigrations
    python manage.py migrate
5. To perform the feature 1 Management command to load and index the complete dataset to database model please run the below command :-
    python manage.py management
6. Please run the below command and navigate to http://127.0.0.1:8000/ URL in the browser to launch the application :-
    python manage.py runserver
