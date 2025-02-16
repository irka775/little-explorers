# **Performance Testing - Little Explorers**

## **Table of Contents**
- [Overview](#overview)
- [Performance Testing by Feature](#performance-testing-by-feature)
  - [Home Page](#home-page)
  - [Product Catalog & Search](#product-catalog--search)
  - [Shopping & Checkout](#shopping--checkout)
  - [User Authentication & Account Management](#user-authentication--account-management)
  - [Order Management & Notifications](#order-management--notifications)
  - [Admin Features](#admin-features)
- [Performance Test Results](#performance-test-results)
- [Optimization Recommendations](#optimization-recommendations)
- [Conclusion](#conclusion)

---

## **Overview**
As part of my project, I conducted performance testing using Google Lighthouse in Chrome DevTools on both desktop and mobile. While the results were good on desktop, mobile performance was not as strong. The tests identified several areas that need improvement, mainly related to image optimization and static file loading.

## **Performance Testing by Feature**
Below is a **breakdown of performance testing** based on **Kanban Board user stories and tasks**.

### **Home Page**
 **Issues Found:**
- Background image slightly impacts performance on mobile
- Navbar script blocking rendering

 **Test Results:**
- **View Home Page Test - Desktop**  ![View Home Page Test - Desktop](media\screenshots\lighthouse\home_desctop.PNG)
- **View Home Page Test - Mobile**  ![View Home Page Test - Mobile](media\screenshots\lighthouse\home_mobile.PNG)

---

### **Product Catalog & Search**
 **Issues Found:**
- Search bar performance drops slightly on slow networks
- Lazy loading required for product images

 **Test Results:**
- **View Product Catalog Test** ![View Product Catalog Test - Desktop](#)
- **View Product Catalog Test** ![View Product Catalog Test - Mobile](#)
- **View Product Search Test** ![View Product Search Test - Desktop](media\screenshots\lighthouse\search_desctop.PNG)
- **View Product Search Test** ![View Product Search Test - Mobile](media\screenshots\lighthouse\search_mobile.PNG)

---

### **Shopping & Checkout**

 **Issues Found:**
- Payment form script causes a slight delay in mobile
- Multiple JavaScript calls increase blocking time

 **Test Results:**
- **View Shopping Cart Test - Desktop** ![View Shopping Cart Test - Desktop](media\screenshots\lighthouse\shopBag_desctop.PNG)
- **View Shopping Cart Test - Mobile** ![View Shopping Cart Test - Mobile](media\screenshots\lighthouse\shopBag_mobile.PNG)
- **View Checkout Test - Desktop** ![View Checkout Test - Desktop](media\screenshots\lighthouse\checkout_desctop.PNG)
- **View Checkout Test - Mobile** ![View Checkout Test - Mobile](#)

---

### **User Authentication & Account Management**

 **Issues Found:**
- Authentication scripts cause minor delay on mobile
- Password reset page performance could be improved

 **Test Results:**
- **View Sign-Up Test - Desktop** ![View register Test - Desktop](media\screenshots\lighthouse\register_desctop.PNG)
- **View Sign-Up Test - Mobile** ![View register Test - Mobile](media\screenshots\lighthouse\register_mobile.PNG)
- **View Login Test - Desktop** ![View Login Test - Desktop](media\screenshots\lighthouse\signIn_desctop.PNG)
- **View Login Test - Mobile** ![View Login Test - Mobile](media\screenshots\lighthouse\signin_mobile.PNG)
- **View Profile Page Test - Desktop** ![View Profile Page Test - Desktop](media\screenshots\lighthouse\profile_desctop.PNG)
- **View Profile Page Test - Mobile** ![View Profile Page Test - Mobile](media\screenshots\lighthouse\profile_mobile.PNG)

---

### **Order Management**

 **Issues Found:**
- Order history table takes longer to render on large datasets

 **Test Results:**
- **View Order History Test - Desktop** ![View Order History Test - Desktop](media\screenshots\lighthouse\orderHistory_desctop.PNG)
- **View Order History Test - Mobile** ![View Order History Test - Mobile](media\screenshots\lighthouse\orderHistory_mobile.PNG)


---

### **Admin Features**


 **Issues Found:**
- Admin panel loads extra scripts that slow page performance

 **Test Results:**
- **View Login Test - Mobile** ![View Admin Panel Test - Desktop](media\screenshots\lighthouse\admin_desctop.PNG)
- **View Login Test - Mobile** ![View Admin Panel Test - Mobile](media\screenshots\lighthouse\admin_mobile.PNG)
- **View Store settings Test - Desktop** ![View Store settings Test - Desktop](media\screenshots\lighthouse\storeSet_desctopp.PNG)
- **View Store settings  Test - Mobile** ![View Store settings  Test - Mobile](media\screenshots\lighthouse\storeSet_mobile.PNG)







