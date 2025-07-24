# Prime-Cuts Booking

## Project Description
The "Prime-Cuts Booking" project aims to develop a simple, intuitive web-based application that allows customers to book appointments at a local barbershop. 
The system will also provide the barbershop owner with a simple interface to manage appointments, services, and working hours.

## Context
Prime-Cuts is a small, popular barbershop that currently manages all its appointments via phone calls and a physical appointment book. This manual process is time-consuming, prone to errors (e.g., double bookings), and offers no flexibility for customers who want to book outside of business hours. 
The owner wants to modernize operations, improve customer experience, and reduce the administrative workload on the staff. 
The application should be straightforward and require minimal technical knowledge to operate.

## Key Stakeholders

- **Barbershop Owner**: Primary user of the admin interface. Needs to manage schedules, services, and view booking reports.
- **Barbers**: Will use the system to check their daily schedules.
- **Customers**: Will use the public-facing website to book, reschedule, or cancel their appointments.
- **Receptionist**: Will use the system to manage walk-in appointments and assist customers over the phone.

## User Stories

### Customer Stories

- As a customer, I want to see available time slots for a specific service and barber, so that I can book an appointment at my convenience.
- As a customer, I want to create a simple profile with my name and contact details, so I don't have to enter them every time I book.
- As a customer, I want to receive an email and SMS confirmation for my new appointment, so I am sure it has been booked correctly.
- As a customer, I want to receive a reminder 24 hours before my appointment, so I don't forget it.
- As a customer, I want to be able to easily cancel or reschedule my appointment online up to 24 hours in advance.
- As a customer, I want to view my history of past and upcoming appointments.

### Staff (Owner/Receptionist/Barber) Stories

- As the barbershop owner, I want to define the services offered, including their name, duration, and price.
- As the barbershop owner, I want to manage my staff's profiles and their standard working hours and days off, so the system only shows real availability.
- As the barbershop owner, I want to view a daily, weekly, and monthly overview of all booked appointments for all barbers.
- As a barber, I want to be able to block specific time slots in my calendar for breaks or personal appointments.
- As a receptionist, I want to be able to book an appointment on behalf of a customer who calls or walks in.
- As the owner, I want to see a simple report on which services are most frequently booked, so I can understand my business better.
- As a barber, I want to see any notes a customer has left with their booking (e.g., "allergic to a certain product").

## Quality Attributes

- **Usability**: The system must be extremely easy to use for both customers and staff with no technical background. The booking process should be completable in just a few clicks.
- **Reliability**: The system must be available 24/7. The booking data must be accurate to avoid conflicts like double bookings.
- **Performance**: The page for viewing available slots should load within 2 seconds, even during peak hours.
- **Security**: Customer data (name, email, phone number) must be stored securely. No payment information will be handled initially.

## Additional Information Important for the Project

- The initial version will not handle payments. This is a potential feature for a future release.
- The application must be responsive and work flawlessly on mobile devices, as most customers are expected to book via their smartphones.
- The initial version should be as simple and cheap as possible.