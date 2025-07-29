# "Fork & Knife" Delivery Platform

## Project Description

The "Fork & Knife" project is the creation of a food delivery platform that connects customers with local restaurants. The platform will consist of a customer-facing web and mobile app for ordering, a restaurant-facing web portal for managing menus and orders, and a logistics system for delivery drivers.

## Context

The market for food delivery is growing, but existing platforms often charge high commission fees to restaurants. "Fork & Knife" aims to be a more restaurant-friendly alternative with a transparent fee structure. The system needs to handle a three-sided marketplace: coordinating orders from customers, preparation by restaurants, and pickup/delivery by drivers in real-time.

## Key Stakeholders

- **Customers**: Users ordering food.
- **Restaurant Owners/Managers**: Users managing menus, prices, and incoming orders.
- **Delivery Drivers**: Users who accept and complete delivery jobs.
- **Platform Administrators**: Internal team managing platform operations, user support, and payments.

## User Stories

### Customer Stories

- As a customer, I want to browse restaurants by cuisine type, location, price range, and rating, so I can find food I like.
- As a customer, I want to filter restaurants based on dietary options (e.g., vegetarian, gluten-free), so I can meet my dietary needs.
- As a customer, I want to view a restaurant's full menu with descriptions and prices, and add items to my cart.
- As a customer, I want to pay for my order securely within the app using various methods (credit card, PayPal).
- As a customer, I want to track the status of my order in real-time on a map, from "order accepted" to "in the kitchen," "out for delivery," and "delivered."
- As a customer, I want to save my favorite restaurants and re-order a previous meal with one click.
- As a customer, I want to rate and review the restaurant and the delivery driver after my order is complete.

### Restaurant Stories

- As a restaurant manager, I want to receive a clear, audible notification for new orders on a dedicated tablet application.
- As a restaurant manager, I want to accept or reject new orders and provide an estimated preparation time.
- As a restaurant manager, I want to easily create and update my menu, including photos, descriptions, prices, and categories.
- As a restaurant manager, I want to temporarily mark specific items or the entire restaurant as "sold out" or "unavailable."
- As a restaurant manager, I want to view my order history and access financial reports on my daily and weekly earnings.
- As a restaurant manager, I want to be able to communicate with the customer or driver regarding a specific order (e.g., "we are out of an ingredient").

### Driver Stories

- As a delivery driver, I want to set my status to "online" to start receiving delivery job offers.
- As a delivery driver, I want to see a list of available delivery jobs near me, including pickup/drop-off locations and the estimated fee.
- As a delivery driver, I want to accept or decline a job offer within a limited time frame.
- As a delivery driver, I want to use an in-app map with optimized routing to navigate to the restaurant and then to the customer.
- As a delivery driver, I want to be able to contact the customer or restaurant if I have issues (e.g., can't find the address).
- As a delivery driver, I want to see a summary of my completed trips and my total earnings for the day/week.

## Quality Attributes

- **Scalability**: The system must be able to handle a high volume of concurrent users and orders, especially during peak lunch and dinner times.
- **Real-time Capabilities**: Order status updates, driver location tracking, and notifications must happen in near real-time.
- **Reliability**: The system must have high uptime. An outage during peak hours would result in significant revenue loss and user frustration. The payment processing must be completely reliable.
- **Interoperability**: The system will need to integrate with third-party services for payments (e.g., Stripe) and mapping/geolocation (e.g., Google Maps).
- **Maintainability**: The architecture should allow different teams to work on different parts of the system (customer, restaurant, logistics) independently.

## Additional Information Important for the Project

The architecture will likely consist of several distinct backend services. These services will need to communicate with each other, likely via a mix of synchronous (REST/gRPC) and asynchronous (message queues like RabbitMQ or Kafka) communication.
Each service would have its own database to ensure loose coupling.
A robust API gateway will be required to manage and secure access to the backend services from the various client applications (web, iOS, Android).