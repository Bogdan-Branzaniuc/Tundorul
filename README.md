I Introduction



II Epics and User Stories



III Models
UserProfile
Vods
Suggestions


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