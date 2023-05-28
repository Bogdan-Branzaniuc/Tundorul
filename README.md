# Tundorul

## Game Streamer  

[view Live Site Here](https://tundorul.herokuapp.com/suggestions)

A website designed to enhance the streaming gaming and viewing experience for Tundorul.tv.
A romanian Streamer that plays games on "ungodly levels of difficulty".

"Once we know a game is a good vibe, we treat it with the utmost respect, 
meaning we don't skip any cinematic /lore /loot /collectible /trophy /achievement. 
In for a penny, in for a pound."


The business goals for this website are:
* Keeping in touch with the community
* Setting grounds for future projects
* Providing a space where feedback could be voted by the community

The customer goals of this website are:
* The Ability to keep in touch and follow the streamer's next steps
* The Possibility to see livestreams directly from this website
* The ability to see the past 10 streams in chronological order
* The ability to write suggestions that once approved can be up voted by community members


#### The Ideal Client
* Is already a Tundorul channel follower on twitch.
* Loves a good vibe and games.
* Acts within the community Rules.


# User Stories



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