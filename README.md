# Tundorul

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
![image with displays](https://res-console.cloudinary.com/dgzv7gan8/thumbnails/v1/image/upload/v1685357777/ZGlzcGxheXNfcHJqc2Zx/preview)
* web large
* web medium
* web small
* tablet
* Surface Duo
* Iphone 12 Portrait
* Iphone 12 landscape


## Features


## Left to implement



III Models
UserProfile
Vods
Suggestions
   - red-cases: 1 unique title + message.
                2 required fields.
                3 suggestion body too short  field min char. 

IV Views


V APIS
1. Twitch API
    - /// 
2. Appscheduler
    - the appscheduller makes a call to twitch API every 6 hours to retrieve the last version of the Icalendar then updates the static file twitchdev.ics.
    - BUG: it runs twice every time, fixed the vods by filtering for duplicates in vods.py view

VI Libraries
1. Gsap
2. Allauth


VII Mechanics
1. homepage countdown till the next stream


VIII Testing
   


IXDeployment



X End