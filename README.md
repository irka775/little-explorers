# Little Explorers

Little Explorers is an e-commerce web application designed for customers looking to purchase high-quality children's clothing online.
**Disclaimer:** This is not a real store. The site is created for **learning purposes only** as part of a portfolio project.

This project is part of my portfolio, showcasing a full-featured online store with user authentication, product management, and secure payment integration.

Users can create accounts to manage their orders, while administrators have full write and delete access to all products and customer data.

You can view the deployed site [here](https://little-explorers-journey-34e4e4481594.herokuapp.com/).

![Mockup of live site on different devices](media/responsive.PNG)

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
      - [Epic 2: Products](#epic-2-products)
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
  - [Bugs](#bugs)
  - [Credits](#credits)
    - [Copyrights](#copyrights)
      - [Media](#media)
      - [Content](#content)
    - [Coding Tips and Tricks](#coding-tips-and-tricks)
    - [Acknowledgments](#acknowledgments)

## Project Overview

Little Explorers is an assignment project created for learning purposes, designed as part of a portfolio in full-stack software development. While it is a fictional e-commerce store, the functionality is built to simulate a real-world online shopping experience.

This project focuses on **e-commerce development** using the **Django framework**, allowing users to browse children's clothing, add items to their cart, and complete purchases with a secure payment system.


### Agile Workflow

![Kanban Board](media/screenshots/canban_board.PNG)

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

---


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

#### Business Model

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
- Newsletter Marketing: Registered users can **subscribe to receive promotional emails**, ensuring they stay updated on new collections and deals.
#### **User Experience Focus**
The website is designed to be:
- Easy to navigate, ensuring users can quickly find what they need.
- Mobile-friendly, allowing users to shop conveniently on any device.
- Secure & Trustworthy, integrating **secure payment processing** and **customer reviews** to build confidence.

**Little Explorers' mission** is to provide a seamless shopping experience where users(parents) can find stylish, comfortable, and affordable clothing for their children in just a few clicks.

---

####  Marketing

##### **Marketing Strategy**
For the **Little Explorers** e-commerce project, I have developed a **basic Facebook marketing strategy** to simulate how a real business would promote an online store. However, since this project is created for learning purposes and is not a real e-commerce site, I have set up a **fictional Facebook page** and captured a screenshot of it instead of managing an actual social media presence.
 
This site has a Facebook Business page with a link on the page footer. **Screenshot of the Fictional Facebook Page:**

 ![Facebook Page Screenshot](media/facebook_bussines_page.PNG) 

While this page is only a placeholder for learning purposes, in the future, a fully functional Facebook page could be implemented with more advanced social media marketing strategies like:
- Regular product updates and promotions to engage potential customers.  
- Customer interaction via comments, messages, and reviews to build trust.  
- Facebook Ads campaigns to increase visibility and drive traffic to the store. 


##### **Newsletter Subscription (Email Marketing)**
**Little Explorers**  allow users to subscribe to newsletters during registration. This simulates how an online store can engage with customers through **exclusive offers, product updates, and seasonal promotions**.

- Upon subscribing, users are get a confirmation message.   
- Subscribers receive promotional emails when new collections, discounts, or special events are launched.


#### **Subscription Form**
![Subscription Form](media/screenshots/subscribe_email.PNG)

#### **Subscription Confirmation Page**
![Subscription Confirmation Page](media/screenshots/subscribe.PNG)

#### **Subscription Success Message**
![Subscription Success Message](media/screenshots/unsubscribe.PNG)

#### **Future Marketing Plans (If the Project Expands)**
If **Little Explorers** grows into a real business, the marketing strategy could include:
- **A fully developed and active Facebook page** with real promotions.  
- **Expansion to Instagram & Pinterest** for better product showcasing.  
- **Google Ads & SEO optimization** to attract organic traffic.  
- **Loyalty programs and referral discounts** to increase repeat customers.  


---

#### Search Engine Optimisation

I have generated a sitemap.xml and robots.txt file which helps Google map the pages of the site.

I have also done some research on highest searched words in kids clothing retailing, and came up with this title and description:

#### **Meta-tags seo**
![Meta-tags seo](media/screenshots/meta_tags.PNG)

---

### Structure

Little Explorers is an e-commerce website specializing in kids' clothing and is designed with a user-friendly interface, allowing customers to seamlessly browse, shop, and manage their accounts with ease.The website is built using the Django framework, offering a secure and scalable e-commerce experience. It features a customized product management system, interactive user accounts, and a responsive design to ensure accessibility across all devices.
With intuitive navigation, dynamic filtering options, and secure checkout, Little Explorers provides a smooth and enjoyable shopping experience. Customers can also leave product reviews, manage their wishlists, and track their orders—all in one place.
For store administrators, the platform includes powerful management tools, allowing easy product, brand, order, and customer control. Additional store settings ensure that the shopping experience remains up to date and optimized.

#### Pages

##### **Accessible to All Users**
These pages are available to both **guests and logged-in users**.

- **Home** - The landing page , a welcome message, and a call-to-action button ("Discover More").
- **Products** - A **searchable and sortable** product listing page, where users can browse by category, name, or description.
- **Product Detail** - A dedicated page for each product, displaying images, size options, price, and product description.
- **Cart** - Displays all items added by the user, allowing quantity adjustments and product removal.
- **Checkout** - Users enter their shipping details and payment information to complete their order.
- **Order Confirmation** - Displays the order summary and payment success message.
- **Sign In & Sign Up** - Authentication pages for account registration and login.
- **Contact** - A contact form allowing users to send inquiries. Contact email and phone number are also displayed in the footer.
- **Reviews** - Users can view all product reviews submitted by other customers.
- **Subscribe & Unsubscribe** - Visitors can subscribe to and unsubscribe from email notifications.


##### **Accessible to Signed-In Users**
These features require users to be **logged in**.

- **My Account (Dashboard)** - Users can:
  - View order history.
  - Manage billing and shipping information.
  - Edit their profile details.
  - Access and manage their wishlist.
- **Wishlist** - Users can:
  - Add or remove products from their wishlist.
  - View saved items for future purchases.
- **Order Management** - Users can:
  - View past orders and their details.
  - Access receipts and tracking information.
- **Edit Account** - Users can:
  - Change their password.
  - Log out from all other active devices.
- **Reviews Management** - Users can:
  - Submit reviews for purchased products.
  - Edit or delete their own reviews.
- **Sign Out** - Logs the user out securely.
- **Delete Account** - Permanently removes the user's account and all associated data.


##### **Accessible to Admin Users**
These features are only available to **superusers (store owners/admins)**.

- **Product Management**
  - **Add Product** - Admins can add new clothing items.
  - **Edit Product** - Modify existing product details (name, description, price, images, categories).
  - **Delete Product** - Remove products from the store.
- **Brand Management**
  - **Add Brand** - Admins can introduce new brands.
  - **Manage Brands** - View, edit, or delete brand listings.
- **Order Management**
  - View and manage customer orders.
  - Update order status (e.g., **Processing, Shipped, Completed**).
- **User Management**
  - View user profiles.
  - Manage wishlist items and account settings if needed.
- **Store Settings**
  - Modify general store settings (branding, logo, etc.).
  - Configure shipping settings.
  - Update store policies and terms.
- **Site Error Pages**
  - **Custom 404 Page** - Displayed when a page is not found.
  - **Custom 500 Page** - Shown when an internal server error occurs.
  - **Custom 403 Page** - Access denied page for unauthorized actions.
  - **Custom 400 Page** - Bad request handling.


#### **Pages Provided by Django Allauth**
These pages are integrated from **Django Allauth**. Read more about **Allauth** [here](https://django-allauth.readthedocs.io/en/latest/).

- **Sign Up** - Register a new account.
- **Sign In** - Log in to an existing account.
- **Sign Out** - Logs the user out securely.
- **Password Reset** - Allows users to reset their password via email verification.
- **Email Verification Pages** - Ensures users confirm their email before accessing all features.


#### Technical Design

##### Code Structure

The **Little Explorers** project follows Django's **best practices**, organizing the code into multiple **apps**, each handling a specific part of the functionality.

- **Home** - Handles the main homepage and welcome content.
- **Products** - Manages **product listings, filtering, sorting, and product details**.
- **Bag (Cart)** - Implements the **shopping cart functionality**, allowing users to add and manage their selected items.
- **Checkout** - Manages the **order processing and payment integration**.
- **Profiles** - Handles **user accounts, order history, and wishlist**.
- **Reviews** - Implements the **user review system**, allowing customers to leave, edit, or delete reviews.
- **Store Settings** - Allows **administrators to configure store settings, shipping options, and site preferences**.


**Other Directories and Files**

- **static/** - Contains **CSS, JavaScript, and frontend assets** used for styling and interactivity.
- **media/** - Stores **uploaded product images** for local development (in production, these are stored externally).
- **store_settings/** - Manages store-level **configuration settings, shipping settings, and admin control options**.
- **templates/** - Holds the **HTML templates** used for rendering pages. This includes:
  - **auth templates** (Django Allauth).
  - **error pages** (400, 403, 404, 500).
  - **base templates and layout files**.
- **manage.py** - The main Python script for running the Django project.
- **custom_storages.py** - Configures **AWS S3 for static and media file storage**.
- **db.sqlite3** - The **local development database** (PostgreSQL is used in production).
- **env.py** - Stores **environment variables** securely.
- **.gitignore** - Prevents unnecessary files from being tracked in Git.
- **requirements.txt** - Lists all **dependencies** required for the project.
- **Procfile** - Required for **Heroku deployment**, specifying startup commands.
- **robots.txt & sitemap.xml** - Configured for **Search Engine Optimization (SEO)**.

##### Database

- **Development Database**: [SQLite](https://www.sqlite.org/index.html) is used for local testing.
- **Production Database**: [PostgreSQL](https://www.postgresql.org/) is used for better scalability and is hosted via **Heroku**.
  Both are relational databases and work well with the Django framework used for this project.

 **Security & Environmental Variables**

Sensitive data such as **API keys, database credentials, and payment gateway secrets** are **never stored in the codebase** and instead of that I have been created:
- `env.py` for local development.
- **Heroku Config Vars** in Heroku platform for Heroku development.


##### Data Models

The **Little Explorers** e-commerce platform utilizes a relational database structure, following Django ORM (Object-Relational Mapping).The following models have been used to populate the database and for the site to function as it should:

 **1. User & Profiles**
The UserProfile model extends Django’s built-in **User model**, storing **default shipping details** and **account preferences**. 
**User** - the built in Django User model, facilitates the users basic information.
**UserProfile** - the model storing the users product and order information. 

 **2. Products & Categories**
The Product model represents items available for sale, with categories and reviews linked to it.
**Category** - the category in which the product is place.
**Product** - the model for the product itself and its details.
**WishListItem** - the customer has the option to save an item, which will then appear in their wish list on the My StepUp page.

 **3. Reviews**
Customers can leave **product reviews** or **general site feedback**.
 **Review** - a model for users to give the product a rating and a review.

 **4. Shopping & Orders**
Orders contain **multiple line items**, and each product purchased is stored separately in **OrderLineItem**.
 **Order** - a users successful purchase leads to an instance of the Order model being created, storing delivery and user data.
 **OrderLineItem** - a model holding the product information for a single product, binding the product model together with the order.

 **5. Store Settings & Shipping**
Admin users manage store configurations, shipping options, and payment settings.

##### Schema of models

I used in **Little Explorers** e-commerce platform a **relational database structure** and below is a schema diagram representing the relationships between models.

 **Schema Diagram**
![Schema of models](erd_diagram.png)

 **Key Relationships & Explanation**

 **1. User & UserProfile**
- The UserProfile model extends Django’s built-in User model.
- It stores default shipping details, helping users complete orders faster.
- **Relationship:** UserProfile has a OneToOneField with User.

**2. Products & Categories**
- A Product belongs to a Category, allowing easy organization.
- Each Product can have multiple Reviews from customers.
- **Relationship:** Product has a ForeignKey to Category.

 **3. Reviews**
- Users can leave product reviews or site feedback.
- Reviews include a rating, comment, and creation date.
- **Relationship:** 
  - A Review is linked to both a User and a Product (if applicable).

 **4. Orders & OrderLineItems**
- When a customer places an Order, it contains multiple OrderLineItems.
- Each OrderLineItem stores product, quantity, and subtotal.
- **Relationships:**
  - Order has multiple OrderLineItems (OneToMany).
  - Each OrderLineItem is linked to a Product (ForeignKey).

 **5. Wishlist**
- Customers can save favorite products to their wishlist.
- **Relationships:**
  - Wishlist has a OneToOneField with User.
  - A Wishlist can contain multiple Products (ManyToMany).

 **6. Store Settings & Shipping**
- The StoreSettings model manages global store settings, branding, and payment options.
- ShippingSettings controls delivery costs and free shipping thresholds**.
- **Relationship:** ShippingSettings has a ForeignKey to StoreSettings.

 **7. Subscribers**
- Customers and guests can subscribe to the newsletter.
- **Relationships:**
  - A Subscriber can be linked to a User (OneToOne) or just an email.

This schema ensures that Little Explorers remains scalable, secure, and optimized for handling user interactions, product management, and orders.

---


### Scope - Epics and User Stories

The **Little Explorers** e-commerce platform is designed with a **user-centric approach**, ensuring an intuitive shopping experience. Below is a key **epics and user stories**, defining the functionality required for different types of users (customers, admins, and visitors).
Each epic represents a broad feature set, broken down into smaller, actionable user stories.

#### Epic 1: Project Setup & Configuration
 *As a developer, I want a well-configured development environment so that the project runs smoothly and is easy to maintain.*

####  **User Stories**
-  **Create a New Django Project** (#17)  
   Set up the initial Django project structure with best practices.
-  **Install Necessary Dependencies** (#18)  
   Ensure all required packages (Django, PostgreSQL, Stripe, etc.) are installed.
-  **Configure Database Settings** (#19)  
   Set up PostgreSQL for production and SQLite for local development.
-  **Set Up Environment Variables** (#20)  
   Secure sensitive information using `.env` files.
-  **Run Initial Tests** (#21)  
   Verify that the project runs without errors and initial tests pass.

####  **Acceptance Criteria**
- The Django project is successfully created and follows a structured architecture.
- All required dependencies are listed in requirements.txt and installed without issues.
- The database is configured for both development (SQLite) and production (PostgreSQL).
- Environment variables are set for security(e.g., API keys, database credentials).
- The application runs successfully, and initial tests pass without errors.


####  Epic 2: User Authentication & Profile Management
 *As a user, I want to securely create and manage my account so that I can access personalized features.*

####  **User Stories**
-  **User Registration and Authentication** (#1)  
   Users can sign up, log in, and reset passwords.  
- **User Registration and Shopping Experience for Little Explorers** (#15)  
   A seamless registration and shopping experience.

####  **Acceptance Criteria**
- Users can register and log in securely.
- Password recovery is available via email.
- Users can update their profile details.



####  Epic 3: Product Browsing & Search
 *As a user, I want to browse, search, and filter products so that I can easily find what I need.*

####  **User Stories**
-  **Product Catalog Browsing** (#2)  
   Users can explore product categories.
- **Product Search and Filter** (#3)  
   Users can search by name, category, or price.

####  **Acceptance Criteria**
- Products are categorized and searchable.
- Filtering and sorting options are available.



####  Epic 4: Shopping Cart & Checkout
 *As a user, I want to add items to my cart and proceed to checkout smoothly.*

####  **User Stories**
-  **Shopping Cart Functionality** (#4)  
   Users can add, remove, and update items in their cart.
-  **Secure Checkout and Payment** (#5)  
   Users can enter delivery details and complete payments.

####  **Acceptance Criteria**
- Items persist in the cart until checkout.
- Payment methods are secure.


#### Epic 5: Order Management & Payments
 *As a user, I want to view my order history and receive confirmation after making a purchase.*

####  **User Stories**
-  **Order Management (Admin)** (#7)  
   Admins can view, update, and manage orders.

####  **Acceptance Criteria**
- Users receive email confirmations for orders.
- Admins can process and update order status.


####  Epic 6: Wishlist & Reviews
 *As a user, I want to save products to my wishlist and leave reviews on products.*

####  **User Stories**
-  **Wishlist** (#23)  
   Users can save favorite items for later.
-  **Product Reviews and Ratings** (#11)  
   Users can submit and rate product reviews.
-  **Display Wishlist and Reviews in the Navigation Menu** (#25)  
   Wishlist and reviews are easily accessible.

####  **Acceptance Criteria**
- Wishlist items persist in user accounts.
- Users can submit, edit, and delete reviews.


####  Epic 7: Admin & Store Management
 *As an admin, I want to manage products, inventory, and settings efficiently.*

####  **User Stories**
-  **Product and Inventory Management (Admin)** (#6)  
   Admins can add, edit, and remove products.
-  **Admin Settings Panel for Customization** (#26)  
   Store settings can be adjusted.

####  **Acceptance Criteria**
- Admins can edit product details and stock levels.
- Admin dashboard provides clear data insights.


####  Epic 8: Mobile & User Experience Enhancements
 *As a user, I want the website to be responsive and accessible on all devices.*

####  **User Stories**
-  **Responsive Design for Mobile Devices** (#9)  
   The site adapts to different screen sizes.

#### **Acceptance Criteria**
- The website functions smoothly on mobile.
- UI elements resize dynamically.


#### Epic 9: Social & Email Integrations
 *As a user, I want to receive notifications and share products on social media.*

####  **User Stories**
-  **Social Media Integration** (#14)  
   Users can share products on social platforms.
-  **Email Notifications** (#8)  
  - Users receive updates about orders and promotions.

####  **Acceptance Criteria**
- Email notifications are triggered for key events.
- Social media links are available for sharing.(The Facebook link is created but currently directs to a screenshot of the store's Facebook page instead of a live profile.)

####  Epic 10: Documentation & Feedback
 *As a developer or user, I want clear documentation and feedback options.*

####  **User Stories**
-  **README Documentation for Little Explorers** (#16)  
  A structured README file explaining project features.
-  **Leave Feedback About the Website** (#24)  
  -Users can submit feedback to improve UX.

####  **Acceptance Criteria**
- README includes sections for setup, usage, and features.
- Users can provide feedback through a contact form or direct message.


####  Epic 11: Testing & Deployment
 *As a developer, I want to ensure the platform is stable and functional before release.*

#### **User Stories**
-  **Project Deployment** (#10)  
  Deploy the application to a live server.
-  **Add Unit Tests** (#22)  
   Implement unit tests to ensure system reliability.

#### **Acceptance Criteria**
- The project is deployed and accessible online.
- Automated tests cover critical functionalities.

---
### Skeleton

#### Wireframes

I created wireframes for some of the pages for both desktop and mobile versions to plan the layout and structure of the site effectively.

 **Wireframe of Home Page on Desktop**![Wireframe of Home Page on Desktop](media/screenshots/wireframes/home_desktop.PNG)
 **Wireframe of Home Page on Mobile**![Wireframe of Home Page on Mobile](media/screenshots/wireframes/home_mobile.PNG)
 **Wireframe of Products on Desktop**![Wireframe of Products on Desktop](media/screenshots/wireframes/Products_desktop.PNG)
 **Wireframe of Products  on Mobile**![Wireframe of Products on Mobile](media/screenshots/wireframes/products_mobile.PNG)
 **Wireframe of Sign in on Desktop**![Wireframe of Sign in on Desktop](media/screenshots/wireframes/SignIn_Desktop.PNG)
 **Wireframe of Sign in on Mobile**![Wireframe of Sign in on Mobile](media/screenshots/wireframes/signin_mobile.PNG)


### Surface

#### Colors

The **Little Explorers** website uses a vibrant and playful color palette to reflect the joy and creativity of children's fashion. The combination of green, blue, black, and white provides a fresh, clean, and inviting design.

![Colors](media/screenshots/colors.PNG)  
(*Color palette generated at [imagecolorpicker.com](https://imagecolorpicker.com)*)

##### **Primary Colors**
-  **Green (#2FAA43)** – Used for the header background, representing growth, energy, and a nature-inspired theme.
-  **Blue (#3498DB)** – Used for navigation elements, adding a cool and friendly tone to the design.
-  **Black (#000000)** – Used for text and important contrast elements, ensuring readability.
-  **White (#FFFFFF)** – Used for backgrounds and text, keeping the interface clean and modern.

##### **Accent Colors**
-  **Orange (#F39C12)** – Used for small highlights or action elements, adding warmth and contrast.
-  **Red (#E74C3C)** – Used for important actions, such as the unsubscribe button.

##### **Text Colors**
- The main text color is **black (#000000)**, ensuring strong readability on light backgrounds.
- Some elements use **white text (#FFFFFF)** when displayed on dark or colorful backgrounds for better contrast.
- In the future, I may experiment with **softer shades** to enhance the reading experience, especially for longer texts.

##### **Design Inspiration**
The color scheme was chosen to create a fun, fresh, and engaging experience for customers browsing children's clothing. The combination of green and blue reflects playfulness and comfort, while the black and white elements ensure easy readability and a modern aesthetic.

##### **Future Improvements**
As a student, I am aware that the current color palette could be further optimized for better usability, branding, and accessibility. When I decide to extend and scale this project, I will experiment with alternative color schemes to improve contrast and readability and ensure that colors meet accessibility standards for visually impaired users.




#### Design Choices


The Little Explorers website I was designed with a playful yet clean aesthetic, incorporating soft transitions, rounded edges, and engaging colors to create a welcoming experience for users browsing children's clothing.

**Navbar & Header**
The navbar is designed to be highly functional and visually appealing, maintaining a fixed position at the top of the page for easy navigation. The background features a gradient green-blue blend, making the site feel vibrant and lively.

- The navbar includes icons for user accounts, cart, and categories, ensuring quick access to important sections.
- A search bar allows users to find products efficiently.
- The header features a full-screen hero image with an inviting message and a call-to-action button for exploring products.

![Navbar](media/screenshots/navbar.PNG)


 **Buttons & UI Elements**
Buttons across the site are designed to be eye-catching and functional, enhancing usability and user engagement.

- Primary buttons use a linear-gradient CSS effect to create a glossy finish.
- The "Discover More" button on the homepage stands out with a bold black background for contrast.
- Admin-related buttons (e.g., for managing products) are styled differently to clearly distinguish them from user-facing elements.
- The Unsubscribe button is colored red, indicating a critical action.
- The Subscribe button is styled in a green color, representing a positive action for users who want to stay updated.
  Below are some screenshots showcasing the design choices implemented throughout the website:
 ![Button Elements](media/screenshots/button1.PNG)
 ![Button Elements](media/screenshots/button2.PNG)

 **Typography & Readability**
- The site primarily uses black text  for readability.
- White text is used on dark backgrounds to maintain contrast.
- Fonts are chosen for a modern and clean look, ensuring that product descriptions and labels are easy to read.

 **For future Improvements**
 - I recognize that design choices can always be improved. In the future, I plan to refine the color contrast for better accessibility and implement a dynamic navbar that fades or adjusts upon scrolling and thinking to enhance button styles for even better user engagement.

#### Typography

The typography on Little Explorers I was carefully chosen to ensure clarity, readability, and a modern,simple feel . The primary font used across the website is Lato (Google Font), with Helvetica Neue as a fallback for consistency and Comic Sans MS (Used in the Banner), applied to the announcement banner for a fun and playful touch.

 **Font Usage Across the Homepage**
- **Navigation Bar & Menu** → *Lato (Google Font)*
- **Banner** → *Comic Sans MS', 'Arial', sans-serif;* (Google Font)*
- **Main Heading ("Welcome to our store")** → *Lato (Bold variant)*
- **Body Text & Buttons (Discover More, Unsubscribe, etc.)** → *Lato (Regular & Semi-Bold)*
- **Fallback Font for Safety** → *Helvetica Neue*

To better visualize the typography choices, see the screenshot of the homepage:

- ![Typography in Action1](media/screenshots/baner.PNG)
- ![Typography in Action2](media/screenshots/typography1.PNG)
- ![Typography in Action3](media/screenshots/typography2.PNG)

---

## Existing Features

The Little Explorers e-commerce platform is designed to provide a seamless shopping experience for users while offering robust management tools for administrators. Below is a breakdown of the key features:

### **Feature 1: Navigation Bar**
The navigation bar provides quick access to all essential sections of the website and remains accessible at all times.

 **Implemented Features**
- Brand Logo & Name: Displays "Little Explorers", enhancing brand identity.
- User Account Dropdown:
  - Allows users to log in, register, or access their profile. 
  - Shows the current logged-in user’s name. 
- Shopping Cart Icon:
  - Displays the cart total for easy tracking. 
  - Redirects users to the shopping cart page. 
- Dropdown Menus:
  - All Clothes – Lists all clothing categories. 
  - Categories – Organizes products by category. 
  - Wishlist Access: A quick link to the wishlist page for easy access to saved products. 
- Search Bar: Users can search for products by name or description. 
- Announcement Banner: Displays "FREE Delivery on orders over 51.00 EUR!" with an eye-catching green highlight. 

 **User Stories Covered**
  - **#1**:As a user, I want to be able to register and log into my account so that I can manage my personal details, view my orders, and save my preferences.
  - **#2**: As a user, I want to be able to browse a catalog of products so that I can explore different clothing options for my children.
  - **#3**: As a user, I want to filter and search for specific items so that I can easily find clothes based on size, color, or category.
  - **#4**: As a user, I want to add items to my shopping cart so that I can prepare my purchase.
  - **#23**: As a customer, I want to add products to a wishlist, so that I can save my favorite items for later and easily access them when I'm ready to purchase.


#### **Screenshots**
**Navigation Bar Desktop**![Navigation Bar Desktop](media/existing_features/navbar_desctop.PNG)
**Navigation Bar Mobile**![Navigation Bar Mobile](media/existing_features/navbar_mobile.PNG)


### **Feature 2: Body (Homepage & Content Sections)**
The main body presents featured products, promotions, and call-to-action elements.

 **Implemented Features**
- Hero Section:
  - A large welcome banner with the text: "Welcome to our store"
  - Call-to-action button: "Discover More", redirecting users to explore the store. 
- Dynamic Product Display:
  - Featured products and categories update dynamically.
  - Large, high-quality images showcasing children’s clothing. 
- User-Friendly Interface:
  - Minimalist design focusing on clarity and ease of use.
  - High contrast text for readability.
  
 **User Stories Covered**
 - **#2**: As a user, I want to be able to browse a catalog of products so that I can explore different clothing options for my children.

#### **Screenshots**
**Homepage Body desktop**![Homepage Body desktop](media/existing_features/homepage_desktop.PNG)
**Homepage Body Mobile**![Homepage Body Mobile](media/existing_features/homepage_mobile.PNG)


### **Feature 3: Footer**
The footer provides quick links, social media access, and customer support contact information.

 **Implemented Features**
- Subscription Section:
  - A  "Unsubscribe/Subscribe" button allowing users to manage their newsletter preferences. 
- Social Media Integration:
  - A "Follow us on Facebook" link (displays a screenshot instead of a direct link). 
- Customer Support Information:
  - Displays contact email: IrishRoyals@example.com (fake email).
  - Shows customer service phone number: *+353000000000*.
  - N.B. It is just example for contact email and customer phone number.
- Consistent Design:
  - The footer maintains a green and blue gradient to align with the site's overall theme.
  - Ensures a clear, readable font for user convenience.

  **User Stories Covered**
- **#8**: As a user, I want to receive order confirmation and shipping notifications via email so that I am informed about the status of my purchase.
- **#14**: As a user, I want to share products on social media so that I can recommend them to friends and family.

#### **Screenshots**
**Footer desktop**![Footer desktop](media/existing_features/footer_desctop.PNG)
**Footer Mobile**![Footer Mobile](media/existing_features/footer_mobile.PNG)


### **Feature 4: User Registration and Authentication**
The site allows users to create an account, log in, and manage their profiles.

 **Implemented Features**
- User Registration:Users can create an account using their email and password.
- User Login & Logout:Users can securely log in and out of their accounts.
- Password Reset: Users can reset their password if they forget it.
- Profile Management: Users can update their personal details.
- Admin Access: Admin users have additional privileges, including product and order management.

 **User Stories Covered**
- **#1** - As a user, I want to be able to register and log into my account so that I can manage my personal details, view my orders, and save my preferences.  
- **#15** - As a shoper or site user I want to buy children's clothing from "Little Explorers,so that I can shop for kids in a convenient way.  

#### **Screenshots**
**User Authentication desktop**![User Authentication desktop](media/existing_features/registration_desktop.PNG)
**User Authentication Mobile**![User Authentication Mobile](media/existing_features/registration_mobile.PNG)



### **Feature 5: Product Catalog Browsing**
Users can explore a well-structured list of children’s clothing items categorized for easy navigation.

 **Implemented Features**
- Product pages display detailed descriptions and images.
- Product Categories: Products are categorized for easy browsing.
- Search Functionality: Users can search for specific products.
- Sorting & Filtering: Users can filter products by price, category, and availability.
- Responsive Design: The layout adapts to mobile, tablet, and desktop screens.

 **User Stories Covered**
 **#2** - As a user, I want to be able to browse a catalog of products so that I can explore different clothing options for my children.  
 **#3** - As a user, I want to filter and search for specific items so that I can easily find clothes based on size, color, or category. 
 **#9** - As a user, I want the website to be mobile-friendly so that I can browse and shop on any device. 


### **Screenshots**
**Product List desktop**![Product List desktop](media/existing_features/productlist_desktop.PNG)
**Product List Mobile**![Product List Mobile](media/existing_features/productlist_mobile.PNG)


### **Feature 6: Product Search and Filtering**
Users can quickly find the products they need through search and filtering options.

 **Implemented Features**
- Search Bar: Users can enter keywords to find specific products.
- Filtering Options: Products can be filtered by category, price range, and availability.
- Sorting: Users can sort products alphabetically, by price, or by popularity.

 **User Stories Covered**
 **#3** -  As a user, I want to filter and search for specific items so that I can easily find clothes based on size, color, or category. 

  
#### **Screenshots**
**Search Products desktop**![Search Products desktop](media/existing_features/search_desktop.PNG)
**Search Products Mobile**![Search Products Mobile](media/existing_features/search_mobile.PNG)

### **Feature 7: Wishlist**
Users can *save products* they are interested in purchasing later.

 **Implemented Features**
- Add to Wishlist: Users can save products for later.
- View Wishlist: A dedicated wishlist page displays saved items.
- Remove from Wishlist: Users can remove unwanted items.

 **User Stories Covered**
  **#23** - As a customer, I want to add products to a wishlist, so that I can save my favorite items for later and easily access them when I'm ready to purchase. 


#### **Screenshots**
**Wishlist desktop**![Wishlist desktop](media/existing_features/wishlist_desktop.PNG)
**Wishlist Mobile**![Wishlist Mobile](media/existing_features/wishlist_mobile.PNG)
**Wishlist notification**![Wishlist notification](media/existing_features/wishlist_notification.PNG)


###  **Feature 7: Shopping Cart**
The shopping cart allows users to manage their selected items before checkout.

 **Implemented Features**
- Add to Cart: Users can add products to their cart.
- View Cart: A dedicated cart page shows selected items and total cost.
- Remove Items: Users can remove unwanted products from their cart.
- Cart Total Display: The cart icon updates dynamically to show the number of items.

 **User Stories Covered**
  **#4** - As a user, I want to add items to my shopping cart so that I can prepare my purchase.

#### **Screenshots**
**Shopping Cart Desktop**![Shopping Cart desktop](media/existing_features/shopingbag_desktop.PNG)
**Shopping Cart Mobile**![Shopping Cart Mobile](media/existing_features/shopingbag_mobile.PNG)
**Shopping Cart Notification**![Shopping Cart  Notification](media/existing_features/shopingbag_notification.PNG)


### **Feature 8: Secure Checkout and Payment**
A seamless and secure checkout process ensures safe transactions.

**Implemented Features**
- Delivery Information: Users must provide delivery details before placing an order.
- Payment Options: Users can pay via Stripe, PayPal, or Cash on Delivery.
- Order Summary: Users can review their order before payment.
- Payment Confirmation: A success message is displayed after a successful purchase.

 **User Stories Covered**
 **#5** - As a user, I want to securely checkout and make payments so that I can complete my purchase with ease and confidence. 

#### **Screenshots**
**Checkout Process Desktop**![Checkout Process desktop](media/existing_features/checkoutprocess_desctop.PNG)
**Checkout Process Mobile**![Checkout Process Mobile](media/existing_features/checkoutprocess_mobile.PNG)
**Checkout confirmation Desktop**![Checkout confirmation desktop](media/existing_features/checkout_desktop.PNG)
**Checkout confirmation Mobile**![Checkout confirmation Mobile](media/existing_features/checkout_mobile.PNG)


## **Feature 8: Product Reviews and Ratings**
Users can share feedback and rate products.

### **Implemented Features**
- Leave a Review: Users can submit a review after purchasing a product.
- Rate a Product: Users can rate products from 1 to 5 stars.
- View Reviews: All submitted reviews are visible on product pages.

 **User Stories Covered**
 **#11** -As a user, I want to leave reviews for products I have purchased so that I can share my feedback with other customers.  

#### **Screenshots**
**Product Reviews Desktop**![Product Reviews desktop](media/existing_features/review_desktop.PNG)
**Product Reviews Mobile**![Product Reviews Mobile](media/existing_features/review_mobile.PNG)

### **Feature 9: Responsive Design for Mobile Devices**
The website is fully responsive, ensuring a smooth browsing experience across all devices.

**Implemented Features**
- Optimized layout for mobile, tablet, and desktop. 
- Buttons and navigation adjust dynamically for touch-friendly interactions.

**User Stories Covered**
 **#9** -As a user, I want the website to be mobile-friendly so that I can browse and shop on any device.


#### **Screenshots**
**Mobile view**![Mobile view](media/existing_features/responsive_mobile.PNG)

**Tablet view**![Tablet view](media/existing_features/responsive_ipad.PNG) 

**Desktop view**![Desktop view](media/existing_features/responsive_desktop.PNG)




### **Feature 10: Email Notifications**
Users receive email updates regarding account activity and orders.

 **Implemented Features**
- Order confirmation emails 
- Subscription confirmation for newsletters.
- Admin notifications for new orders.

**User Stories Covered**
 **#8** -As a user, I want to receive order confirmation and shipping notifications via email so that I am informed about the status of my purchase.

 #### **Screenshot**
 **Email Notifications**![Email Notifications ](media/existing_features/review_desktop.PNG)



### **Feature 11: Product and Inventory Management**
Admins can manage product listings and inventory from the admin panel.
Press PrtScn (Print Screen) 
 **Implemented Features**
- Add, edit, or remove products from the store. 
- Stock management with real-time inventory updates.

**User Stories Covered**
 **#6** -As an admin, I want to manage products, categories so that I can keep the product listings up-to-date.

#### **Screenshots**
 **Admin Product Management desktop**![Admin Product Management desktop](media/existing_features/management_desktop.PNG)
 **Admin Product Management mobile**![Admin Product Management mobile](media/existing_features/management_mobile.PNG)


### **Feature 12: Order Management**
Admins can track and manage orders efficiently.

 **Implemented Features**
- View, process, and update orders. 
- Customers receive email updates on order status.

**User Stories Covered**
 **#7** -As an admin, I want to be able to view and manage customer orders so that I can ensure that orders are processed and shipped in a timely manner.


#### **Screenshots**
 **Admin Order Management**![Admin Order Management](media/existing_features/order_management.PNG)



### **Feature 13: Admin Settings Panel for Customization**
The admin dashboard allows customization of store settings.

 **Implemented Features**
- Update store name, logo, and contact details. 
- Enable or disable customer reviews and payment methods.

**User Stories Covered**
 **#26** -The Admin Settings Panel should be accessible only to admin users.
Admin should be able to change the store name from the settings page.
Admin should be able to upload a new logo for the website.
Admin should be able to configure payment options (e.g., enable/disable Stripe, PayPal, Cash on Delivery).
Admin should be able to set the contact email and phone number for customer support.
Admin should be able to toggle site-wide maintenance mode (e.g., enable/disable site for updates).
Admin should be able to configure the currency used in the store.
Admin should be able to enable or disable user reviews and ratings.
Changes made in the settings should be saved and immediately reflected on the site.
A success message should be displayed after saving the settings.

#### **Screenshots**
 **Admin Settings Panel for Customization desktop**![Admin Settings Panel for Customization desktop](media/existing_features/settingspannel_desktop.PNG)
 **Admin Settings Panel for Customization mobile**![Admin Settings Panel for Customization mobile](media/existing_features/settingspanel_mobile.PNG)




### **Feature 14: Social Media Integration**
Users can connect with Little Explorers on social media platforms.

 **Implemented Features**
- Social media links for Facebook and other platforms. 
- A screenshot of the Facebook page instead of a direct link.

**User Stories Covered**
 **#14** -As a user, I want to share products on social media so that I can recommend them to friends and family.

#### **Screenshots**
 **Social Media Integration**![Social Media Integration](media/existing_features/socialmedia.PNG)
 **Social Media Facebook page**![Social Media Facebook page](media/facebook_bussines_page.PNG)



### **Feature 15: Unit Tests & Project Deployment**
The website has unit tests to ensure reliability and is fully deployed.

 **Implemented Features**
- Unit tests for core functionalitie
- Live deployment of the project 

**User Stories Covered**
 **#10** -As a developer, I want to deploy the application to a live server so that users can access and use the platform publicly.
 **#22** -Add comprehensive unit tests to validate the functionality of the product-related views in the Django application. These tests aim to ensure that all key features, such as displaying products, filtering, sorting, and CRUD operations, work as expected. Testing also includes verifying permissions for superusers and preventing unauthorized actions.


## Features Yet to Implement

While Little Explorers already offers a robust and user-friendly shopping experience, several features are planned for future development to enhance usability and functionality I have a lot of ideas in mind, but here are some of them:

 1.Sorting enhancements: Sorting by most viewed, best-selling, and customer reviews.

 2.Product Recommendations,like "Recommended for You" section based on user behavior and "Customers Also Bought" feature on the product detail page.

 3.Live Chat for Customer Support to assist customers in real-time.


 4.Order Tracking System allowing users to monitor their shipment status.

 5.Exploring the possibility of a dedicated iOS and Android app.


## Technologies Used

### Languages
The following programming languages were used in the development of the project 'Little Explorers':

- **[Python 3.10.3](https://www.python.org/)** – Used as the core backend language, handling server-side logic, database interactions, and business processes.  
- **[HTML5](https://en.wikipedia.org/wiki/HTML5)** – The foundation of all web pages, structuring the content and layout of the site.  
- **[CSS3](https://en.wikipedia.org/wiki/CSS)** – Applied for styling, responsiveness, and enhancing the visual appeal of the site.  
- **[JavaScript](https://en.wikipedia.org/wiki/JavaScript)** – Enables interactive features, improves user experience, and enhances frontend functionality.  


### Frameworks, Libraries and Other Resources

The **Little Explorers** project was developed using a combination of powerful frameworks, libraries, and tools to ensure efficiency and responsiveness.

 **Backend Framework**
- **[Django version 5.1.2](https://www.djangoproject.com/)** – The core framework used for backend development, enabling a structured, secure, and scalable web application.

 **Frontend Technologies**
- **[Bootstrap 5.0.2](https://getbootstrap.com/)** – Utilized as the primary CSS framework to enhance styling consistency and mobile responsiveness.
- **[JQuery](https://jquery.com/)** – A JavaScript library used to simplify DOM manipulation and reduce code complexity.
- **[Font Awesome](https://fontawesome.com/)** – Provides all icons used throughout the site for a modern and clean UI.
- **[Google Fonts](https://fonts.google.com/)** – Used for typography to enhance readability and branding consistency.

 **External Services & Integrations**
- **[Facebook Pages](https://www.facebook.com/pages/create/?ref_type=site_footer)** – Used to create the business page that is linked on the site.wich external sources and integration i have been used for email
- **[Email & Subscription System,Django Allauth](https://django-allauth.readthedocs.io/)** – Handles user authentication, email verification, and password reset functionalities.  
- **[Stripe](https://stripe.com/)** – Securely processes payments and handles webhook responses for transactions.

 **Version Control & Development**
- **[Git](https://git-scm.com/)** – Used for version control, ensuring efficient project tracking and collaboration.
- **[GitHub](https://github.com/)** – Serves as the remote repository, where all code and branches are committed and stored.
- **[Gitpod](https://gitpod.io/)** – The cloud-based IDE used for coding, testing, and debugging the application.

 **Deployment & Hosting**
- **[Heroku](https://www.heroku.com/)** – The application is deployed on Heroku, ensuring accessibility and uptime.
- **[AWS S3 Bucket](https://aws.amazon.com/s3/)** – Used to store and serve static files (CSS, JavaScript) and media content (product images, user uploads).

 **Design & Documentation**
- **[Balsamiq Wireframes](https://balsamiq.com/wireframes/)** – Utilized to design wireframe mockups of the site layout. 
- **[Lucidchart](https://lucid.co/product/lucidchart)** – Used to create a visual schema of the project's data models.

## Testing

I have reviewed my project thoroughly and decided to evaluate it using both manual testing and automated testing to ensure all functionalities work as expected.

### Manual Testing
Manual testing was performed to verify that the core features align with the user stories and function as intended and can be viewed [here](MANUAL_TESTING.md).

### Automated Testing
I conducted automated tests for my application as part of the project to ensure functionality, performance, and security. The automated testing phase of the Little Explorers project was successfully conducted using pytest, covering various functional aspects of the application.The tests are listed below:
- **Bag Tests: 6 tests passed** – Verified the functionality of adding, removing, and adjusting products in the shopping bag.![Bag test pass](media/screenshots/unitest/bag_tests_pass.PNG)
- **Checkout Tests: 7 tests passed** – Ensured the checkout process works correctly with authenticated and unauthenticated users.![checkout test pass](media/screenshots/unitest/checkout_tests_pass.PNG)
- **Home Tests: 1 test passed** – Confirmed that the homepage loads properly and critical components function as expected.![home  test pass](media/screenshots/unitest/home_tests_pass.PNG)
- **Profiles Tests: 5 tests passed** – Checked profile authentication, order history accessibility, and profile updates.![profiles  test pass](media/screenshots/unitest/profiles_tests_pass.PNG)
- **Reviews Tests: 7 tests passed** – Validated review creation, editing, and listing functionalities.![review  test pass](media/screenshots/unitest/reviews_tests_pass.PNG)
- **Store Settings Tests: 16 tests passed** – Ensured correct behavior in subscription, password change, and store settings features.![store settings app test pass](media/screenshots/unitest/store_settings_tests_pass.PNG)
- **Overall Total: 42 tests passed successfully**![all tests pass](media/screenshots/unitest/all_tests_passed.PNG)

- All 42 automated tests passed successfully, demonstrating the robustness of the implemented functionalities.
- A few warnings were noted, mainly due to Django version updates (e.g., changes in URLField scheme from HTTP to HTTPS). These do not affect the core functionalities but will need to be addressed in future updates.
- Performance optimizations, such as lazy loading for images and checkout speed improvements, were implemented to enhance user experience.

## Other Services

### Stripe

Stripe was used as the payment gateway for processing transactions securely.

 **Setup Process**
1. Create an account at **[Stripe](https://stripe.com/)**.
2. Go to the **Developers** section and find your **API keys**.
3. Add the **publishable** and **secret keys** to your environment variables (both: in your development environment  and in Heroku for production).

 **Webhooks Integration**
To ensure payments are processed correctly and to make sure payments did not fail due to web errors, **webhooks** were set up:
1. Go to **Webhooks** in the Stripe dashboard.
2. Create an **endpoint** with the URL you send your webhooks to, 
in this case, the url is https://[https://little-explorers-journey-34e4e4481594.herokuapp.com/] 
3. Add webhook events like:
   - `payment_intent.succeeded` (successful payment)
   - `payment_intent.payment_failed` (failed payment)
4. Stripe will automatically send payment updates to the backend.


## Deployment

### **Forking the GitHub Repository**
To 'fork' or create a copy of this repository in your **own GitHub account**, follow these steps:

1. Log in to your **GitHub account** and find the relevant repository.
2. Click the **"Fork"** button in the top right corner.
3. You now have a **forked copy** in your GitHub account.

### **Making a Local Clone**

To clone this repository to your local machine:

1. Log in to your GitHub account and navigate to therelevant repository.
2. Click the "Code" button next to "Add file".
3. Copy the HTTPS clone URL.
4. Open Git Bash or your terminal.
5. Navigate to the directory where you want to store the project.
6. In your IDE's terminal run the following command:
   ```sh
   git clone <paste_copied_URL_here>
7. Press Enter, and the repository will be cloned locally.

### Heroku
This application is **deployed using Heroku**. Follow these steps:

**1. Create a Heroku Account & App**
1. Sign up or log in at **[Heroku](https://www.heroku.com/)**.
2. Click **"Create New App"**.
3. Choose a **unique app name** and select your **region**.
4. Click **"Create app"**.

**2. Configure Settings**
1. Navigate to the **"Settings"** tab.
2. Under **Config Vars**, add your **environment variables** (e.g., API keys, database credentials, etc.).
3. Scroll down to **Buildpacks**, and add:
   - **Python**
   - **Node.js** (if needed for static files).

**3. Connect to GitHub & Deploy**
1. Go to the **"Deploy"** tab.
2. Under **Deployment method**, choose **GitHub**.
3. Connect to your GitHub repository by **searching for the repository name** and selecting it. Enter your repository name and click on it when it shows below
4. Choose the **branch** you want to deploy (e.g., `main` or `master`).
5. Click **"Deploy Branch"** to manually deploy, or enable **Automatic Deploys** to keep the app updated.
6. Wait for the deployment process to complete. Your app is now **live on Heroku**!


### AWS S3
To host **static (CSS & JavaScript) and media files**, AWS S3 was used.
The steps to take are:

**1. Create an AWS Account & IAM User**
1. Go to **[AWS](https://aws.amazon.com/)** and sign up or log in.
2. Navigate to **IAM (Identity & Access Management)**.
3. Create a **new user** and assign the **AmazonS3FullAccess** policy.
4. Copy and store the **AWS Access Key ID** and **Secret Access Key**  as config vars to your workspace and deployment environment

**2. Create an S3 Bucket**
1. Open the **AWS S3** service.
2. Click **"Create Bucket"** and enter a **unique bucket name**.
3. Choose a **region** that matches your Heroku app.
4. Enable **public access** so users can access static and media files.
5. Click **"Create Bucket"**.

**3. Configure Django to Use AWS S3**
1. Add the **AWS credentials** to your environment variables:
   ```sh
   AWS_ACCESS_KEY_ID=<your_access_key>
   AWS_SECRET_ACCESS_KEY=<your_secret_key>
   AWS_STORAGE_BUCKET_NAME=<your_bucket_name>


## Performance

Performance was tested using Google Chrome's Lighthouse tool in DevTools built into the browser. The performance tests can be viewed [here](PERFORMANCE.md).

## Validation

Thourough validation of all code was made without errors. The results can be viewed [here](VALIDATION.md).

## Bugs

Here are a few of the bugs found during the testing phase:

- **Bug** While working on performance optimization for my project, I discovered several issues, including large images slowing mobile load times, JavaScript delays affecting rendering, and checkout & authentication scripts causing lags. Additionally, search, order history, and the admin panel were resource-heavy, impacting efficiency.

To address these, I will implement image optimization (WebP & lazy loading), JavaScript deferment, script optimizations for checkout & login, search pagination, and remove unnecessary admin panel scripts to enhance overall performance.
_Fix_ - No fix as of now

- **Bug**  When sent a password through the Django Allauth service, the link sent is http and not https. A warning by stripe in the terminal that payments for production only works with https is issued. This doesn't affect this site as the payments are for testing purposes, but needs to be investigated further in the future
_Fix_ - No fix as of now

- **Bug** The  product images were not displaying because the necessary AWS S3 storage settings were missing.
_Fix_ - adding the correct STORAGES configuration in Django settings, ensuring that uploaded media files were properly stored and served from Amazon S3

There may still be some undiscovered bugs in the project, as no software is entirely bug-free. However, based on my work and testing, the project currently functions well.

## Credits

### Copyrights

#### Media

Images of the products and the site background are all from [Pixabay](https://pixabay.com//) and [Google images](https://www.google.com//)

Images for favicons are from [Favicons](https://icons8.com/icons/set/favicon)

#### Content

 Since I do not have original product data, I was influenced by several key sources:  

 **Boutique Ado by Code Institute** – This project served as a foundational guide, helping me understand the structure and functionality of a Django-based eCommerce platform. It provided valuable insights into best practices for building an online store.  

 **Existing Kids' Clothing eShops** – I have referenced product details, descriptions, and inspiration from well-known kids' clothing retailers.
 The following sources were referenced for product descriptions, pricing models, and fashion trends:  
- **[Next Ireland - Kids](https://www.next.ie/en/shop/gender-babyboys-gender-babygirls-gender-boys-gender-girls)** – A popular choice for stylish and comfortable kids' wear.  
- **[Mothercare Ireland](https://www.mothercare.ie/)** – Well-known for baby & children's clothing, accessories, and essentials.  
- **[Dunnes Stores - Kids](https://www.dunnesstores.com/c/kids)** – A go-to Irish retailer for affordable and high-quality kids' fashion.  

 **ChatGPT for Product Ideas** – To generate product listings and descriptions, I sought assistance from ChatGPT, which provided creative ideas and suggestions for structuring product information effectively.  
 
### Coding Tips and Tricks
Throughout the development of Little Explorers, I encountered various coding challenges and found useful resources that helped me build and improve the project. These are tips that have helped me along the way for this project:

**Code Institute Boutique Ado project**

**Distribute navbar items evenly:**
https://stackoverflow.com/questions/32140607/horizontal-list-that-evenly-divides-remaining-space-via-css/32140682

**Split list into li items from model:**
https://stackoverflow.com/questions/8317537/django-templates-split-string-to-array


**Title in Django template**
https://stackoverflow.com/questions/14268342/make-the-first-letter-uppercase-inside-a-django-template


**Raise error in model form method**
https://docs.djangoproject.com/en/4.0/ref/forms/validation/

**Parseint JQuery:**
https://stackoverflow.com/questions/16269385/jquery-adding-2-numbers-from-input-fields


**Scroll incl for window width**
https://stackoverflow.com/questions/7715124/do-something-if-screen-width-is-less-than-960-px

**Looping, zip, lists in view and template:**
https://stackoverflow.com/questions/12684128/looping-through-two-objects-in-a-django-template

**Item at certain position in object from template:**
https://stackoverflow.com/questions/4286461/django-templates-first-element-of-a-list

**Footer:**
https://radu.link/make-footer-stay-bottom-page-bootstrap/

**Removing navbar transitions:**
https://stackoverflow.com/questions/13119912/disable-bootstraps-collapse-open-close-animation



## **Acknowledgments**

The development of *Little Explorers* has been an incredible journey, filled with challenges, learning, and growth. I am deeply grateful to everyone who supported, guided, and inspired me throughout this project. I would like to extend my heartfelt thanks to the following:

1. **My Husband**  
   Your unwavering support, encouragement, and belief in my abilities kept me motivated even during the most challenging moments. Thank you for standing by me and cheering me on every step of the way.

2. **Laura_ci (Cohort Facilitator)**  
   Thank you for your invaluable guidance on structuring clear and professional README documentation. Your advice helped me create a well-organized and informative project presentation, ensuring that every detail was communicated effectively.

3. **The Code Institute Tutors**  
   I am truly grateful to all the tutors at Code Institute for their patience, dedication, and willingness to assist whenever I encountered difficulties. Your insights and support made a significant difference in overcoming obstacles and improving my project.

4. **Fellow Students at Code Institute**  
   A special thank you to my peers for their continuous encouragement, collaboration, and exchange of ideas. Your feedback and shared experiences made this journey even more enriching.

5. **Project Inspiration – [StepUp](https://github.com/johnvenkiah/CI_PP5_John_Venkiah)**  
   The *StepUp* project served as a valuable template for structuring my README documentation, providing clear and effective insights into organizing content logically and professionally. Thank you, John Venkiah, for sharing your work and inspiring others.

6. **The Entire Code Institute Community**  
   From the course content to the community discussions, the support provided by the Code Institute team has been truly exceptional. Thank you for creating an environment that fosters growth, creativity, and success.

---

The journey of building *Little Explorers* has been both challenging and rewarding, and it would not have been possible without the incredible people mentioned above. Thank you all for your guidance, support, and inspiration!

