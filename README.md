# Tundorul
<img src="https://res.cloudinary.com/djnxh7xga/image/upload/v1684923696/logo_default_ibawlh.svg" alt="Tundorul Logo" style="width: 100px; height: 100px;">

# Game Streamer  

* [view Live Site Here](https://tundorul.herokuapp.com/suggestions)
* [view Twitch Channel Here](https://www.twitch.tv/tundorul)

A website designed to enhance the streaming gaming and viewing experience for Tundorul.tv.
A romanian Streamer that plays games on "ungodly levels of difficulty".

"Once we know a game is a good vibe, we treat it with the utmost respect, 
meaning we don't skip any cinematic /lore /loot /collectible /trophy /achievement. 
In for a penny, in for a pound."


### The business goals for this website are:
* Keeping in touch with the community
* Setting grounds for future projects
* Providing a space where feedback could be voted by the community

### The customer goals of this website are:
* The Ability to keep in touch and follow the streamer's next steps
* The Possibility to see livestreams directly from this website
* The ability to see the past 10 streams in chronological order
* The ability to write suggestions that once approved can be up voted by community members


### The Ideal Client
* Is already a Tundorul channel follower on twitch.
* Loves a good vibe and games.
* Acts within the community Rules.
* Possibly subscribed to the Channel, but not mandatory
* Treats every game with respect to the developers

### User Stories
* As a User I want to be able to create a suggestion so I can help the comunity with my input
* As a USER I want to be able to **SEE my non-approved suggestions** so I can **edit or delete them without waiting for them to be approved first**
* As a USER I want to be able to Edit a suggestion if I want to add something to it or fix typo's
* As a USER I want to be able to delete my suggestion so I can remove it if I changed my mind
* As a USER I want to be able to Upvote Another user suggestion if I like it and want it implemented in future streams or website Architecture

### Moderator Stories
* As an **Admin** I want to be able to see and filter suggestions like a user, but including the non-approved suggestions
* As an **Admin** I want to have a live-countdown in the home page to the next stream so my users can clearly see the time left to the closest stream
* As and **Admin** I want to be able to retrieve my Stream Schedule from Twitch so I can display it into the Home Page
* As an **Admin** I want to have an embeded Iframe with my Live or Offline status where my viewers can see me live directly from my website
* As an **Admin** I want to be able to ban a user on my website so I can mentain a positive environment 
* As an **Admin** I want to be able to unban users so I can give them another chance or fix a mistake when banning the wrong user
* As an **Admin** I want to be able to Display the user an error page when reaching a wrong url or display a Banned Page if the user was banned 
or a "you have to log in" page for suggestions and profile pages

</br></br></br></br>

# Display and Layout across devices:
![image with Layouts across devices](https://res.cloudinary.com/dgzv7gan8/image/upload/v1685357777/displays_prjsfq.png)
* web large
* web medium
* web small
* tablet
* Surface Duo
* Iphone 12 Portrait
* Iphone 12 landscape

</br></br></br>

# Features

### Nav Bar
![navbar versions image](https://res.cloudinary.com/dgzv7gan8/image/upload/v1685360930/navbar_vqche2.png)
there are 3 states :
* if Logged in as a normal User,
* if Logged out,
* if Logged in as an Admin,
* all three states respect the collapsible feature from Bootstrap.

### Home Page
* ### Welcome section
![welcome-section image](https://res.cloudinary.com/dgzv7gan8/image/upload/v1685363582/home-welcome_sphhjg.png)
* A welcome message an an Iframe that is linked to Tundorul's live on Twitch showing Offline while there's no live stream
* ### Schedule section   
![schedule-section image](https://res.cloudinary.com/dgzv7gan8/image/upload/v1685363521/home-schedule_yaaemt.png)
* This schedule is retrieved from Twitch and stored in an .ics file which then is rendered in html
* there is a JS file that builds the countdown timer and updates the clock every second
* The website updates the Schedule every 6 hours to determine if any changes were made in the Original Schedule on Twitch
* ** /// BUG ALERT //// ** 
* The Js file is not yet configured to take into acount the user's current time if they are in a different timezone than the App's server. 
* There also seems to be a little counting issue in the code since there is 60 minutes and 23 seconds left, instead of 4 hours and 23 seconds. 
* ### Rules section
![rules-section image](https://res.cloudinary.com/dgzv7gan8/image/upload/v1685363521/home-rules_lxwx2g.png)


### Vods Page
![vods Page image](https://res.cloudinary.com/dgzv7gan8/image/upload/v1685363739/vods_Page_czswao.png)
* The last 10 Vods are getting updated every 6 hours in the website Database


### Profile Page 
![profile Page image](https://res.cloudinary.com/dgzv7gan8/image/upload/v1685364752/profile_ltkkcj.png)
* If the user is logged in with his twitch account, he can see his profile image on twitch along with his twitch data
* If the user isn't logged in yet, a message is rendered telling the user the page is available only when logged in with a twitch account
* In the end of the page there is an animation and a message saying "more to follow", since this page is currently static, in the future it will hold Crud Functionality for the UserProfile Model as well as other related models. 


### Suggestions Page
![suggestions page image](https://res.cloudinary.com/dgzv7gan8/image/upload/v1685365906/suggestions_page_nyrzlt.png)
![suggestions mechanism image](https://res.cloudinary.com/dgzv7gan8/image/upload/v1685365804/suggestions_clwz4y.png)
* On This Page Django Unicorn was used to send Ajax requests to the backend, meaning everything that happens on this page is instantly rendered without full page reloading 
* users can only write or see suggestions if they are logged in, otherwise they will be showed a message telling them to Log in with their twitch account
* Once a suggestion's form is submitted, the suggestion goes into awaiting approval mode, The user can still edit or delete it at this point
* Once a suggestion is approved it can be up voted by it's author or any other user
* At this point the user can still edit or delete the suggestion, after submitting the edit form, if valid, the suggestion will go into approval mode again
![filters image](https://res.cloudinary.com/dgzv7gan8/image/upload/v1685366887/filters_ldkiza.png)
* There are 3 sets of filters:
  - All / Mine  
    * renders the list with all Approved Suggestions or just the current logged in User's suggestions.
  - Approved / Awaiting Approval   
    * If awaiting approval is on the All/Mine filter will get set on Mine automatically.
    ![filters-wireframe image](https://res.cloudinary.com/dgzv7gan8/image/upload/v1685369630/filters-miniwireframe_pfyzrc.png)
  - By votes / by date 
    * this filter works the same at all times



### /// Important Feature left outside this version /// ###
A user will be allowed a limit of suggestions per week for future spam preventions

### Log in 
![sing in image](https://res.cloudinary.com/dgzv7gan8/image/upload/v1685367865/sign_in_gmsrex.png)

### Log out
![sign out image](https://res.cloudinary.com/dgzv7gan8/image/upload/v1685367866/sign_out_q6gdpv.png)

### Awaiting Approval
![awaiting approval page image](https://res.cloudinary.com/dgzv7gan8/image/upload/v1685367866/awaiting_approval_page_lmwv0r.png)
* here the admin will approve sugestions that are either newly created or edited by the users 
### /// Important Feature left outside this version /// ###
A delete button will be displayed along with any suggestion

### Footer
![footer_image](https://res.cloudinary.com/dgzv7gan8/image/upload/v1685368482/footer_knmedl.png)
* Social Media Links

### Django Messages
![django_messages_image](https://res.cloudinary.com/dgzv7gan8/image/upload/v1685369870/django-messages_rmckiv.png)

### Left to implement
* Giveaway Application
* Spending Channel Points on the website
* Gsap Library for front end user experience [see my CV as example](https://bogdan-branzaniuc.github.io/CV/)
* Sorting Vods by View-count or by date (as default) 
* Suggestions Pagination

</br></br></br>

# Models
[See the models wireframe](https://www.figma.com/community/file/1245677960849513360/Bogdan-Branzaniuc)

</br></br></br>

# Parts And Applications
## tundorul App
- is responsible for all the views of the Website aside of suggestions view
- log in
- log out
- home.py
- user_profile.py
- user_profile_build.py
- vods.py
- banned_user.py
- handler_error_page.py
- models: UserProfile, Vods
## suggestion App
- in order to render suggestions page with Django Unicorn, suggestion app was created
- it is responsible for suggestion/components/suggestions.py view 
- model: Suggestions
## jobs Appscheduler Directory
- responsible for tasks that have to run once every n time [see Twitch Api](#twitch-api)
</br></br></br>
# Twitch API
## Scheduled Requests
* Appscheduler requests to twitch API
  - every 6 hours to retrieve the last version of the Icalendar then updates the static file twitchdev.ics.
  - every 6 hours to retrieve the last 10 vods and updates the Vods model
  - every 4704769 seconds to store the Application Token needed for twitch Api requests.
  ### ***Important Detail*** ###
    The Application Token is stored in the environment variable "APP_TOKEN" and refreshed after a given interval. The Twitch Response is also providing this 
    interval, but a hardcoded interval was used due to insufficient time to figure out how to store the interval without calling the API twice.
    This will be addressed in following versions. 
* Appscheduler is runed from jobs directory in root directory.

## Signal based Requests
  - in tundorul.views.user_profile_build I used the receiver @receiver(user_logged_in) to trigger a request that creates or updates the UserProfile instance of the user,
  - Thea method is_follower() checks if the user is a follower to Tundorul's Channel and if true updates join_date with the response 'followed on' data. 
  - This helps keeping user data updated every time they change something to their account, like, the name, email, profile immage

## Endpoints Used:

* [Get Followed Channels](https://dev.twitch.tv/docs/api/reference/#get-followed-channels)
* [Get Channel iCalendar](https://dev.twitch.tv/docs/api/reference/#get-channel-icalendar)
* [Get Videos](https://dev.twitch.tv/docs/api/reference/#get-videos)
* [App Access Token](https://dev.twitch.tv/docs/authentication/#app-access-tokens)
</br></br></br></br>
# Technologies
* Python and [pycharm](https://www.jetbrains.com/pycharm/) IDE
* [Twitch Api](https://dev.twitch.tv/docs/api/)
* [Django framework](https://www.djangoproject.com/)
* Django Libraries:
  * Django Allauth
  * Django Unicorn
  * Appscheduler
* Postgres [Elephant SQL]()  
* Heroku 
</br></br></br></br>
# Deployment
* If you are using Gitpod with Pycharm, run this command in order to be able to install requirements to Django
```
echo 'export PIP_USER=no' >> ~/.bashrc && export PIP_USER=no
```

* [Create a virtual env and install requirements.txt (stack overflow)](https://stackoverflow.com/questions/41427500/creating-a-virtualenv-with-preinstalled-packages-as-in-requirements-txt) 
```
pip install virtualenv          //(if you don't already have virtualenv installed)
virtualenv venv to create       //your new environment (called 'venv' here)
source venv/bin/activate        //to enter the virtual environment
pip install -r requirements.txt //to install the requirements in the current environment
```

  ## Log into your Cloudinary account
  create env.py file in your root directory </br></br>

  env.py
  ```
  import os

  os.environ["CLOUDINARY_URL"] = "your cloudinary url"
  ```
  </br>

  settings.py 
  ```
  STATIC_URL = '/static/'
  STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
  STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
  STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
  ```

  ## Create an ElephantSql Database
  * Log into your elephant Sql account 
  * click on ```Create New Instance``` 
  * Sellect ```Tiny Turtle(Free)``` 
  * from the main dashboard sellect your new instance</br></br>

  env.py
  ```
  os.environ["DATABASE_URL"] = "Elephant Sql Database Url"
  ``` 
  </br>

  settings.py
  ```
  DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
  }
  ```
  </br> </br>
  ## Create a Heroku Application
  * Log into your Heroku account
  * press ```New``` and ```create new app```
   </br> </br>

  ## Create your Twitch Application
  * go on [https://dev.twitch.tv/console](https://dev.twitch.tv/console) and create or log into your twitch account
  * Click on *Register Your Application*
  * Set Category to *Website Integration* and then click *create*

  * Go to your developer console and click *manage* on your newly created App
  * Set *OAuth Redirect URLs* to ```your_heroku_app_domain/accountstwitch/login/callback/``` it also supports localhost
  
  env.py
  ```
    os.environ["CLIENT_ID"] = "owh7ttfh3085i7jg6jzl04tcg64u54"  
  ```
  the client Id from twitch is public info </br>
  click on get secret in your Twitch manage-app dashboard
  ``` 
    os.environ["SECRET_KEY"] = "twitch app secret"
    os.environ["APP_TOKEN"] = ""    
  ```
  APP_TOKEN remains empty, Appscheduler will populate it  after 6 hours from deploiment

  * In your settings.py file
  ```
  INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'apscheduler',
    'tundorul',
    'suggestion',
    'django_unicorn',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.twitch',
    'cloudinary_storage',
    'cloudinary',
    'asyncio',
    'twitchAPI',
    'django_extensions',
]
  ACCOUNT_EMAIL_VERIFICATION = 'none'
  LOGIN_REDIRECT_URL = '/'
  LOGOUT_REDIRECT_URL = '/'
  SOCIALACCOUNT_STORE_TOKENS = True
  SOCIALACCOUNT_PROVIDERS = {
      'twitch': {
          'SCOPE': ['user_read', 'user:read:follows'],
          'AUTH_PARAMS': {'access_type': 'online'},
          'METHOD': 'oauth2',
      },
  }
  ```
  * In your project terminal

  ``` 
    python manage.py makemigrations
    python manage.py migrate
  ```

  * run your django Project with 
  ```
    python3 manage.py runserver
  ```
  * create a superuser with
  ```
    python manage.py createsuperuser
  ```
  * log into your django admin panel
  * Go to ```Sites``` Model
  * Edit the site that django generated to point to your heroku app url ex ```https://tundorul.herokuapp.com/```
  * click save

  * Go to SocialApplications model and create a new instance
    * Provider: ```Twitch```
    * Name: ```your heroku app, twitch app and this Social App would be great to have the same names for consistency reasons``` 
    * Client id: ``` your twitch App client id ```
    * Secret key: ``` your twitch App secret ```
    * Key: ``` blank ```
    * sites: ```select the site you created previously and click the arrow to move it to the right box```
  * click save

</br>

## Create a procfile
  * In your root directory create a file named ```Procfile``` </br>

Procfile
```
  web: gunicorn tundorul_django.wsgi
```
</br>

#  /////////// Make extra sure you have ```Debug = False``` in your settings.py \\\\\\\\\\\\\\\\\\\
## Setup Heroku App for deploiment
* Go on Heroku select your application and click ```settings```
* ```Reveal Config Vars```
* Fill in all the environment variables you have in env.py
* add ```PORT 8000```
* Go to ```Deploy```
* connect your github repository to heroku, sellect the branch and Hit ```deploy branch```
</br>
</br>
## Voilla! if everything went well the app is up and running.
</br></br></br>

# Notes file deleted:
![deleted notes file](https://res.cloudinary.com/dgzv7gan8/image/upload/v1685572071/deleted_notes_xr8bhp.png)

* this are two Twitch Accounts, 
  * the first one was deleted from twitch,
  * the second one has only a refference instead of it's true password. It's password was changed and the account testBogdan123 will be provided to the test Commision in my submission details. since it has both a SocialAccount linked to it and superuser and staff status on the website.   


# Testing
## UX & UI

* I used [BrowserStack](https://live.browserstack.com/dashboard#os=iOS&os_version=14.0&device_browser=safari&zoom_to_fit=true&full_screen=true&url=https%3A%2F%2F8000-bogdanbranzaniuc-cv-xsqhgnyysr5.ws-eu87.gitpod.io%2F%23about-me&speed=1) for testing the application across multiple browsers and devices within the limit of a free trial.

* Also Tested directly on my devices: 
* One+ 9 Pro Android Chrome
* Windows Desktop Brave, Chrome, Mozila, Opera

## Manual Testing
* all the features were manualy tested by me during development and by me, friends and family after development
 

## Database Testing
* The web app was developed with a Django default database
* Tested with the default database, migrate to a production Database, and tested again with the production Database

## Unit Tests
![coverage tests report](https://res.cloudinary.com/dgzv7gan8/image/upload/v1685522855/coverage_report_hosh5h.png)

In order to run the tests you need to go in settings.py and use Django default database. 

```
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': BASE_DIR / 'db.sqlite3',
   }
}
```
also make sure to start the virtual env
```
. my_env/bin/activate
```
and then run all tests with
```
python manage.py test 
```

 # //// Important /////
  * the ```suggestion app```, ```Appscheduler``` and ```other Twitch Api Calls``` were manually and carefully tested 
  * They were left outside the ```unitests``` Since the first is using Django Unicorn Library with Ajax calls and the later could end with a ban from twitch on my Twitch Application, which in fact happened once due to an error loop in Jobs directory that makes use of ```Appscheduler```.  
  * I waited for all the time intervals up to 5 times consecutively and checked the application's logs on heroku and everything was running smoothly.

# Validators



</br></br></br>

# Credits

## Django Developers 
## Django Allauth Library Developers
## Django Unicorn Library Developers
## Twitch Api Developers
## Bootstrap Developers
## Python, Js, Jquery creators
  * Without this people, my project's current state would have been far from reality in this amount of time.

## My Brother Tudor
  * He brought his own input to the project as the Website was designed for his work.

## Media 
  * The videos used on this website represent the intelectual property of Tundorul.
  * The Logo was made by ```Andrei Muresan``` 
    * [linkedin](https://www.linkedin.com/in/andrei-muresan-5328a8220/?originalSubdomain=fr) 
    * [website](https://andrei-muresan-portfolio.webnode.fr/) 
  
## Stack Overflow
  * I managed to overcome a lot of issues by just going on this amazing resource with a copy paste of my errors.

## Twitch Developers Discord
  * At one point I was encoutering a problem with Allauth library, specifficly with it's sociallogin configuration.
  * I went on the discord server in the Authentication chat at 4 AM and 3 people responded in 2 minutes. It was a great feeling regardless of the timezone of each person involved. They managed to give me the most accurate direction pointing to my configuration after quickly inspecting the library Code and declaring it functionall. </br>
  //////////////////// Cudos to this people \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

## Chat GPT
  * I used Chat GPT to navigate Django's main concepts, As a beginner I found it the quickest way to see how this Django's Lego pieces were coming together.
  * I learned to use this tool mainly for general and consistent concepts and documentations rather than specific libraries, since it's training consists of lying and deceiving about it's actual knowledge. 
  * Lesson I learned from Chat GPT : ```If you have to change your question, go elsewere for the most acurate response```
 
## Code Institute
  * For enforcing high standards of good practices on my project
  * For compacting and providing valuable information and know-how in their course

## Me
  * For designing the architecture of the website 
  * For creating a decent product that meets the requirements of both Code Institute and Tundorul's Business

# Acknowledgements
## My two mentors Reuben Ferante and Brian Macharia 
  * Reuben Helped me at the beggining with great examples, directions and best practices
  * Towards the end of the project Reuben stepped down from Code Institute. On this regard I am thanking him for the previous help and his work as a mentor in this time.   
  * Brian Helped me a lot towards the end of the project, knowing how to press the Turbo Button 

## My brother for trusting me with his brand and immage 
