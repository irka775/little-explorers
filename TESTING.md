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
9. [Conclusion](#conclusion)

---

##  Overview
During the development of the **Little Explorers** eCommerce store, I conducted thorough **manual testing** to ensure all features function correctly across **different devices** and **screen sizes**. The testing was based on the **user stories** outlined in my **Kanban board**.

### ** Key Areas Tested:**
-  Home Page Functionality
-  Product Catalog & Search
-  Shopping Cart & Checkout
-  User Authentication & Account Management
-  Order Management & Notifications
-  Admin Panel & Store Management

---

##  Home Page

### **User Story 1:**
*As a user, I want to easily navigate the website and see featured products.*

### **Test Cases:**
 Ensure the navigation menu is accessible on desktop and mobile.  
 Verify that featured products are displayed correctly.  
 Test if clicking on a featured product redirects to the correct product page.  
 Check if the search bar and category filters work properly.  
 Ensure the home page loads within an acceptable time.  

### ** Result:**  
 **All tests passed.** Some performance optimizations were needed for **image loading**.

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
 **All tests passed.** **Lazy loading** was added for product images to improve performance.

---

##  Shopping Cart & Checkout

### **User Story 3:** 
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
 **All tests passed.** **JavaScript optimizations** were made to improve checkout speed.

---

##  User Authentication & Account Management

### **User Story 4:**
*As a user, I want to sign up, log in, and manage my account details.*

### **Test Cases:**
 Verify that users can register with a valid email and password.  
 Check that users can log in and log out securely.  
 Test password reset functionality with correct and incorrect credentials.  
 Ensure profile updates (e.g., address changes) are saved.  
 Confirm security measures (password hashing, CSRF protection).  

### ** Result:**  
 **All tests passed.** **Password reset page** was slightly optimized for mobile display.

---

##  Order Management & Notifications

### **User Story 5:**
*As a user, I want to view my past orders and receive order updates.*

### **Test Cases:**
 Ensure users can access their order history.  
 Verify order details are accurate (items, pricing, delivery address).  
 Test email notifications for order confirmation and status updates.  
 Check if unauthorized users are restricted from viewing orders.  

### ** Result:**  
 **All tests passed.** Large order history pages were **optimized** for faster loading.

---

##  Admin Panel & Store Management

### **User Story 6:**
*As an admin, I want to manage products, categories, and orders.*

### **Test Cases:**
 Verify admin users can add, edit, and delete products.  
 Check if product images are uploaded correctly to AWS S3.  
 Ensure admin panel pages load quickly and display relevant data.  
 Test order status updates and refunds.  
 Validate restricted access to admin-only features.  

### ** Result:**  
 **All tests passed.** Missing **AWS S3 settings** were added to resolve image upload issues.

---

##  Final Thoughts & Improvements

### ** Issues Found:**
- **Some pages had large image files** causing slow loading.
- **JavaScript files blocked rendering** in some sections.
- **Checkout & login scripts needed optimization** for mobile devices.
- **Order history pages slowed down** when displaying large datasets.
- **Admin panel loaded unnecessary scripts**, impacting performance.

### ** Optimizations Applied:**
- **Converted images to WebP format** and implemented lazy loading.
- **Deferred JavaScript execution** to improve page speed.
- **Optimized checkout & authentication scripts** for faster response.
- **Implemented pagination** for large order history pages.
- **Removed unnecessary admin panel scripts** to enhance performance.

---

##  Conclusion

The Little Explorers eCommerce project has been extensively tested to ensure a seamless and secure shopping experience. 


