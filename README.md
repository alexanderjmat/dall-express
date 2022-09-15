# The DALL-Express Gallery of Art

Repository URL: https://github.com/alexanderjmat/dall-express

## Purpose

The DALL-Express Gallery of Art (·DEGA·) is the very first online art gallery dedicated to displaying and selling pieces created by DALL·E 2, OpenAI's natural language to image generation program. The website functions primarily to display and sell digital artwork, although this release is a demo and does not integrate E-commerce features.

## Features

## User Flow

The homepage of the website immediately captures the eye with a field of floating art pieces right under the navigation bar. Users can click these moving pictures and be directed to their respective pages in the marketplace. At the bottom of the homepage the user can scroll through all the newest artwork released on the site. Both of these features ensure that the user is immediately given plenty of interesting content upon visting the page.

There is a navigation bar at the top of the homepage displaying three primary options:

- About
- Marketplace
- Contact
  
The About page is very simple. It contains three paragraphs that discuss the purpose of ·DEGA·, explain what DALL·E 2 is, and start a conversation about AI-generated art.

The Marketplace is where users can view and (in the future) purchase artwork. Each piece in the marketplace is given a nice border that looks like a frame, and users can click on the pieces to see a page that provies more info, such as the name, prompt, and price, of the artwork. Each piece of art has the option to be purchased as a poster, canvas, or Ultra-HD image. Users can add and remove items from a cart if they have an account, but this is a mere aesthetic display for now, since the pieces cannot be purchased yet.

The Contact page contains a form where users can send a message to the Gallery. In the future, the message data will be sent to an official ·DEGA· email address, but for now it is simply there for display and the data is not sent anywhere.

The primary navigation bar also contains links to signup and login at the top-right, allowing users to easily create and use accounts. When a user is in the session, the login link is replaced with a link to their own profile, which is an extremely simple page that will track their orders and account information.

## Technology Stack

This website was built primarily using Flask, JavaScript, HTML/CSS, SQLAlchemy, and Python.

