# Overview

For this project I was trying to learn Django. I have worked with other webframeworks in the past, but never this one. I thought learning this framework would be a good way to display some of the projects that I have created while in school. There are some issues that I am still working on, but it is a good start. 
To open up this applictaion you type "py manage.py runserver" this will differ based on your opperating system. In order to get to the home page, you have to type in /projects into the url. This brings you to the home page which has a navigation bar a count of the projects in the database and eventually it will have a display of each project. 

[Software Demo Video](https://youtu.be/8tPPLPFqAa4)

# Web Pages

I have three pages in this web applictaion: a home page, a projects page, and a contact page. You can navigate to each of these pages through the nav bar at the top. The home page dynamically updates when you create a new entry in the database. There is a little section that tells you the count of projects. The page updates with each new entry. There is a for loop in the code that creates a card to display each project on the page. The contact page simply has a form for people to leave messages.

# Development Environment

I used vidual studio code to develop this web app. The programming language I used was python with the django framework. I also had to use some html and css to create templates for the page to display information. 

# Useful Websites

* [Mozilla Developer](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction)
* [W3 Schools](https://www.w3schools.com/django/django_intro.php)

# Future Work

* The biggest thing I want to fix is the issue with the url that is automatically opened when you run the server. I don't want users to have to type /projects into the url because that's bad UX.
* I need to figure out why my code is not displaying the data of each database entry.
* I want to work on the design of the site and make it more beautiful.