 
  # JU Eats



![Ju_Eats-removebg-preview](https://user-images.githubusercontent.com/88835836/134530227-89867115-7cca-4ad6-bb12-4140a4d1bcd7.png)



<h2> Hungry? You're at the right place.  </h2>

<h1 align="center"> OPEN JU Eats, TRACK FOOD, ORDER IT. </h1>

[![forthebadge](https://forthebadge.com/images/badges/built-by-developers.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/for-you.svg)](https://forthebadge.com)

 ## We have deployed our website at [Click here](https://arghyadeepsengupta.pythonanywhere.com/)<br>
 ## Want to clone it in your local machine? Click here ➡ [Steps to follow ](#Stepstofollow)
 
 ## Video Demonstration 
 https://user-images.githubusercontent.com/84338935/125182981-43478400-e230-11eb-9c5d-1bcb564b56e0.mp4

 ## Youtube link for the same [Click here](https://youtu.be/hEeJh9MAtz8) <br>
 
<h2 align="center" id="content"> 🗂 CONTENTS : </h2>

```diff
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
```

> `📌` [HacknPitch | JU E-Cell Hackathon](#HacknPitch)<br>
>> `📌` [Description](#Inspiration)<br>
>>> `📌` [Tech Stacks (we used)](#TechStack)<br>
>>>> `📌` [Features](#Features)<br>
>>>>> `📌` [How to get started](#Howtogetstarted?)<br>
>>>>>> `📌` [Steps to follow ](#Stepstofollow)<br>
>>>>>>> `📌` [Developed By](#DevelopedBy)<br>
>>>>>>>> `📌` [ScreenShots](#ScreenShots)<br>
>>>>>>>>> `📌` [Thank you note](#TimetoSayGoodBye)<br>
```diff
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
```

<br>

<h2 align="center" id="HacknPitch"> :trophy: HacknPitch | JU E-Cell Hackathon</h2>

<h2 align="center" id="Inspiration"> :label: Description</h2>

JU Eats **integrates all campus canteens on one web application**. It does so by showing food menu, providing the feature to track live canteen food, taking real-time orders & furthermore providing schedule for later option. The idea was generated during **HacknPitch Hackathon by JU E-Cell**. <br>
Whether you are hungry or not, a glimpse at JU Eats webapp will definitely make you hungry in a jiffy. <br> <br>
**#EatWhatMakesYouHappy**

<i><p align="center"><a href="#content">⬆️ CLICK HERE TO GO BACK TO CONTENTS</a></p></i><br>

<br>

<h2 align="center" id="TechStack"> :label: Tech Stack

```diff
+ HTML +
+ CSS +
+ JAVASCRIPT +
+ REACT.JS +
+ DJANGO +
+ PYTHON +
+ PayPal API +

```

</h2>

<i><p align="center"><a href="#content">⬆️ CLICK HERE TO GO BACK TO CONTENTS</a></p></i><br>

<br>

<h2 align="center" id="Features"> :label: Features</h2>

  #### Main Features
  
   :point_right: JU Eats can track the availability of the food in JU Canteens <br/>
   :point_right: Order can be placed realtime or can be scheduled <br/>
   


   #### Future Features
  
   :point_right: Will add delivery feature so that people outside JU Campus can have their tasty food at their doorsteps.<br/>
   :point_right: Will intergrate all the JU Canteens (JU Eats now mainly focused on 4 of them).<br/>
   

![WORLFLOW (1)](https://user-images.githubusercontent.com/84338935/134521790-e027b083-64a7-400b-a698-5390d7113620.png)


<i><p align="center"><a href="#content">⬆️ CLICK HERE TO GO BACK TO CONTENTS</a></p></i><br>

<br>

<h2 align="center" id="Howtogetstarted?"> ⭐ How to get started?</h2>

You can refer to the following articles on the basics of Git and Github and also contact the Project Mentors, in case you are stuck:

- [Watch this video to get started, if you have no clue about open source](https://www.youtube.com/watch?v=yzeVMecydCE&ab_channel=freeCodeCamp.org)
- [Installing an apk](https://www.javatpoint.com/how-to-install-apk-on-android)
- [Cloning a Repo](https://help.github.com/en/desktop/contributing-to-projects/creating-a-pull-request)
- [How to create a Pull Request](https://opensource.com/article/19/7/create-pull-request-github)
- [Getting started with Git and GitHub](https://towardsdatascience.com/getting-started-with-git-and-github-6fcd0f2d4ac6)

<i><p align="center"><a href="#content">⬆️ CLICK HERE TO GO BACK TO CONTENTS</a></p></i><br>


<h2 align="center" id="Stepstofollow"> ⭐ Steps that are to be followed :scroll:</h2>

<br>


### 1️⃣ Clone it :busts_in_silhouette:

You need to clone (download) it to local machine using

```sh
$ git clone https://github.com/pappan-123/JU-Eats.git
```

> This makes a local copy of repository in your machine.

Once you have cloned the `JU-Eats` repository in Github, move to that folder first using change directory command on linux and Mac.

```sh
# This will change directory to a folder  
$ cd JU-Eats
```

Move to this folder for all other commands.

<br>



### 2️⃣ Set it up :arrow_up:

You'll need the following dependencies : <br/>

Pycharm Install <a href="https://www.jetbrains.com/pycharm/download/">here</a> <br/>
**or** <br>
VS-Code install <a href="https://code.visualstudio.com/download">here</a> <br/>

Installing Django
```sh
 $ python -m pip install Django
```
## comment for install dependencies
<br>

pip install django-allauth <br>
pip install django-crispy-forms

## comment for change Django-Admin Portal
pip install -U django-jazzmin<br>
Add 'jazzmin', to INSTALLED_APPS<br>
INSTALLED_APPS = [
    'jazzmin',<br>
    'django.contrib.admin',
    [...]
]
<br>



### 3️⃣ Sync it :recycle:

Always keep your local copy of repository updated with the original repository.
Before making any changes and/or in an appropriate interval, run the following commands *carefully* to update your local repository.

```sh
# Fetch all remote repositories and delete any deleted remote branches
$ git fetch --all --prune

# Switch to `master` branch
$ git checkout master

# Reset local `master` branch to match `upstream` repository's `master` branch
$ git reset --hard upstream/master

# Push changes to your forked `covisite` repo
$ git push origin master
```

<br>



### 4️⃣ Ready Steady Go... :turtle: :rabbit2:

Once you have completed these steps, you are ready to start contributing by checking our `Help Wanted` Issues and creating

<br>

### 5️⃣ Create a new branch :bangbang:

Whenever you are going to make contribution. Please create seperate branch using command and keep your `master` branch clean (i.e. synced with remote branch).

```sh
# It will create a new branch with name Branch_Name and switch to branch Folder_Name
$ git checkout -b Folder_Name
```

Create a seperate branch for contibution and try to use same name of branch as of folder.

To switch to desired branch

```sh
# To switch from one folder to other
$ git checkout Folder_Name
```

To add the changes to the branch. Use

```sh
# To add all files to branch Folder_Name
$ git add .


```sh
# This message get associated with all files you have changed
$ git commit -m 'relevant message'
```

<br>


### 6️⃣ Share your work :star_struck:

Now, Push your awesome work to your remote repository using

```sh
# To push your work to your remote repository
$ git push -u origin Folder_Name
```

Then, go to your repository in browser and click on `compare and pull requests`.
Then add a title and description to your pull request that explains your precious effort.

<i><p align="center"><a href="#content">⬆️ CLICK HERE TO GO BACK TO CONTENTS</a></p></i><br>

<h2 align="center" id="DevelopedBy"> :label: Developed By</h2>
    
   :arrow_right: [Souvik Choudhury](https://github.com/SouvikChoudhury360)
      (JU MECHANICAL 2nd Year)
   <br>
   :arrow_right: [Arghyadip Sengupta](https://github.com/arghya1912)
      (JU ETCE 2nd Year)
      <br>
    :arrow_right: [Saptadeep Sen](https://github.com/Saptadeep717)
      (JU ETCE 2nd Year)
   <br>
   :arrow_right: [Arkapravo Saha](https://github.com/pappan-123)
      (JU ETCE 2nd Year)
   <br>
   :arrow_right: [Soham Maji](https://github.com/mafiariders7)
      (JU ETCE 2nd Year)
   <br>



<i><p align="center"><a href="#content">⬆️ CLICK HERE TO GO BACK TO CONTENTS</a></p></i><br>

<h2 align="center" id="ScreenShots"> :label: ScreenShots</h2>

|||
|---|---|





![IMG_20210924_140932](https://user-images.githubusercontent.com/84338935/134647836-87cce6b6-a325-404d-bdf9-b57599f14e10.jpg)

![IMG_20210924_141021](https://user-images.githubusercontent.com/84338935/134647761-3bc29195-32dd-4920-a60b-e08924d59a10.jpg)

![IMG_20210924_141044](https://user-images.githubusercontent.com/84338935/134647723-bbed0601-7d04-4ef4-b36c-2e451f8cb98e.jpg)










![IMG_20210924_141206](https://user-images.githubusercontent.com/84338935/134647505-b7156d08-b926-4bd1-ae07-e11f12925808.jpg)

![IMG_20210924_141129](https://user-images.githubusercontent.com/84338935/134647675-fd5bff58-dc0f-42e4-8f01-3f86f1ba77d1.jpg)



<!--|<h3 align="center">Home Page</h3><img width="200" alt="Home Page" src="https://drive.google.com/file/d/1L1n96VT44BJGh9bBQKP8rtKDJ5pkIIZC/view?usp=sharing">-->

<i><p align="center"><a href="#content">⬆️ CLICK HERE TO GO BACK TO CONTENTS</a></p></i><br>


<h2 align="center" id="TimetoSayGoodBye"> :label: Phew! It's time to say Good Bye! :smile: </h2>
    
   Thank You for giving us a chance! Wishing You a Good Day ahead.



<i><p align="center"><a href="#content">⬆️ CLICK HERE TO GO BACK TO CONTENTS</a></p></i><br>
