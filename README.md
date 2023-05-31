# dj4e
Learn Django -  https://www.dj4e.com/
 3-html
 4-css

project: https://hudir.pythonanywhere.com/

get samples code 
```bash
git clone git@github.com:csev/dj4e-samples.git
```


 # Wrong and unknown Q&A

## Which of the following files in a Django application most closely captures the notion of "View"?
 - templates/polls/main.html

## Which file represents the "Controller" aspect of a Django application?
 - It is not as simple as that (42)

## What does the built-in Django template tag "spaceless" do?
 - Removes whitespace between HTML tags. This includes tab characters and newlines.
 Only space between tags is removed – not space between tags and text. In this example, the space around Hello won’t be stripped:

{% spaceless %}
    <strong>
        Hello
    </strong>
{% endspaceless %}

## What does the built-in Django template filter "length" do?
Returns the length of the value. This works for both strings and lists.

## What is the built-in Django template filter to count the number of words in a string? [_____]
wordcount
Returns the number of words.

## Looking at the Django built-in template and filter documentation, the author seems to have a pet named "Joel". What kind of animal is their pet?
"Joel is a slug"

## What does the Django built-in template tag forloop.counter represent in a Django template?
forloop.counter	The current iteration of the loop (1-indexed)
forloop.counter0	The current iteration of the loop (0-indexed)

## In Object Oriented Programming, what is another name for the attributes of an object?
fields

## Which of the following is NOT a good synonym for "class" in Python?
direction

## Which of the following is rarely used in Object Oriented Programming?
 Destructor


## In the class django.views.generic.list.ListView, which of the following methods is called earliest in the process?

 get_template_names() 

 ## What does the django.urls.reverse() function do?
 It constructs the path to a view using the name of a path entry in urls.py


 ## In polls/templates/polls/detail.html file in Django tutorial 4, what happens if you leave out the csrf_token line in the form?
  The post data will be blocked by the server

 ## What does the Django template filter "pluralize" do?
 It emits an 's' if the value is > 1

 ## Which of the following is the label we give a column that the "outside world" uses to look up a particular row?
 Logical key

 ## When you add an index to a field in a database table, how are performance and storage affected?
 Read performance is faster, insert performance is slower and extra storage is required

 ## Which best describes the Django functionality that puts up the login form?
 Application

 ## What is the default name of the emplate that Django will load when presenting the user with a login screen?
 registration/login.html

 ## Which of the following is *not* a benefit of using the Django forms capability?
 Database portability

 ## You cannot use a Django form unless it is connected to a Django Model.
 False

 ## How to you indicate that you want to display a form using the Crispy library in a template?
 form|crispy

 ## What utility method simplifies the code needed to load the old model data when processing an update request?
  get_object_or_404()


## Why do we insist on producing a delete confirmation screen?
Because a GET request should never modify data

## Which of the following methods is called first in the Django generic list view?
 setup()

## What is the template variable that indicates the current logged in user?
 user

##  In OwnerUpdateView, how do we make sure that the current logged in user cannot retrieve any rows that don't belong to them?
We add a model filter

## When a generic edit view is receiving POST data which of the following steps is done first?
clean()