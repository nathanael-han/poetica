<a name="br1"></a> 

Nathanael Han

CSCI E33-a

Final Project:

**Poetica**

For my final project I made a web application called Poetica. Poetica is a

forum/social network site where users can share their poetry and view the poetry of

other writers.

The features on my website include:

• A home page where all the posted poems can be viewed

• A page that lists the poets registered on the site

• A page where users can post a poem using a rich text editor

• Like/unlike functionality

• Users can delete their posts

• A page that displays the poems a user has liked

• Clicking each poem title leads to a page displaying that individual

poem

o On this page users can comment on the displayed poem.

• Profile pictures for each poet

• Profile pages for each user, displaying poems posted by the user

o The profile page allows a user to post a “status” on their

own page.

• Mobile navigation

• Pagination for the poets, liked, poems, and profile pages.

• A dark mode toggle button



<a name="br2"></a> 

**Requirements:**

[Django](https://django-ckeditor.readthedocs.io/en/latest/)[ ](https://django-ckeditor.readthedocs.io/en/latest/)[Ckeditor](https://django-ckeditor.readthedocs.io/en/latest/)

**Log in credentials:**

Superuser:

username: user1

email: user1@gmail.com

password: cse33spring

Other accounts:

password: cse33spring

**Files:**

Finalproject directory:

o In settings.py I configured the appearance of the Ckeditor

Users directory:

This app includes the user authentication functionality.

o views.py: contains the views for login, logout and registration

o templates:

o registration.html

▪ displays the form fields to create a new account

o login.html

▪ displays the form to log in to an account



<a name="br3"></a> 

**Poetica directory/app:**

**Static files:**

Assets folder: contains svg and png files used on the site

Stylesheets: dark\_mode.css and styles.css

Poetica.js:

o Defines stylesheets — later used in the currentMode( ) and changeColor( )

functions.

o Initializes AOS (Animate on Scroll Library)

o I used this library to animate the posts as the page is scrolled

o One problem I ran into with using this library was that when I refreshed

the page, the posts would disappear.

▪ I was able to find a fix for this online to correctly load the AOS

library [(](https://github.com/michalsnik/aos/issues/239)<https://github.com/michalsnik/aos/issues/239>[)](https://github.com/michalsnik/aos/issues/239)

o When DOM is loaded:

o Mobile navigation element is selected

o On click, display is toggled

o Dark mode switch is selected

o If the dark mode state isn’t yet saved, it is given a default setting of false

o The currentMode( ) function is called to check the theme setting and

change the stylesheet accordingly

o Functions:

o currentMode( ): uses conditionals to check the theme setting, then

modifies the logo and stylesheet included in the html

o changeColor( ): when the switch is toggled, the localStorage setting is

updated, then the logo and stylesheet are modified in the html.

o likePoem( ): references the view to retrieve the number of likes on a

poem. After the like button is pressed, the function hides the like button



<a name="br4"></a> 

and displays the unlike button. Lastly, the current number of likes is

updated on the html.

o unlikePoem( ): references the view to retrieve the number of likes on a

poem. After the like button is pressed, the function hides the unlike

button and displays the like button. Then the current number of likes is

updated in the html.

**Templates:**

layout.html: the basic template for the pages on the site.

o References poetica.js

o In the head of this document, I include a style tag to hide the html. When the

stylesheets are loaded, the html is set to visible. This prevents the pages from

briefly displaying without styling, when the dark mode switch is toggled.

(reference: <https://bojanvidanovic.com/blog/css-solutions-fouc/>[)](https://bojanvidanovic.com/blog/css-solutions-fouc/)

o Includes the navigation links

o Some links are only displayed if a user is logged in.

o Includes the bootstrap toggle switch for dark mode.

index.html: displays each poem posted to the website. Uses a for loop to iterate

through the list of poems.

Poem display:

If the poster of a given poem has a profile picture, that photo is displayed. If

not, a default graphic is shown. Each div also displays the poem’s title (as a

link to the poem’s individual page) and the poet’s name (as a link to the user’s

profile page). The poem’s text is displayed with the “safe” tag, which allows the

output from the rich text editor to be displayed correctly. If a user is logged in,

the like/unlike buttons are displayed, along with the current number of likes

the poem has.

If the current user is in the list of users who have liked the poem, the page

shows the unlike button and hides the like button. If the user has not liked the

poem, the unlike button is hidden and the like button is shown.

If the poem displayed was posted by the current user, the delete button is

displayed.



<a name="br5"></a> 

Pagination:

The poems are paginated in groups of 8 posts. I implemented this using

[Django’s](https://docs.djangoproject.com/en/4.0/topics/pagination/)[ ](https://docs.djangoproject.com/en/4.0/topics/pagination/)[pagination](https://docs.djangoproject.com/en/4.0/topics/pagination/)[ ](https://docs.djangoproject.com/en/4.0/topics/pagination/)[class.](https://docs.djangoproject.com/en/4.0/topics/pagination/)

likes.html: Displays the poems a user has liked.

poem\_page.html: Displays an individual poem. On this page, if a user is logged in, a

form to post a comment is displayed. In the comment\_section div, using a for loop,

the comments are displayed along with the user’s profile picture and name.

poets.html: Lists the poets that are registered on the site (their username, profile

picture, first name, and last name). Each link references to the user’s profile page.

Uses a for loop to iterate through the users in the database. The page is paginated by

groups of 20.

post\_poem.html: Displays the rich text editor for a user to post their poem.

profile.html: Displays the user’s profile picture, username, name, and the poems they

have posted. This page also provides a form to write a “status” message.

**Models.py**

Contains four models: User, Poem, Comment, and Status.

Poem model:

• body field, uses [RichTextField](https://django-ckeditor.readthedocs.io/en/latest/)[ ](https://django-ckeditor.readthedocs.io/en/latest/)[field](https://django-ckeditor.readthedocs.io/en/latest/)[ ](https://django-ckeditor.readthedocs.io/en/latest/)[type](https://django-ckeditor.readthedocs.io/en/latest/)[ ](https://django-ckeditor.readthedocs.io/en/latest/)from Ckeditor.

• Referencing the timestamp of the post, poems are ordered in reverse, with the

most recent posts first.

**Admin.py**

o Registers the Poem, Comment, and Status models



<a name="br6"></a> 

**Forms.py**

o Contains the model forms for posting a poem, writing a comment, and writing

a status message.

**Urls.py**

o Contains the URL patterns for the website.

**Views.py**

Functions:

index:

▪ Using pagination, provides all the poems in the database to

index.html.

▪ Renders the homepage.

post poem:

▪ Renders the page with a form to post a poem.

▪ If the user submits a post:

• Processes the form submission, saving the posted poem

and its author in the database.

• Redirects back to the homepage.

poem\_page:

▪ Renders a page displaying an individual poem

• The poem IDs are passed in from the URL templates tags.

▪ Provides the poem, the poem’s comments, and the comment

form as context

▪ If a comment is submitted:

• The comment, the poem commented on, and the

commenter are saved to the Comment model.

• The view redirects to the poem’s page.



<a name="br7"></a> 

like\_poem:

▪ Adds a like on a poem for a current user.

▪ Provides the current number of likes on the poem using

JsonResponse — used in poetica.js to update the count.

unlike\_poem:

▪ Removes the like on a poem from the user.

▪ Provides the current number of likes on the poem using

JsonResponse — used in poetica.js to update the count.

delete\_poem:

▪ When delete button is submitted, the poem is deleted from the

model.

▪ Redirects to the homepage

\* This feature could use some work — when a post is

deleted, the page will redirect from the current page back to

the index page. If I had more time, I would have liked to use

JS to hide the post, and remain on the same page.

poets:

▪ Renders the page displaying the list of poets registered on the

site.

▪ Using pagination, provides this list of users as context to

poets.html.

liked\_poems:

▪ Renders likes.html

▪ Using pagination, provides the poems liked by the current user as

context.



<a name="br8"></a> 

profile:

▪ Renders the profile page

• The poet’s ID is passed in from the URL templates tags.

▪ Provides the poems written by the current user to the profile page

as well as the form to update the user’s status.

▪ If a status message is submitted

• Saves status and the current user in the Status table.

• Redirects back to the profile page.

▪ If the user hasn’t posted any status messages, a default message is

provided to the profile page.

▪ Otherwise, the most recent status message is provided as context.

