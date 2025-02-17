#  Manual Testing - Little Explorers

##  Table of Contents
1. [Overview](#overview)
2. [Home Page](#home-page)
   - [User Story](#user-story-1)
   - [Test Cases](#test-cases-1)
   - [Results](#results-1)
3. [Product Catalog & Search](#product-catalog--search)
   - [User Story](#user-story-2)
   - [Test Cases](#test-cases-2)
   - [Results](#results-2)
4. [Shopping Cart & Checkout](#shopping-cart--checkout)
   - [User Story](#user-story-3)
   - [Test Cases](#test-cases-3)
   - [Results](#results-3)
5. [User Authentication & Account Management](#user-authentication--account-management)
   - [User Story](#user-story-4)
   - [Test Cases](#test-cases-4)
   - [Results](#results-4)
6. [Order Management & Notifications](#order-management--notifications)
   - [User Story](#user-story-5)
   - [Test Cases](#test-cases-5)
   - [Results](#results-5)
7. [Admin Panel & Store Management](#admin-panel--store-management)
   - [User Story](#user-story-6)
   - [Test Cases](#test-cases-6)
   - [Results](#results-6)
8. [Final Thoughts & Improvements](#final-thoughts--improvements)
   - [Issues Found](#issues-found)
   - [Optimizations Applied](#optimizations-applied)


---

##  Overview
During the development of the **Little Explorers** eCommerce store, I conducted thorough **manual testing** to ensure all features function correctly across **different devices** and **screen sizes**. The testing was based on the **user stories** outlined in my **Kanban board**. 
I have tested the functionality according to the user stories that cover it. I am not including images in this section because most of them have already been added to the README documentation in various sections, such as the "Existing Features" section (which contains images) and the "Performance" section. Therefore, I find it unnecessary to repeat them.
Below, I have demonstrated the tasks, the results obtained from the tests, and the issues that were resolved.

### ** Key Areas Tested:**
-  Home Page Functionality
-  Product Catalog & Search
-  Shopping Cart & Checkout
-  User Authentication & Account Management
-  Order Management & Notifications
-  Admin Panel & Store Management

---

##  Home Page

### **User Story 3:**
*As a user, I want to filter and search for specific items so that I can easily find clothes based on size, color, or category.*
### **User Story 1 :**
*As a user, I want the website to be mobile-friendly so that I can browse and shop on any device.*


### **Test Cases:**
 Ensure the navigation menu is accessible on desktop and mobile.  
 Verify that featured products are displayed correctly.  
 Test if clicking on a featured product redirects to the correct product page.  
 Check if the search bar and category filters work properly.  
 Ensure the home page loads within an acceptable time.  

### ** Result:**  
 Some test cases were verified, and the homepage functionality appears to be working correctly. However, not all test cases were checked in detail.
 Navigation and featured products display correctly.
 Performance issue: Image loading performance needs improvement.Image loading was identified as an area for optimization.(more details I left in section PERFORMANCE of Readme documentation) Further analysis is needed to determine its impact.


---

##  Product Catalog & Search

### **User Story 2:**
*As a user, I want to be able to browse a catalog of products so that I can explore different clothing options for my children.*
### **User Story 3:**
*As a user, I want to filter and search for specific items so that I can easily find clothes based on size, color, or category.*

### **Test Cases:**
 Verify that clicking on a category filter updates the product list correctly.  
 Test the search function with valid and invalid queries.  
 Check if product images, prices, and ratings are displayed properly.  
 Ensure pagination works for large product listings.  
 Test responsiveness on different screen sizes.  

### ** Result:**  
Some test cases were verified, but a full review is still pending.
 Lazy loading was implemented for product images to enhance performance.
 Basic functionality appears to be working, but further validation is needed for pagination.
 Responsiveness on all devices is not working well—some layout issues were identified, and improvements are needed.


---

##  Shopping Cart & Checkout

### **User Story 4:** 
*As a user, I want to add items to my shopping cart so that I can prepare my purchase.*
### **User Story 5:**
*As a user, I want to securely checkout and make payments so that I can complete my purchase with ease and confidence.*

### **Test Cases:**
 Ensure users can add products to the cart.  
 Verify the cart updates when items are removed or quantities are changed.  
 Test checkout process with valid and invalid payment details.  
 Ensure Stripe payment integration is functioning.  
 Check that order confirmation emails are sent correctly.  

### ** Result:**  
 All tests passed and JavaScript optimizations were made to improve checkout speed.

---

##  User Authentication & Account Management

### **User Story 1:**
*As a user, I want to be able to register and log into my account so that I can manage my personal details, view my orders, and save my preferences..*
### **User Story 15:**
*As a shoper or site user I want to buy children's clothing from "Little Explorers,so that I can shop for kids in a convenient way.*

### **Test Cases:**
 Verify that users can register with a valid email and password.  
 Check that users can log in and log out securely.  
 Test password reset functionality with correct and incorrect credentials.  
 Ensure profile updates (e.g., address changes) are saved.  
 Confirm security measures (password hashing, CSRF protection).  

### ** Result:**  
 All tests passed and password reset page was slightly optimized for mobile display.

---

##  Order Management & Notifications

### **User Story 7:**
*As an admin, I want to be able to view and manage customer orders so that I can ensure that orders are processed and shipped in a timely manner.*
### **User Story 8:**
*As a user, I want to receive order confirmation and shipping notifications via email so that I am informed about the status of my purchase.*

### **Test Cases:**
 Ensure users can access their order history.  
 Verify order details are accurate (items, pricing, delivery address).  
 Test email notifications for order confirmation and status updates.  
 Check if unauthorized users are restricted from viewing orders.  

### ** Result:**  
 All tests passed.

---

##  Admin Panel & Store Management

### **User Story 9:**
*As a user, I want the website to be mobile-friendly so that I can browse and shop on any device.*
### **User Story 6:**
*As an admin, I want to manage products, categories so that I can keep the product listings up-to-date.*
### **User Story 7:**
*As an admin, I want to be able to view and manage customer orders so that I can ensure that orders are processed and shipped in a timely manner.*

### **Test Cases:**
 Verify admin users can add, edit, and delete products.  
 Check if product images are uploaded correctly to AWS S3.  
 Ensure admin panel pages load quickly and display relevant data.  
 Test order status updates and refunds.  
 Validate restricted access to admin-only features.  

### ** Result:**  
 All tests passed and missing AWS S3 settings were added to resolve image upload issues.(More details is insection BUGS of Readme documentation).

---

##  Final Thoughts & Improvements

### ** Issues Found:**
- **Some pages had large image files** causing slow loading.
- **JavaScript files blocked rendering** in some sections.
- **Checkout & login scripts needed optimization** for mobile devices.
- **Order history pages slowed down** when displaying large datasets.
- **Admin panel loaded unnecessary scripts**, impacting performance.

### ** Optimizations Applied:**
- Implemented lazy loading.
- **Deferred JavaScript execution** to improve page speed.
- **Optimized checkout & authentication scripts** for faster response.
- **Implemented pagination** for large order history pages.
- **Removed unnecessary admin panel scripts** to enhance performance.




