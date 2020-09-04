# Welcome to Vroom-!    :car:



# What is Vroom?
Vroom is a peer to peer car selling website. Users are able to browse and search for cars at the touch of their fingertips.
Please visit the live site [here](https://lzx1vroom.herokuapp.com/) 

### For test users, please use the following account:
- Email: **test@test.com**
- Password: **12345678!**
##### Add in any image by going to Google.com/images and right clicking to copy a image URL.


# UI/UX


## Strategy
### Owner stories:

- As the owner, I want to attract both seller and buyers onto my platform so that I can build a car buying ecosystem.

- As the owner, I will make transactions on the website free so that more users will use my platform to transact their cars so that I can attract car 
dealerships and individuals to advertise on my website.

- As the owner, I want to create a friendly and well laid out website so that clients will spend more time browsing on my website.

- As the owner, I want to help sellers collate all of their orders into their own shop page to forge identity and entice buyers with a greater array of selections
from the same trusted seller.

### User-seller:

- As the seller, I want to reach a large number of audiences so that my car has the best chance to be sold.

- As the seller, I want a website that has minimal fees or no fees so that I can maximise my profit margins.

- As the seller, I want to create a e-commerce shop so that the buyer can easily view all of my cars and be intrigued by my other listings as well.

### User-buyer:

- As the buyer, I do not want to go through the hassle of signing up before I can buy a car.

- As the buyer, I want to browse a large selection of cars so that I will have the most information before I make a purchase

- As the buyer, I want to be able to search for the cars I want using different search functions to narrow down my search so that I can find the
car I am looking for.

- As the buyer, I want to find out all the cars from a trusted seller so that I can recommend them to my friends or browse for other cars that may interest me.


## Scope

### Current Features

- Register
- Login
- Logout
- Search by seller name, car brand, car model and new/used cars.
- Create listings
- Update listings
- Delete listings
- User's personalised store

### Features to be implemented

- Login/Register with social media sites
- Filter search results and sort by price or date listed
- Wishlist for users to add in sortlisted listings

## Skeleton

Wireframes can be found [here](https://github.com/liuzhenxin2/vroom-/blob/master/vroom.pdf)


## Surface

As this is a car buying/selling website, 
- I chose to stick with the default font because my audience, being predominantly male, would appreciate fonts that are straightforward and easy to read. 
- I have also chosen bold colors such as red (redline in cars) blue (electric and ecofriendly car) and black (petrol and exhaust).


# Technologies used

- HTML
- CSS
- Javascript
- [JQuery](https://jquery.com/) to simplify DOM manipulation
- [Bootstrap version 4.5](https://getbootstrap.com/docs/4.5/getting-started/introduction/) for flex boxes, color schemes and navbar
- [MongoDB Atlas](mongodb.com) for storing data on database
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) to route and display webpages
- [Flask-Login](https://flask-login.readthedocs.io/en/latest/) for user authentications
- [pymongo](https://pymongo.readthedocs.io/en/stable/) to communicate with MongoDB in Python
- [GitHub](https://github.com/) for version control
- [toastr](https://github.com/CodeSeven/toastr) for displaying messages

# Database design

I used both reference and embeded documents for my database design.
- My complete ER Diagram can be found [here](https://github.com/liuzhenxin2/vroom-/blob/master/Vroom%20ERD.pdf)
- A sample mongoDB document can be found [here](https://github.com/liuzhenxin2/vroom-/blob/master/Vroom%20sample%20mongo%20doc.png)

# Testing

A detailed testing file can be found [here](https://github.com/liuzhenxin2/vroom-/blob/master/Vroom%20testing.pdf)

### Bugs

- Footer css stylings cant seem to be pushed to heroku
- Background image(expect index page) cant seem to be 0.5 opacity

# Deployment

This website is deployed on Heroku. The URL for the deployed website is https://lzx1vroom.herokuapp.com/

To deploy on Heroku:

1. Clone the master branch from github
2. To list all the requirements in requirements.txt, run the following command in terminal:
``` 
pip3 freeze --local > requirements.txt 
```
3. Set Debug to False
4. Procfile need to be created to run gunicorn upon deployment
5. Git push to Heroku Master after all the documents ready
6. Add public keys and private keys for the following to Heroku Config Vars settings:
 - MongoDB URI
 - SECRET KEY

# File Hierarchy and Organisation

- **Static** folder contains pictures and styles which contains pictures and css files respectively 
- **templates** folder contains all html templates with jinja codes to render the display of the information from the database

# Credits

- Google and Unsplash for images



































