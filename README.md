# Oodles of Comfort

<img src="./documentation/amiresponsiveimage.PNG">

## Overview

Oodles of Comfort is a blog which is home to many tasty ramen recipes. Users can browse a huge range of recipes to find the perfect one for them. They can also filter through the recipes should they need more specific recipes i.e vegan recipes.

As well as this users will be able to create an account and log in to the blog, this will allow them to like and add comments to their favourite recipes and create a user profile. 

## Contents

* User Experience
- [Design](#design)
    - [Wireframes](#wireframes)
    - [Site Styling](#site-styling)
    - [Database Design](#database-design)
- [Features](#feature)
* Testing
* Languages and Technologies
* Deployment
* Credits

## User Experience

## Design

### Wireframes

#### Desktop

<details><summary>Home</summary>
<img src="./documentation/wireframes/homepage-desktop.png">
</details>

<details><summary>Recipe List</summary>
<img src="./documentation/wireframes/ramenlistpage-desktop.png">
</details>

<details><summary>Recipe Post</summary>
<img src="./documentation/wireframes/recipeview-desktop.png">
</details>

<details><summary>User Profile</summary>
<img src="./documentation/wireframes/userpage-desktop.png">
</details>

<details><summary>Sign In Design 1</summary>
<img src="./documentation/wireframes/signin1-desktop.png">
</details>

<details><summary>Sign In Design 2</summary>
<img src="./documentation/wireframes/signin2-desktop.png">
</details>

<details><summary>404 Page</summary>
<img src="./documentation/wireframes/404page-desktop.png">
</details>

#### Mobile

<details><summary>Home Page</summary>
<img src="./documentation/wireframes/HomePageMobile.png">
</details>

<details><summary>Recipe List</summary>
<img src="./documentation/wireframes/RecipeListMobile.png">
</details>

<details><summary>Recipe Post</summary>
<img src="./documentation/wireframes/RecipeDetailMobile.png">
</details>

<details><summary>User Profile</summary>
<img src="./documentation/wireframes/User Profile Page.png">
</details>

<details><summary>404</summary>
<img src="./documentation/wireframes/404Mobile.png">
</details>

### Site Styling

#### Colour Scheme

<img src="./documentation/colour_scheme/colour-scheme.PNG">

During the initial planning of the overall site design, I had gone with the above colour scheme as it I felt that it would like nice alongside the chosen images for my recipes however on adding the CSS to my index.html page the overall look was difficult to read. 

Due to this, I changed the colour scheme to more softer colours.

##### Final Colour Scheme 
<img src="./documentation/colour_scheme/final-colour-scheme.PNG">


#### Typography

##### Heading Font
<img src="./documentation/fonts/heading-fonts.PNG">

For the headings throughout the site I went with the font Madimi One. 

This font suits the overall minimal style of the site. 

##### Content Font
<img src="./documentation/fonts/content-font.PNG">

For the overall content of the site I decided to use the font Nunito, this font is quite similar to Madimi One and pairs with it quite well and is legible for the large amount of content with the recipes. 

### Database Design

#### ERD - Entity Relationship Diagram

### Models

#### Recipe Model

#### Recipe Tag Model

#### UserProfile Model

#### Comment Model

#### LikedRecipe Model

## Features

### Navbar

The navbar was created using Bootstrap 5 in order to ensure it would be responsive across various viewports. When a user is not signed in the navbar will display the following:

- Home
- Recipes
- Register
- Login

When the user is signed in the following is instead displayed:

- Home
- Recipes
- My Profile
- Sign Out

#### Desktop - Signed out

<img src="./documentation/features/navbar-desktop-signed-out.PNG">

#### Desktop - Signed in

<img src="./documentation/features/navbar-desktop.PNG">

#### Mobile non-expanded

<img src="./documentation/features/navbar-mobile1.PNG">

#### Mobile expanded

<img src="./documentation/features/navbar-mobile2.PNG">

### Footer

The footer for this site is used to contain links to various social media platforms. 

<img src="./documentation/features/footer.PNG">

### Home Page

For this site the home page is used to introduce the user to ramen, with a short blurb which emphasises the cosiness of a bowle of ramen and ties in with the name of the site. 

Under this there is a 'Recipes of the day' section, which displays 4 random recipes from the database to the user. This is changed on every refresh of the home page. 

<img src="./documentation/features/main-page1.PNG">

<img src="./documentation/features/main-page2.PNG">

### Recipes List Page

The recipe list page lets the user see all of the recipes that are available on site. From here they can also search for a particular recipe. 

<img src="./documentation/features/recipe-list-desktop.PNG">

### Recipe Search Page

When a user searches for a particular recipe it is presented to them on a separate page. 

<img src="./documentation/features/recipe-search.PNG">

### Recipe Details Page

On this page the user is presented with the name of the recipe, recipe image, ingredients and the necessary steps to create the dish. 

<img src="./documentation/features/recipe-detail1.PNG">

### Comments 

Users are able to comment on any of the recipes, once approved it will be displayed on the page. If a user is logged in and has posted to the page they will see the option to 'Edit' or 'Delete' their comment. 

<img src="./documentation/features/comments1.PNG">

<img src="./documentation/features/comments2.PNG">

### User Profile

Here the user can see a page which displays their username, when the account was created and a profile picture. 

<img src="./documentation/features/userprofile.PNG">

In future I would like to display recently liked recipes and a scrollable list of recent comments, further to this an option to upload a profile picture as it is currently only possible through the admin panel. 

### Sign Up

From here if the user does not have an account they may register their account. 

<img src="./documentation/features/signup.PNG">

### Sign In

For users that already have an account they can sign in here

<img src="./documentation/features/sign in.PNG">

### Sign Out

When the user wishes to sign out they are presented with a message to ensure they do want to sign out. 

<img src="./documentation/features/sign-out.PNG">

## Languages and Technologies

### Languages and Frameworks

Throughout the creation of this project the following languages and frameworks were used.

- HTML was used for the markup and templating. 
- Django as the web framework.
- Python was used for all backend work. 
- CSS was used to style the site.
- Bootstrap 5 was used throughout some elements for a responsive framekwork. 

### Packages

The following packages were installed throughout the development. 

| Package Name| Package Description |
| ----------- | ----------- |
| [crispy-bootsrap5](https://github.com/django-crispy-forms/crispy-bootstrap5)     |  This package was used to create a reusable DRY approach to forms.      |
| [Django-allAuth](https://docs.allauth.org/en/latest/)   | This package was used to provide templates, views and models necessary for user authentication.    |
| [Summernote](https://summernote.org/)   | Summernote was used to allow for a more creative approach when posting to the database through a custom model. Text fields can now have various font and layout styling added to them.         |
| [Whitenoise](https://pypi.org/project/whitenoise/)   | Whitenoise was used to allow the app to serve it's own static files which would be needed for deployment.        |

### Tools and Programs Used. 

- [GitPod](https://gitpod.io/workspaces) was used as the main IDE for the project. 
- [Git](https://git-scm.com/) was used for version control. 
- [GitHub](https://github.com/) for hosting my repository. 
- [Heroku](https://id.heroku.com/login) was used for deployment. 
- [Coolors](https://coolors.co/) was used for the colour palette. 
- [FontAwesome](https://fontawesome.com/) for providing all icons used throughout the site. 
- [Lucid](https://lucid.app/documents) for creating the database ERD. 
- [AmIResponsive](https://ui.dev/amiresponsive) for creating the README header image. 
- [Favicon.io](https://favicon.io/) for creating a favicon.
- [Balsamiq](https://balsamiq.com/) for creating the wireframes. 

## Testing

## Deployment

## Credits
