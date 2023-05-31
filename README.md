# Tundorul
<img src="https://res.cloudinary.com/djnxh7xga/image/upload/v1684923696/logo_default_ibawlh.svg" alt="Tundorul Logo" style="width: 100px; height: 100px;">

## Game Streamer  

* [view Live Site Here](https://tundorul.herokuapp.com/suggestions)
* [view Twitch Channel Here](https://www.twitch.tv/tundorul)

A website designed to enhance the streaming gaming and viewing experience for Tundorul.tv.
A romanian Streamer that plays games on "ungodly levels of difficulty".

"Once we know a game is a good vibe, we treat it with the utmost respect, 
meaning we don't skip any cinematic /lore /loot /collectible /trophy /achievement. 
In for a penny, in for a pound."


#### The business goals for this website are:
* Keeping in touch with the community
* Setting grounds for future projects
* Providing a space where feedback could be voted by the community

#### The customer goals of this website are:
* The Ability to keep in touch and follow the streamer's next steps
* The Possibility to see livestreams directly from this website
* The ability to see the past 10 streams in chronological order
* The ability to write suggestions that once approved can be up voted by community members


#### The Ideal Client
* Is already a Tundorul channel follower on twitch.
* Loves a good vibe and games.
* Acts within the community Rules.
* Possibly subscribed to the Channel, but not mandatory
* Treats every game with respect to the developers

#### User Stories
* As a User I want to be able to create a suggestion so I can help the comunity with my input
* As a USER I want to be able to **SEE my non-approved suggestions** so I can **edit or delete them without waiting for them to be approved first**
* As a USER I want to be able to Edit a suggestion if I want to add something to it or fix typo's
* As a USER I want to be able to delete my suggestion so I can remove it if I changed my mind
* As a USER I want to be able to Upvote Another user suggestion if I like it and want it implemented in future streams or website Architecture

#### Moderator Stories
* As an **Admin** I want to be able to see and filter suggestions like a user, but including the non-approved suggestions
* As an **Admin** I want to have a live-countdown in the home page to the next stream so my users can clearly see the time left to the closest stream
* As and **Admin** I want to be able to retrieve my Stream Schedule from Twitch so I can display it into the Home Page
* As an **Admin** I want to have an embeded Iframe with my Live or Offline status where my viewers can see me live directly from my website
* As an **Admin** I want to be able to ban a user on my website so I can mentain a positive environment 
* As an **Admin** I want to be able to unban users so I can give them another chance or fix a mistake when banning the wrong user
* As an **Admin** I want to be able to Display the user an error page when reaching a wrong url or display a Banned Page if the user was banned 
or a "you have to log in" page for suggestions and profile pages


## Display and Layout across devices:
![image with Layouts across devices](https://res.cloudinary.com/dgzv7gan8/image/upload/v1685357777/displays_prjsfq.png)
* web large
* web medium
* web small
* tablet
* Surface Duo
* Iphone 12 Portrait
* Iphone 12 landscape

## Features

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
* A welcome message and an Iframe that is linked to Tundorul's live on Twitch showing Offline while there's no live stream
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


# Models
[See the models wireframe](https://www.figma.com/community/file/1245677960849513360/Bogdan-Branzaniuc)
<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FHhIMKlJfVKrVmcr996Rcfa%2FUntitled%3Ftype%3Dwhiteboard%26node-id%3D0%253A1%26t%3DN877HhRN5DFHiUEq-1" allowfullscreen></iframe>

# Twitch API
## Scheduled Requests
* Appscheduler requests to twitch API
  - every 6 hours to retrieve the last version of the Icalendar then updates the static file twitchdev.ics.
  - every 6 hours to retrieve the last 10 vods and updates the Vods model
  - every 4704769 seconds to store the Application Token needed for twitch Api requests.
  ### ***Important Detail*** ###
    The Application. b Token is stored in the environment variable "APP_TOKEN" and refreshed after a given interval. The Twitch Response is also providing this 
    interval, but a hardcoded interval was used due to insufficient time to figure out how to store the interval without calling the API twice.
    This will be addressed in following versions. 
* Appscheduler is runed from jobs directory in root directory.

## Signal based Requests
  - in tundorul.views.user_profile_build I used the receiver @receiver(user_logged_in) to trigger a request that creates or updates the UserProfile instance of the user,
  - Thea method is_follower() checks if the user is a follower to Tundorul's Channel and if true updates join_date with the response 'followed on' data. 
  - This helps keeping user data updated every time they change something to their account, like, the name, email, profile immage

## Endpoints Used:
[Get Followed Channels](https://dev.twitch.tv/docs/api/reference/#get-followed-channels)
[Get Channel iCalendar](https://dev.twitch.tv/docs/api/reference/#get-channel-icalendar)
[Get Videos](https://dev.twitch.tv/docs/api/reference/#get-videos)
[App Access Token](https://dev.twitch.tv/docs/authentication/#app-access-tokens)

VI Libraries
2. Allauth social login
3. Django_Unicorn


# Deployment


# Testing
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


X End