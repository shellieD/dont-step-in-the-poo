# DON'T STEP IN THE POOP

## Introduction

This project has been developed as part of the [Code Institute's](https://codeinstitute.net/) Diploma in Full-Stack Software Development.  The aim is to create a command line app that will demonstrate the skills I have learnt in python. 

This command line app is a fun little game of chance.  The aim of the game is not disimiliar to Battleships - where you guess co-ordinates in a grid to sink your opponents shits - however, in this game you need to guess co-ordinates to make a clear path across the 'garden' without stepping in a dog poo. 

## UX 

### Strategy Plane

#### Site Goal

* To provide the user with a fun and simple game of chance. 

### User Stories

* As a user I want to play a fun and simple game of chance. 
* As a user I want the purpose and the rules of the game to be apparent.

### Scope Plane

#### Features Planned

* 

### Structure Plane

* User Story: / Acceptance Criteria:

### Skeleton Plane

#### Wireframes?

#### Logic Flow

### Surface Plane

#### Design

#### Features 

* Welcome Screen
* Story and Rules
* Game board - Use of emojis
* Personalise with player name
* Option to Play
* Data Validation

### Future Development

### Testing

### Libraries Used

### Deployment

This app has been deployed via ![Heroku](https://www.heroku.com/) and the live link can be found here: PUT LINK HERE!!! 

The following steps were followed to deploy to Heroku:

1. Visit ![Heroku](https://www.heroku.com/) and log-in or create a new account.
2. Click the 'New' button.
3. Select the option to 'Create new app'.
4. Give the app a unique name.  Heroku will advise you if the name is available or not.  The unique name for this app is dont-step-in-the-poop.  Names should consist of only lower-case letters, numbers and dashes.
5. Select the appropriate region.
6. Click 'Create App'.  This will create your app in Heroku and take you to the app dashboard. 
7. Navigate to the settings tab and scroll down to 'Config vars'.  For KEY enter PORT and VALUE enter 8000.  Click the 'Add' button
8. Scroll down to 'Buildpacks' and click the 'Add Buildpack' button.  Firstly select 'python' and save changes.  Repeat, this time selecting 'node.js' and saving changes.  Make sure your buildpacks show in the correct order once selected, with Python being first in the list and node.js second.  If they are not in the correct order, you can drag and drop as required.
9. Use the menu at the top of the page to navigate to the 'Deploy' tab.
10. Select Github as the deployment method and then confirm you want to connect to Github by pressing the 'Connect to Github' button. 
11. Search for the Github Repository using the search field and click 'Search'. 
12. Click 'Connect' next to the correct Github repository. 
13. Once your repsitory is connected to Heroku, you can enable automatic deploys using the 'Enable Automatic Deploys' button or manually deploy  by selecting the branch to deploy following by the 'Deploy Branch' button. 
14.  If you choose to automatic deploys, Heroku will build a new version of the app whenever a change is pushed to Github.  Manually deploys allows you to update the app whenever you click the 'Deploy Branch'.   For this project I enabled automatic deploys to ensure the app was updated each time changes were pushed to Github.
15. When the build process is complete you will be able to view the live app by clicking the link 'Your app was successfullly deployed".
