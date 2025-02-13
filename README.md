# Little Explorers

Little Explorers is an e-commerce web application designed for customers looking to purchase high-quality children's clothing online.
🚨 **Disclaimer:** This is not a real store. The site is created for **learning purposes only** as part of a portfolio project.

This project is part of my portfolio, showcasing a full-featured online store with user authentication, product management, and secure payment integration.

Users can create accounts to manage their orders, while administrators have full write and delete access to all products and customer data.

You can also test the card payment functionality without making a real purchase. Use the following test card details:

**Card Number:** 4242 4242 4242 4242  
**Expiration Date:** Any future date  
**CVC:** Any 3-digit number  
**Postal Code:** Any 5-digit number  

You can view the deployed site [here](https://little-explorers-journey-34e4e4481594.herokuapp.com/).

![Mockup of live site on different devices](media\screenshots\main_page.PNG)

## Table of Contents

- [Little Explorers](#stepup)
  - [Project Overview](#project-overview)
    - [Agile Workflow](#agile-workflow)
  - [User Experience](#user-experience)
    - [Strategy](#strategy)
      - [Primary Goals](#primary-goals)
      - [Business Model](#business-model)
      - [Marketing](#marketing)
      - [Search Engine Optimisation](#search-engine-optimisation)
    - [Structure](#structure)
      - [Pages](#pages)
      - [Pages provided by Django](#pages-provided-by-django)
      - [Technical Design](#technical-design)
        - [Code Structure](#code-structure)
        - [Database](#database)
        - [Data Models](#data-models)
        - [Schema of models](#schema-of-models)
    - [Scope - Epics and User Stories](#scope-epics-and-user-stories)
      - [Epic 1: Base functionality and ease of use](#epic-1-base-functionality-and-ease-of-use)
      - [Epic 2: Products](#epic-2-products)hj
      - [Epic 3: The Cart](#epic-3-the-cart)
      - [Epic 4: Checkout](#epic-4-checkout)
      - [Epic 5: User registration and account](#epic-5--user-registration-and-account)
      - [Epic 6: The Wish List](#epic-6-the-wish-list)
      - [Epic 7: Reviews](#epic-7-reviews)
      - [Epic 8: Contact](#epic-8-contact)
      - [Epic 9: Site Owner functionality](#epic-9--site-owner-functionality)
      - [Epic 10: Terms and Policy](#epic-10--terms-and-policy)
    - [Skeleton](#skeleton)
      - [Wireframes](#wireframes)
    - [Surface](#surface)
      - [Colors](#colors)
      - [Design Choices](#design-choices)
      - [Typography](#typography)
  - [Existing Features](#existing-features)
    - [Feature 1: The Navbar](#feature-1-the-navbar)
    - [Feature 2: The Home Page](#feature-2-the-home-page)
    - [Feature 3: The Footer](#feature-3-the-footer)
    - [Feature 4: The Products List](#feature-4-the-products-list)
    - [Feature 5: The Product Detail Page](#feature-5--the-product-detail-page)
    - [Feature 6: The Cart](#feature-6-the-cart)
    - [Feature 7: The Checkout Page](#feature-7-the-checkout-page)
    - [Feature 8: The Order Successful Page](#feature-8-the-order-successful-page)
    - [Feature 9: The Sign Up/In/Out Pages](#feature-9-the-sign-up-in-out-pages)
    - [Feature 10: My StepUp](#feature-10-my-stepup)
    - [Feature 11: The Wishlist](#feature-11-the-wishlist)
    - [Feature 12: The Contact Page](#feature-12-the-contact-page)
    - [Feature 13: The Admin Features](#feature-13-the-admin-features)
    - [Feature 14: The Django Admin](#feature-14-the-django-admin)
  - [Features Yet to Implement](#features-yet-to-implement)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks, Libraries and Other Resources](#frameworks--libraries-and-other-resources)
  - [Testing](#testing)
  - [Other Services](#other-services)
    - [Stripe](#stripe)
  - [Deployment](#deployment)
    - [Forking the GitHub Repository](#forking-the-github-repository)
    - [Making a Local Clone](#making-a-local-clone)
    - [Heroku](#heroku)
    - [AWS S3](#aws-s3)
  - [Performance](#performance)
  - [Validation](#validation)
  - [Accessibility](#accessibility)
  - [Bugs](#bugs)
  - [Credits](#credits)
    - [Copyrights](#copyrights)
      - [Media](#media)
      - [Content](#content)
    - [Coding Tips and Tricks](#coding-tips-and-tricks)
    - [Acknowledgments](#acknowledgments)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## Project Overview

Little Explorers is an assignment project created for learning purposes, designed as part of a portfolio in full-stack software development. While it is a fictional e-commerce store, the functionality is built to simulate a real-world online shopping experience.

This project focuses on **e-commerce development** using the **Django framework**, allowing users to browse children's clothing, add items to their cart, and complete purchases with a secure payment system.


### Agile Workflow

![Kanban Board](media\screenshots\canban_board.PNG)

For the development of **Little Explorers**, I have followed an **Agile approach**, breaking down the project into smaller, manageable tasks using **user stories**, a **Kanban board**, and **Labels** to track progress.

I have structured the workflow as follows:

- **User Stories:** Each feature or functionality is documented as a user story to ensure a user-centered design with an acceptance criteria.
- **Kanban Board:**  To manage the development of **Little Explorers**, I use an **Agile workflow** with a **Kanban board**, tracking progress across multiple stages.

- **To Do** – Planned tasks and features.  
- **In Progress** – Tasks currently being worked on.  
- **Done** – Completed tasks.  

The **Kanban board** helps ensure a structured workflow and smooth progress from idea to implementation.
Tasks are managed visually, moving through stages: *To Do*, *In Progress*, and *Done*.
- **Labels:** labels suggest prioritization based on MoSCoW (Must have, Should have, Could have).

The Kanban board can be viewed [here](https://github.com/users/irka775/projects/9/views/1?pane=issue&itemId=95547391&issue=irka775%7Clittle-explorers%7C25).


## User Experience

###  Strategy

#### **Primary Goals**

#### **The site owner's primary goals:**
- To provide an online store for selling children's clothing.
- To easily manage the store, including adding, removing, or editing products.
- To view and manage customer orders, with the ability to update or cancel them if necessary.
- To track customer information and order history for better service.
- To ensure the website is easy to navigate and fully responsive across all devices.
- To provide a customizable Admin Settings Panel for managing store preferences and user permissions.



#### **A potential customer's primary goals:**
- To browse and purchase high-quality children's clothing.
- To register for an account to track orders and manage their shopping experience.
- To view an order history and track past purchases.
- To edit personal account details or delete their account if desired.
- To easily navigate the website and keep track of interactions (e.g., cart items, total spending).
- To have a Wishlist feature to save favorite products for later.
- To use a search and filter system to quickly find specific products.
- To receive updates and offers through email.
- To have a smooth and secure shopping cart experience with clear payment options.
- To leave reviews on purchased products to help other customers make informed decisions.

#### **Developer goals**

As a student in the **Code Institute Full-Stack Software Development program**, I wanted to ensure that this project not only functions as a real-world e-commerce store but also follows best coding practices. While the primary focus of this site is to provide a seamless shopping experience for customers, I have also considered **developer-specific goals** to enhance maintainability, scalability, and performance.

These goals help ensure that the project is **efficiently built, secure, and ready for future improvements**.

##### **Key Developer Goals:**
- Project Deployment – Ensure the website is hosted on a live server for public access.
- Unit Testing – Implement tests to maintain site stability and catch errors before deployment.
- Code Scalability – Structure the code for easy future expansion (new features, product categories, etc.).
- Security Best Practices – Protect user data by implementing secure authentication and encrypted transactions.
- Performance Optimization – Optimize page load times and improve user experience on all devices.
- SEO Implementation – Use meta tags, canonical links, and sitemaps for better search engine ranking.

---

### Business Model

I have chosen a **traditional B2C (Business-to-Customer) e-commerce model**, where the store directly sells children's clothing to customers without intermediaries. The website is designed to provide a **straightforward and user-friendly shopping experience**, ensuring users(parents and guardians) can easily find and purchase high-quality clothing for their children.

Unlike marketplaces that host multiple sellers, **Little Explorers** operates as a **single-vendor store**, curating and offering products sourced from **reliable manufacturers and wholesalers**. 

#### **Business Flow**
-  Little Explorers sources children's clothing from trusted manufacturers and wholesalers.  
-  Products are listed on the website, categorized for easy browsing and filtering.  
-  Customers browse, add items to their cart, and purchase through a secure checkout system (powered by Stripe).  
-  Orders are processed and shipped directly to the customer.  
-  Customers can review their purchases, helping future buyers make informed decisions.  
-  Marketing Efforts: Newsletter Campaigns users can subscribe to receive exclusive discounts, new arrivals, and seasonal promotions via email.

#### **Revenue Model**
- Direct Sales: Customers purchase clothing directly from the store.
- Promotional Offers & Discounts: Special promotions encourage repeat purchases.
- Newsletter Marketing: Registered users can **subscribe to receive promotional emails**, ensuring they stay updated on new collections and deals.
#### **User Experience Focus**
The website is designed to be:
- Easy to navigate, ensuring users can quickly find what they need.
- Mobile-friendly, allowing users to shop conveniently on any device.
- Secure & Trustworthy, integrating **secure payment processing** and **customer reviews** to build confidence.

**Little Explorers' mission** is to provide a seamless shopping experience where users(parents) can find stylish, comfortable, and affordable clothing for their children in just a few clicks.

---

###  Marketing

##### **Marketing Strategy**
For the **Little Explorers** e-commerce project, I have developed a **basic Facebook marketing strategy** to simulate how a real business would promote an online store. However, since this project is created for learning purposes and is not a real e-commerce site, I have set up a **fictional Facebook page** and captured a screenshot of it instead of managing an actual social media presence.
 
This site has a Facebook Business page with a link on the page footer. **Screenshot of the Fictional Facebook Page:**

 ![Facebook Page Screenshot](media\facebook_bussines_page.PNG) 

While this page is only a placeholder for learning purposes, in the future, a fully functional Facebook page could be implemented with more advanced social media marketing strategies like:
- Regular product updates and promotions to engage potential customers.  
- Customer interaction via comments, messages, and reviews to build trust.  
- Facebook Ads campaigns to increase visibility and drive traffic to the store. 


##### **Newsletter Subscription (Email Marketing)**
**Little Explorers** integrates **Mailchimp** to allow users to subscribe to newsletters during registration. This simulates how an online store can engage with customers through **exclusive offers, product updates, and seasonal promotions**.

- Upon subscribing, users are redirected to a confirmation page.  
- The site owner can track subscribers in the **Mailchimp Audience Dashboard**.  
- Subscribers receive promotional emails when new collections, discounts, or special events are launched.


### **Confirmation After Subscribing**
![Subscription Confirmation](#)

### **The New Subscriber Appears in the Mailchimp Audience Dashboard**
![Mailchimp Audience](#)

### **Subscribers Receive Promotional Emails from Little Explorers**
![Mailchimp Campaigns](#)










-----------------------------------------------------------------
--------------------------------------------------------

### **Future Marketing Plans (If the Project Expands)**
If **Little Explorers** grows into a real business, the marketing strategy could include:
- **A fully developed and active Facebook page** with real promotions.  
- **Expansion to Instagram & Pinterest** for better product showcasing.  
- **Google Ads & SEO optimization** to attract organic traffic.  
- **Loyalty programs and referral discounts** to increase repeat customers.  


---



This site has a Facebook Business page with a link on the page footer. It can be viewed [here](https://www.facebook.com/stepupshoeseurope/)

Upon registering for an account, customers can check a box to receive news and offers through email via [Mailchimp](https://mailchimp.com/).

Upon registering, the user ir redirected to a new page confirming their subscription. The site owner can now see the new subscriber on their audience dashboard, and new campaigns will be sent to them too.


**The mailchimp signup form**

## ![Meta-tags seo](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/misc/mailchimp_field.png)

**Confirmation after subscribing**

## ![Meta-tags seo](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/misc/mailchimp_subscr_conf.png)

**The new subscriber is added to the site owners audience in the Mailchimp Dashboard**

## ![Meta-tags seo](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/misc/mailchimp_audience.png)

**They will receive emails when the site owner creates a new campaign**

## ![Meta-tags seo](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/misc/mailchimp_campaigns.png)

</details>
















------------------------------------------------------------------------------------
---------------------------------------------------------------------------------

#### Search Engine Optimisation

I have generated a sitemap.xml and robots.txt file, and only included relevant canonical links (pages that are not duplicates) which helps Google map the pages of the site.

I have also done some research on highest searched words in shoe retailing, and came up with this title and description:

![Meta-tags seo](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/misc/seo.png)

### Structure

This website has 11 custom built pages and 16 (not all are used) account operations Django Allauth pages. The navbar at the top of the screen gives users access to the most important pages at all times.

#### Pages

**Accessible to all users**

- Home - The landing page of the site, with a full screen carousel hero image giving first time visitors a nice welcome

- Products - This is a list of the products when clicking on a category in the navbar, or performing a search

- Product Detail - The dedicated page for a specific product, where users can read a description and perform all given tasks for the product

- Cart - A user purchases an item by adding it to the cart; clicking on it will show all cart items

- Checkout - Here users enter their delivery details and card info to proceed with their order

- Order Confirmation - The page show when a payment has successfully been made, showing the order information

- The Sign In and Sign Up pages

- Contact - A simple contact form that is sent to the site owner

**Accessible to signed in users**

- My StepUp - The users order history, billing and shipping info is here, as well as the users wish list, editable here in the My StepUp page.

- Sign Out

- Other accounts operations pages such as Change Password or Password reset

- Delete Account - Allows the user to completely remove their account from StepUp

**Accessible to Admin users**

- Add Brand or Product - This is where admin users can add new products to the website

- Edit Product - The page for admins to edit or delete products

- Manage Brands - An overview of all brands on the site with edit and remove functionality

#### Pages provided by Django

These pages are provided by the Allauth package of the Django framework, but are customised by me to fit in with the rest of the site. Read more about Allauth [here](https://django-allauth.readthedocs.io/en/latest/)

- Sign Up - where users can register for an account on the site

- Sign in - Registered users can log accessing their personal info etc by signing in

- Sign Out - The same goes for signing out

- Various pages for email verification and password reset, etc

#### Technical Design

##### Code Structure

I have devided the code into apps as per Django best practice, for the different areas of functionality.

- Home - basic functionality for the home page

- Products - all functionality related to the products on the site

- Cart - functionality for the users shopping cart

- Checkout - functionality for the user to go through with the order and payment

- Profiles - functionality regarding the users profile and order data (My StepUp)

- User Account - The app in which users can delete their account

**Other Directories and files**

- static - css and javascript files

- media - images for the development website (other images are used in the production version)

- stepup - project folder containing settings, urls and other configuration files for the whole project

- templates - contains the base template and templates (HTML-files with Django logic) for the Django allauth authentication

- manage.py - the main python project file to get the web application running

- README.md - the document you are reading right now, documentation of the whole project

- custom_storages.py - configuration for storage of media and static files on AWS S3

- Procfile - needed for deployment to Heroku to specify commands to be executed by the app on startup

- requirements.txt - a list of dependancies (installed packages) that the project requires for the application to function

- robots.txt and sitemap.xml - files configured for Search Engine Optimisation

Enviromental Variables such as API-keys, passwords etc are stored securely in the back end (in the development environment and in the Heroku App settings) so that regular users do not have access to them.

##### Database

The [SQLite](https://www.sqlite.org/index.html) database was used for the development environment, and the [Postgres](https://www.postgresql.org/) database for production as an add-on via Heroku. Both are relational databases and work well with the Django framework used for this project.

##### Data Models

The following models have been used to populate the database and for the site to function as it should:

- **User** - the built in Django User model, facilitates the users basic information

- **Category** - the category in which the product is placed

- **Brand** - the brand of the product

- **Product** - the model for the product itself and its details

- **Review** - a model for users to give the product a rating and a review

- **Order** - a users successful purchase leads to an instance of the Order model being created, storing delivery and user data

- **OrderLineItem** - a model holding the product information for a single product, binding the product model together with the order

- **UserProfile** - the model storing the users product and order information

- **WishListItem** - the customer has the option to save an item, which will then appear in their wish list on the My StepUp page

##### Schema of models

Below is a schema of the models used in this application, created with [Lucidchart](https://lucid.co/product/lucidchart)

![Schema of models](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/schemas/db_model_schema.png)

### Scope - Epics and User Stories

#### Epic 1: Base functionality and ease of use

1. As a user, the intention of the specific page is made clear to me, so that I know the purpose of that page

2. As a user, I can access important links such as home, products, my cart, sign in/out, and My StepUp by scrolling and/or clicking once, regardless of where on the site I am, so that i can easily navigate the site

3. As a user, I can see a form to register for newsletters repeatedly throughout the website, so that I can receive news on products and campaigns

4. As a user, I can see a link in the footer to the site’s Facebook Business Page, so that I can follow the company on Facebook

5. As a user, it is visible if I am signed in or not, so that I am made aware of this

6. As a user, the choices I make on the site are confirmed to me, so that I am always aware of them

#### Epic 2: Products

7. As a user, I can browse a list of products for sale on the site so that I can find the product I seek

8. As a user, i can perform a search, so that products matching the search appear in the products list

9. As a user, I can sort the products list by category, alphabetically or by rating, so that i can quickly find the product I seek

10. As a user, I can view the most important details of the product in the product list, such as model, brand, category, price, rating, and image so that i know most details without having to click on the product

11. As a user, i can click the product in the products list so that I can view the products details

12. As a user, I can choose the size of the product, as well as the quantity, so that I can purchase the correct size/quantity

#### Epic 3: The Cart

13. As a user, I can add a product to my cart by clicking ’Add to Cart’ from the product detail page so that I can purchase the product

14. As a user, I can always see the total price of my cart in the navigation bar, so that I know what the total cost will be

15. As a user, i can adjust the quantity of the product chosen after adding it to the shopping cart

16. As a user, I can view the products added to my cart by clicking the cart icon or by adding an item to the cart

17. As a user, I can click the remove from cart button, so that I can easily remove products from my cart

#### Epic 4: Checkout

18. As a user, I can click on Proceed to Checkout, so that I can purchase the items in my cart

19. As a logged in user, on the Checkout page, I can choose to save my delivery address to My StepUp, so that I can retain it for future orders

20. As a user, i can enter my card details on the checkout page, so that I can make the desired purchase

21. As a user, I am informed of whether my purchase was successful or not via the Order Successful page, as well as via an email sent upon order confirmation

#### Epic 5: User registration and account

22. As a user, I can register for an account on the site, so that I can gain all the site’s customer benefits

23. As a user, I am not able to access pages that require authentication if I am not signed in

24. As a user, I have to confirm my email address to complete my account registration

25. As a logged in user, i can view a My StepUp page, so that I can view my previous orders, and view and update my delivery and contact details

26. As a logged in user, I can add my delivery details to the My StepUp page, so that it is my default delivery address for my order on the checkout page

27. As a logged in user, I can choose to delete my account, so that my user account no longer exists

#### Epic 6: The Wish List

28. As a logged in user, I can add a product to my Wish List, so that I can easily view it later

29. As a logged in user, I can remove a product from my Wish List, so that it no longer is there

30. As a logged in user, I can add products from my Wish List to my cart, so that I can easily purchase them (user story removed for now)

#### Epic 7: Reviews

31. As a user, i can read user reviews for products that have received them, so that I easier know if the product is right for me

32. As a logged in user, i can write a review and rate a product in the list, so that other users can benefit from this

33. As a logged in user, I can remove my review of a product, so that it no longer is there

#### Epic 8: Contact

34. As a user, I can get in touch with the site owner, regardless of whether I am signed in or not

#### Epic 9: Site Owner functionality

35. As a site owner, I can view an admin page, where I can perform batch editing of model instances on the site including products, categories, orders and brands

36. As a site owner, I can add, edit or remove any product on the site

37. As a site owner, I can add, edit or remove any brand on the site

38. As a site owner, I can remove any products review on the site

39. As a site owner, I can receive an email from a user that fills in the contact form, so that they can get in touch with me

#### Epic 10: Terms and Policy

40. As a user, I can view a terms document via a link in the sites footer

41. As a user, I can view a privacy policy document via a link in the sites footer

### Skeleton

#### Wireframes

![Wireframe of Product Detail on Desktop](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/wireframes/images/product_detail_desktop.png)

Wireframe images were made for all pages except for the ones rarely used by the site, for example password change and email confirmation.

All wireframes can be viewed [here](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/wireframes/WIREFRAMES.md)

### Surface

#### Colors

![Colors](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/surface/colors.png) (palette generated at https://imagecolorpicker.com)

I have chosen the combination of a dark purple night sky as the background, orange and white for text and main buttons in orange and grey. As design is important to me, I couldn't help myself in experimenting and exploring in the possibilities for this project.

#### Design Choices

I have added lots of semi-transparent elements to create a feeling of three-dimentionality, for example the navbar. It fades to completely transparent on scroll, so users can view the content in full.

## ![Navbar](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/surface/gif_navbar_scroll.png)

Buttons are coloured with CSS-style attribute background: linear-gradient to create a glossy finish on the main buttons.
Admin operation buttons on products and brands are styled differently to distinguish them from the others.

Here you can see some of the button elements, as well as the badge, here used to indicate that the product is on sale.

## ![Button Elements](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/surface/button_badge_elements.png)

#### Typography

Google Fonts was used for all fonts on this site, and I have used three fonts:

- Anaheim for the general content, but also the main heading
  ![Anaheim Font](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/surface/font_anaheim.png)

---

- Average for the hero images
  ![Anaheim Font](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/surface/font_average.png)

---

- Abel for the page headings and main products nav menu

I think they blend well together with the main Anaheim Logo:

## ![Anaheim Font](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/surface/fonts_abel_anaheim.png)

## Existing Features

### Feature 1: The Navbar

The navbar allows users to easily navigate the website, no matter which page they are on. The navbar consists of:

- The products navigation menu, with sorting or filtering possibilities
- A search bar, displaying results based on product name
- A Sign In/Sign Up icon
- Cart

---

**Products Nav Desktop**

## ![Home Desktop Products nav](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/desktop_prod_nav.png)

The navbar is also dynamic, transparent when users scroll down, for full content visibility, and turns a translucent blue shade when scrolling up, so menu items are visible.

If the user us logged in, the Sign Up/Sign In menu becomes the Account menu, and if the user has admin privileges the user can access the manage brands an add product or brand pages through here.

There is a floating badge in the top right corner displaying the grand total and item count, always visible of the user scrolls up, which also gets an orange border if items are added.

<details>
    <summary>View More Images</summary>

---

**Sign In/Up Menu**

## ![Navbar Sign In Up](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/sign_in_up_menu.png)

**Tablet nav for admin users**

## ![Navbar Sign In Up](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/tablet_auth_nav.png)

**Desktop nav after scroll up**

## ![Home Desktop Products nav](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/desktop_nav_after_scroll_up.png)

**Mobile nav after scroll down**

## ![Navbar Sign In Up](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/mobile_nav_scroll_down.png)

**Cart total and count badge**

## ![Cart total and count badge](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/cart_badge_filled.png)

</details>

**User stories covered**

2. As a user, I can access important links such as home, products, my cart, sign in/out, and My StepUp by scrolling and/or clicking once, regardless of where on the site I am, so that i can easily navigate the site

3. As a user, it is visible if I am signed in or not, so that I am made aware of this

4. As a user, the choices I make on the site are confirmed to me, so that I am always aware of them

5. As a user, i can perform a search, so that products matching the search appear in the products list

6. As a user, I can always see the total price of my cart in the navigation bar, so that I know what the total cost will be

7. As a user, I can view the products added to my cart by clicking the cart icon or by adding an item to the cart

8. As a user, I am not able to access pages that require authentication if I am not signed in

### Feature 2: The Home Page

The home page is the landing page of the site, with the purpose to entice the user to proceed to the products.

---

**Home On Desktop**

## ![Home Desktop](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/desktop_home.png)

The user is presented with a window-sized (half window on tablet/mobile) carousel, consisting of three hero images giving the user a feel of edecation and quality on first sight. The images link to displaying the products results page, with different filtering (fitness, new and sneakers).

<details>
    <summary>View Images on mobile and tablet</summary>

---

**Home Mobile**

## ![Home Mobile](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/mobile_home.png)

**Home Tablet**

## ![Home tablet](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/tablet_home.png)

</details>

**User stories covered:**

1. As a user, the intention of the specific page is made clear to me, so that I know the purpose of that page

2. As a user, I can access important links such as home, products, my cart, sign in/out, and My StepUp by scrolling and/or clicking once, regardless of where on the site I am, so that i can easily navigate the site

3. As a user, the choices I make on the site are confirmed to me, so that I am always aware of them

### Feature 3: The Footer

The footer includes a signup form for a newsletter, as well as a link to the site's Facebook business page and important links, such as contact, terms of use and the pages privacy policy. Wherever the user is on the site, except for some account operations, the footer is visible at the bottom of the page, giving the user access to these important links at virtually all times.

---

**Footer on tablet:**

## ![Footer](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/tablet_footer.png)

The policy and terms appear in a modal window, which users easily can close and access again at will, due to the links placement in the footer.

<details>
    <summary>View Privacy policy on mobile</summary>

---

## ![Mobile privacy policy](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/mobile_privacy_policy.png)

</details>

**User stories covered:**

3. As a user, I can see a form to register for newsletters repeatedly throughout the website, so that I can receive news on products and campaigns

4. As a user, I can see a link in the footer to the site’s Facebook Business Page, so that I can follow the company on Facebook

5. As a user, I can view a terms document via a link in the sites footer

6. As a user, I can view a privacy policy document via a link in the sites footer

### Feature 4: The Products List

The products list is dynamic and will show the relevant products, depending on if the user has performed a search, clicked on a category or filtered the products in any other way.

---

**The Products list**

## ![Desktop products list](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/desktop_products.png)

Filtering can be done:

- By category
- By brand
- By gender
- By whether items are new or on sale
- By users performing a search

On top of this, sorting can be done by price, rating, name or category. Users can see if the item is on sale or new, already in the products list, with a badge saying "new" or "save €".

In the products list, the most important details of each item are displayed; name, brand, category, gender, price, if on sale, if new, and of course the product image. For admin users. the edit and delete buttons are also visible here.

<details>
    <summary>View More Images</summary>

---

**Performing a search**

## ![Mobile perform search](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/mobile_perform_search.png)

**Desktop products filtered**

## ![Desktop products filtered](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/desktop_products_filter.png)

**Tablet products for admin users**

## ![Tablet products for admin users](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/tablet_auth_products.png)

</details>

**User stories covered:**

7. As a user, I can browse a list of products for sale on the site so that I can find the product I seek

8. As a user, i can perform a search, so that products matching the search appear in the products list

9. As a user, I can sort the products list by category, alphabetically or by rating, so that i can quickly find the product I seek

10. As a user, I can view the most important details of the product in the product list, such as model, brand, category, price, rating, and image so that i know most details without having to click on the product

### Feature 5: The Product Detail Page

This page shows a dedicated page for the specific product. Here users can choose the size and the quantity of the product, as well as read a description and user reviews of it.

---

**Desktop product detail**

## ![Desktop products detail](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/desktop_product_detail.png)

Here users can decide the quantity as well as the size of the product to be added to their cart. If registered and logged in, users can add the item to their Wishlist.

Logged in users can also write and remove their own reviews here. lastly, admin users can edit and remove the product through links here, and remove any review if desired.

<details>
    <summary>View More Images Here</summary>

---

**Product detail on mobile**

## ![Reviews Box](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/mobile_product_detail_buttons.png)

**Reviews Box if Product has reviews**

## ![Reviews Box](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/tablet_reviews.png)

**Delete review dialog modal**

## ![Reviews Box](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/mobile_delete_review.png)

**Delete product admin dialog modal on desktop**

## ![Reviews Box](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/delete_product_modal.png)

</details>

**User stories covered:**

11. As a user, i can click the product in the products list so that I can view the products details

12. As a user, I can choose the size of the product, as well as the quantity, so that I can purchase the correct size/quantity

13. As a user, i can read user reviews for products that have received them, so that I easier know if the product is right for me

14. As a logged in user, i can write a review and rate a product in the list, so that other users can benefit from this

15. As a logged in user, I can remove my review of a product, so that it no longer is there

### Feature 6: The Cart

The Cart is the users digital shopping cart, containing all products the user has added to it and their details, including the chosen quantity and size if applicable.

---

**The cart page on desktop**

## ![The cart page](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/desktop_cart_several_items.png)

Its grand total and count is always partially visible in the navbar but has a dedicated page through which users can go through with the payment when they are done shopping.

A toast, a small dialog window at the top right, will be visible after adding an item to the cart, letting the user know that the add was successful. The user can view, change quantity and remove items from the cart on the cart page.

<details>
    <summary>View More Images Here</summary>

---

**Cart page on tablet**

## ![Cart page on tablet](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/tablet_cart_filled.png)

**Added item to cart dialog toast on mobile**

## ![Added item to cart dialog toast on mobile](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/mobile_added_to_cart.png)

**Buttons to update quantity or remove product from cart**

## ![Buttons to update quantity or remove product from cart](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/cart_hover_update_btn.png)

</details>

**User stories covered:**

13. As a user, I can add a product to my cart by clicking ’Add to Cart’ from the product detail page so that I can purchase the product

14. As a user, I can always see the total price of my cart in the navigation bar, so that I know what the total cost will be

15. As a user, i can adjust the quantity of the product chosen after adding it to the shopping cart

16. As a user, I can view the products added to my cart by clicking the cart icon or by adding an item to the cart

17. As a user, I can click the remove from cart button, so that I can easily remove products from my cart

### Feature 7: The Checkout Page

The checkout page features a form for the user to fill in, with name, email, phone nr, delivery address and card details.

---

**Checkout page on desktop**

## ![Checkout page on desktop](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/desktop_checkout.png)

From the checkout page, if user is authenticated, they can save their details to their My StepUp profile so they are prefilled for the next order. If they are not logged in, a link to log in is displayed in place of that option.

If the payment fails or info is sufficient, the user gets a new chance to enter their info, without being charged.

<details>
    <summary>View More Images Here</summary>

---

**Checkout page on tablet**

## ![Checkout page on tablet](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/tablet_checkout_details_filled.png)

**Checkout page card details on mobile**

## ![Checkout page bottom on mobile](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/mobile_pay_btn.png)

**Payment processing on mobile**

## ![Checkout page bottom on mobile](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/mobile_payment_processing.png)

</details>

**User stories covered:**

18. As a user, I can click on Proceed to Checkout, so that I can purchase the items in my cart

19. As a logged in user, on the Checkout page, I can choose to save my delivery address to My StepUp, so that I can retain it for future orders

20. As a user, i can enter my card details on the checkout page, so that I can make the desired purchase

### Feature 8: The Order Successful Page

If the user has made a successful purchase, an order confirmation will be displayed to the user, and sent to the given email address during checkout. If the order was successful, the cart will be emptied, and, if the user is logged in and had any of the items in their wishlist, they are removed from there.

In the confirmation, the user can view the items order, their sizes and quantity, an order number, grand total and delivery details.

---

**Order confirmation page on desktop**

## ![Order confirmation page on desktop](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/desktop_order_confirmation.png)

<details>
    <summary>View More Images Here</summary>

---

**Order Confirmation page on tablet**

## ![Order Confirmation page on tablet](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/tablet_order_confirmation.png)

**Order Confirmation page on mobile**

## ![Order Confirmation page on mobile](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/mobile_order_confirmation.png)

**Order Email Received**

## ![Order Email Received](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/order_confirmation_email_received.png)

</details>

**User stories covered:**

21. As a user, I am informed of whether my purchase was successful or not via the Order Successful page, as well as via an email sent upon order confirmation

### Feature 9: The Sign Up/In/Out Pages

Signing up, in and out are vital parts of this site, allowing users to save customer details to improve the users experience of the site. It also creates a possibility for the site owner to gain revisiting customers.

---

**Sign Up page on mobile**

## ![Sign Up page on mobile](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/mobile_sign_up.png)

Users can easily sign up through the link in the navbar.

As users browse the site, they will see various links to sign in to access functionality, such as adding items to a wishlist, saving delivery details or posting reviews of products.

Upon registration, the site sends an email to confirm the users email address. They then can sign in to the site and access their My StepUp profile and all other functionality for signed in users.

<details>
    <summary>View More Images Here</summary>

---

**Sign Up page on tablet**

## ![Order Confirmation page on tablet](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/tablet_signup.png)

**Sign In page on tablet**

## ![Order Confirmation page on tablet](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/tablet_signin.png)

</details>

**User stories covered:**

22. As a user, I can register for an account on the site, so that I can gain all the site’s customer benefits

23. As a user, If I am not signed in, I am redirected to sign in/up if I click on any of the links or buttons restricted to logged in users

24. As a user, I have to confirm my email address to complete my account registration

### Feature 10: My StepUp

Each user can access their own personal profile where they can enter their delivery information, subscribe or unsubscribe to the newsletter and keep track of their orders.

---

**The My StepUp page on desktop including the Wishlist**

## ![The My StepUp page on desktop](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/desktop_my_stepup.png)

Here, users can also change their password, and delete their account completely if desired.

<details>
    <summary>View More Images Here</summary>

---

**Order History box on the My StepUp page, tablet**

## ![Add item to Wishlist on tablet](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/tablet_order_history.png)

**Account Operations area in My Stepup, mobile**

## ![Account Operations area in My Stepup, mobile](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/mobile_account_operations.png)

</details>

**User stories covered:**

25. As a logged in user, i can view a My StepUp page, so that I can view my previous orders, and view and update my delivery and contact details

26. As a logged in user, I can add my delivery details to the My StepUp page, so that it is my default delivery address for my order on the checkout page

27. As a logged in user, I can choose to delete my account, so that it no longer exists

### Feature 11: The Wishlist

Users can add products to their Wishlist, if they do not wish to purchase items straight away. This is located at the top of the My StepUp page. The products will remain in the users Wishlist until they have purchased the item or removed it from the list. Check image above for desktop view.

<details>
    <summary>View Images Here</summary>

---

**The My StepUp page on mobile**

## ![The My StepUp page on mobile](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/mobile_my_stepup_wl_filled.png)

**Add item to Wishlist on tablet**

## ![Add item to Wishlist on tablet](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_2/tablet_add_to_wl.png)

</details>

**User stories covered:**

28. As a logged in user, I can add a product to my Wish List, so that I can easily view it later

29. As a logged in user, I can remove a product from my Wish List, so that it no longer is there

30. As a logged in user, I can add products from my Wish List to my cart, so that I can easily purchase them

### Feature 12: The Contact Page

This is a standard contact form, through which users can contact the site owner. The form is sent by email to the site owner.

---

**Contact Page on desktop**

## ![Contact Page on desktop](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_1/desktop_contact.png)

**User stories covered:**

34. As a user, I can get in touch with the site owner, regardless of whether I am signed in or not

35. As a site owner, I can receive an email from a user that fills in the contact form, so that they can get in touch with me

### Feature 13: The Admin Features

There are extra features for admin users, so that site owners can add, edit and remove products, brands and reviews on the site. This is visible in the navbar, where two more items are visible in the account menu; Add Brand or Product and Manage Brands.

---

**The Admin account menu**

## ![The Admin account menu](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/tablet_auth_nav.png)

It is also visible in the products page, where a plus sign has appeared at the top, aswell as the Edit and Delete buttons on each product card in the list. On the product detail page, the Edit and Delete buttons are also visible, and every review displays a delete button, which deletes the review in question after confirmation.

The Manage Brands page provides an overview of the brands on the site, and the possibility to edit or remove brands. Here admin users can change the brand name or the logo image for the brand. The changes are reflected in the Brands menu item in the Products nav menu, as well as in the product detail page, where, if uploaded, a brand image is visible.

The Add Brand or Product page has two forms, for brand and product respectively. The product form has a lot of fields, and complex validation (for example, if an item is on sale the sale price cannot be higner that the initial one). Each form has a "add" button and the product or brand is added to the site if the form is valid. If not, an error is visible or the user is taken back to the form for them to fill it out properly.

The Edit Product page consists of the same product form as on the previously mentioned page, only already filled out with the products current information. Here the admin user can update any current info for the product, as well as change the product image.

<details>
    <summary>View More Images Here</summary>

---

**The Manage Brands page on tablet**

## ![The Manage Brands page on tablet](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/tablet_manage_brands.png)

**Added new brand, Manage Brands page on mobile**

## ![Added new brand, Manage Brands page on mobile](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/mobile_add_brand_successful.png)

**Add brand or product page on desktop**

## ![Add brand or product page on desktop](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/desktop_add_brand_product.png)

**Edit Product page on mobile**

## ![Edit Product page on mobile](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/mobile_edit_product_new_image.png)

**Products list with Edit and Delete buttons, desktop**

## ![Edit Product page on mobile](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/desktop_auth_products.png)

**Price validation in add or edit product form**

## ![Price validation in add or edit product form](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/update_product_invalid_price.png)

</details>

**User stories covered:**

36. As a site owner, I can add, edit or remove any product on the site

37. As a site owner, I can add, edit or remove any brand on the site

38. As a site owner, I can remove any products review on the site

### Feature 14: The Django Admin

The Django framework provides an excellent admin interface which this site has taken full advantage of. The admin panel of this site contains all instances of all database models, and the ability to edit, remove or add instances.

---

**The Django Admin Panel**

## ![The Django Admin Panel](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/screenshots/user_case_3/admin_home.png)

**User stories covered:**

35. As a site owner, I can view an admin page, where I can perform batch editing of model instances on the site including products, categories, orders and brands

## Features Yet to Implement

User story 30, adding products to the cart, is a could have user story, and for this implementation I decided not to include in production. This due to the need for quantity and size input from user, and there was no space on the My StepUp page in the current design for this.

Also, the ability for site owners to keep track of stock numbers is an important future update.

Having several images for the products is intended, but, as this is a fictional site and the images are royalty free, I had to make do with the single image for each one. In a real world scenario, the site owner would provide me with all content for the site, erasing this issue.

## Technologies Used

### Languages

- [Python 3.8](https://www.python.org/) was used for backend programming

- [HTML5](https://en.wikipedia.org/wiki/HTML5) was used for building all web pages

- [CSS3](https://en.wikipedia.org/wiki/CSS) was utilized for styling the website

- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) for frontend programming

### Frameworks, Libraries and Other Resources

This project is built solely through the framework [Django](https://www.djangoproject.com/), and I have tried to make use of its many powerful features.

- I have used [Bootstrap 4](https://getbootstrap.com/) as a framework for styling for efficiency purposes.

- The JavaScript framework [JQuery](https://jquery.com/) was used to minimize written code.

- [Font Awesome](https://fontawesome.com/) fonts were used for all icons in this project.

- [Google Fonts](https://fonts.google.com/) - Were used for all fonts in this project.

- [Facebook Pages](https://www.facebook.com/pages/create/?ref_type=site_footer) was used to create the Facebook Business Page that is linked on the site.

- [Mailchimp](https://mailchimp.com/) was used to create the newsletter signup form.

- [Git](https://git-scm.com/) - Version control system used to commit and push to Github via Gitpod.

- [Github](https://github.com/) - The projects repository and all its branches were commited,
  and pushed to Github.

- [Heroku](https://www.heroku.com) - Used to deploy the application.

- [AWS S3 Bucket](https://aws.amazon.com/s3/) - Used to host media (images) and static(CSS and JavaScript) files for the site.

- [Stripe](https://stripe.com/) - Used to process the users payments and handle webhooks.

- [Gitpod](https://gitpod.com/) - All code was written and tested with the Gitpod web-based IDE.

- [Balsamiq Wireframes](https://balsamiq.com/wireframes/) was used to create wireframe images of the website which you can view [here](#).

- [Lucidchart](https://lucid.co/product/lucidchart) was used to create the visual [model schema](#schema-of-models) of the project.

## Testing

Thorough testing of the StepUp site was performed and can be viewed [here](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/testing/TESTING.md).

## Other Services

### Stripe

Stripe was used as a payment service, allowing users to pay for products. The process:

1. Create an account at https://stripe.com/
2. Go to the developers pane and navigate to API keys
3. Copy the publishable and secret keys and put them in your config vars in your development envirenment (and in Heroku config vars in production)

Webhooks were created too to make sure payments did not fail due to web errors. This can be done by doing the following:

1. Navigate to Webhooks on the page, and create an endpoint with the url you send your webhooks to, in this case, the url is https://stepup-shoes.herokuapp.com/checkout/wh/
2. Add events to listen for, for example payment_intent_succeeded and payment_intent.payment_failed as in this case
3. The webhooks should be sent when processing orders in all cases

## Deployment

### Forking the GitHub Repository

To make a clone, or 'Fork' this repository, follow the steps below.

1. Access your GitHub account and find the relevant repository.
2. Click on 'Fork' on the top right of the page.
3. You will find a copy of the repository in your own Github account.

### Making a Local Clone

1. Access your GitHub account and find the relevant repository.
2. Click the 'Code' button next to 'Add file'.
3. To clone the repository using HTTPS, under clone with HTTPS, copy the link.
4. Open Git Bash.
5. Access the directory you want the clone to be have.
6. In your IDE's terminal type 'git clone' and the paste the URL you copied.
7. Press Enter.
8. You now have a local clone.

### Heroku

This application has been deployed from Github using Heroku. Here's how:

1. Create an account at [heroku.com](https://www.heroku.com/)
2. Create a new app, add app name and your region
3. Click on create app
4. Go to "Settings"
5. Under Config Vars, add your sensitive data (creds.json for example)
6. For this project, I set buildpacks to <Python> and <NodeJS> in that order.
7. Go to "Deploy" and at "Deployment method", click on "Connect to Github"
8. Enter your repository name and click on it when it shows below
9. Choose the branch you want to buid your app from
10. If desired, click on "Enable Automatic Deploys", which keeps the app up to date with your Github repository
11. All done!

### AWS S3

The deployed version of this website has static(CSS and JavaScript) and media files hosted to it via a web based service called Amazon Web Services S3 Bucket.

The steps to take are:

1. Create an account at aws.amazon.com
2. Navigate to the IAM application and create a user and group
3. Set the AmazonS3FullAccess for the user and copy the AWS ACCESS and SECRET keys as config vars to your workspace and deployment environment
4. Create a new Bucket within the S3 application with an appropriate name.
5. Enable public access for your bucket so users can access and use the services on your website (upload, view, download, etc). More info can be read in the official documentation: https://aws.amazon.com/s3/

## Performance

Performance was tested using Google Chrome's Lighthouse tool in DevTools built into the browser. The performance tests can be viewed [here](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/performance/PERFORMANCE.md).

## Validation

Thourough validation of all code was made without errors. The results can be viewed [here](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/validation/VALIDATION.md).

## Accessibility

Accessibility tests were also performed with the [WAVE](https://wave.webaim.org/) Web Accessibility Evaluation Tool and passed all tests. They can be viewed [here](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/accessibility/ACCESSIBILITY.md).

## Bugs

Here are a few of the bugs found during the testing phase.

**Bug** - The forms in the Manage Brands page were displaying information for the wrong brand instances
_Fix_ - Remove the sorting functionality in the pages Django view which sorted the instances of brands but not the forms

**Bug** - Duplicate ID's in HTML elements due to Django creating the same form over again in Manage Brands
_Fix_ - Give a prefix of the brands ID to the form, ensuring each one is unique

**Bug** - Sizes displaying as 'N/A' even though product has size on Order Confirmation page
_Fix_ - Logic in order confirmation had false values, updated and works

**Bug** - When sent a password through the Django Allauth service, the link sent is http and not https. A warning by stripe in the terminal that payments for production only works with https is issued. This doesn't affect this site as the payments are for testing purposes, but needs to be investigated further in the future
_Fix_ - No fix as of now

**Bug** - Price validation in product form failing
_Fix_ - Creating variables in the JavaScript file that controls this, as the id's for the form are different on the edit and add pages where the form is present

**Bug** - Navbar animation jumpy and not displaying menus correctly at all times
_Fix_ - Refine JavaScript to add and remove classes to show and hide all elements of the nav upon clicking and accessing other menus, remove animations

**Bug** - Modal not displaying for remove review, only overlay
_Fix_ - Remove css attribute backdrop filter for modal causing issues

**Bug** - 404 error at checkout when processing payment
_Fix_ - Fix try and except in code that removes users wishlist items that are purchased

## Credits

### Copyrights

#### Media

Images of the products and the site background are all from [Unsplash](https://unsplash.com/).

Images of logos are from [Wikimedia Commons](https://commons.wikimedia.org/wiki/Main_Page) and from the brands website, with consent.

The shoe icon in the pages favicon comes from here: https://en.m.wikipedia.org/wiki/File:Running_shoe_icon.png

#### Content

As I have no data on the images of model or other information, I have taken product information from similar products for the ones on this site.

The sites I have taken product information from are here:

https://www.cucufashion.co.uk/hexya-orange-sock-sneakers/

https://www.amazon.com/ElegantPark-Womens-Buckles-Evening-Sandals/dp/B01GR2ZJGY?th=1

https://www.endclothing.com/gb/comme-des-garcons-play-x-converse-chuck-taylor-1970s-hi-p1-k112-1.html

https://www.farfetch.com

https://www.vallgatan12.se/

https://erwans.com/

https://www.google.com/shopping

https://theluxurycloset.com/women/chanel-creamblack-leather-cap-toe-bow-mary-jane-block-heel-pumps-size-38-p499197?cur=GBP

https://www.redbubble.com/i/socks/i-love-Mouths-pattern-by-virilamissa/62023266.9HZ1B

clarks.co.uk

https://www.sweatshop.com/Running-Shoes/Nike/Free-Run-5.0-Ladies-Running-Shoes-Black-or-White/255056

https://danishendurance.com/products/low-cut-running-socks?variant=33432525307963

https://axelarigato.com/

https://www.gearcor.com/t53009/Timberland-Pro-Endurance-PR-Wedge-6inch-Soft-Toe.htm

https://www.johnstonsofelgin.com/

https://www.nike.com

https://www.timberland.se

https://www.asics.com

https://www.bellabelleshoes.com

https://www.minfot.se

https://www.gucci.com

### Coding Tips and Tricks

These are tips that have helped me along the way for this project:

**Code Institute Boutique Ado project**

**Hiding header on scroll down:**
https://medium.com/@mariusc23/hide-header-on-scroll-**down-show-on-scroll-up-67bbaae9a78c

**Distribute navbar items evenly:**
https://stackoverflow.com/questions/32140607/horizontal-list-that-evenly-divides-remaining-space-via-css/32140682

**Split list into li items from model:**
https://stackoverflow.com/questions/8317537/django-templates-split-string-to-array

**Proper way to handle two forms**
https://stackoverflow.com/questions/1395807/proper-way-to-handle-multiple-forms-on-one-page-in-django

**Title in Django template**
https://stackoverflow.com/questions/14268342/make-the-first-letter-uppercase-inside-a-django-template

**Adapted Mailchimp form**
https://bootstrapious.com/p/mailchimp-signup-form -->

**Raise error in model form method**
https://docs.djangoproject.com/en/4.0/ref/forms/validation/

**Parseint JQuery:**
https://stackoverflow.com/questions/16269385/jquery-adding-2-numbers-from-input-fields

**Smooth Scrolling:**
https://css-tricks.com/snippets/jquery/smooth-scrolling/

**Scroll incl for window width**
https://stackoverflow.com/questions/7715124/do-something-if-screen-width-is-less-than-960-px

**Looping, zip, lists in view and template:**
https://stackoverflow.com/questions/12684128/looping-through-two-objects-in-a-django-template

**Item at certain position in object from template:**
https://stackoverflow.com/questions/4286461/django-templates-first-element-of-a-list

**Back button:**
https://stackoverflow.com/questions/27325505/django-getting-previous-url

**Footer:**
https://radu.link/make-footer-stay-bottom-page-bootstrap/

**Removing navbar transitions:**
https://stackoverflow.com/questions/13119912/disable-bootstraps-collapse-open-close-animation

### Acknowledgments

I want to thank my mentor Mo Shami positive vibes throughout the course, and pointing me in the right directions. Also pmeenys project [Love Rugby](https://github.com/pmeeny/CI-MS4-LoveRugby) has given me tips on some of the elements on this site, including the review model and automated testing.

Lastly, I want to thank all Tutors at Code Institute for their patience; Jo, Sheryl, John, Sean, Igor, Alan, Rebecca, James, and all the rest that have had to put up with me!
