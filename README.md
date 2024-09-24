## Satvik Food Restaurant Overview 

The Satvik Restaurant Table Reservation App is a Django-based web application designed to allow users to book tables at the Satvik restaurant. The app provides a user-friendly interface for customers to reserve tables, view reservations, and make special requests. It also includes an admin panel with rich text editing capabilities for managing reservations using Django Summernote.

![Responsice Mockup Desktop]([https://github.com/pooja-par/satvik_food/satvik/static/satvik/images/bigscreen.png])
![Responsice Mockup Mobile](https://github.com/pooja-par/satvik_food/satvik/static/satvik/images/smallscreen.png)

Author: Pooja Parmar

## Site Goal

Allow the users to view the menu, book the table and also update the booking. Website also allows admin to login and view the reservation. 

## Features

- Responsive design for various screen sizes: Check the pictures in first section.
- Nevigation bar for Home, Menu, Contact and Admin Login panal.
- Table Reservation: Users can book tables by specifying the number of guests, the date, and the time.

![Responsice Mockup Mobile](https://github.com/pooja-par/satvik_food/satvik/static/satvik/images/tablereserve.png)

- View Reservations: Users can view their upcoming reservations.
- Cancel Reservations: Users can cancel their reservations directly from the application.

![Responsice Mockup Mobile](https://github.com/pooja-par/satvik_food/satvik/static/satvik/images/viewreserve.png)

- Admin Management: Admins can manage reservations via the Django Admin interface with rich text capabilities provided by Django Summernote.

![Responsice Mockup Mobile](https://github.com/pooja-par/satvik_food/satvik/static/satvik/images/djangohome.png)

- Responsive Design: The application is fully responsive and optimized for desktop and mobile devices.
- Following tables are available to book. one table can not be booked multiple times. 

![Responsice Mockup Mobile](https://github.com/pooja-par/satvik_food/satvik/static/satvik/images/tables.png)

- Admin can view the reservation

![Responsice Mockup Mobile](https://github.com/pooja-par/satvik_food/satvik/static/satvik/images/reservations.png)

- Menu page where user can select the menu

![Responsice Mockup Mobile](https://github.com/pooja-par/satvik_food/satvik/static/satvik/images/menu.png)

- Contact Us page where user can find the contact detail and address of the restaurant.

![Responsice Mockup Mobile](https://github.com/pooja-par/satvik_food/satvik/static/satvik/images/contact.png)


## Technologies Used

- Backend: Django 4.2.16 (Python-based web framework)
- Frontend: HTML, CSS, JavaScript, Django templates
- Database: PostgreSQL (or SQLite in development)
- Rich Text Editor: Django Summernote for rich text editing in the admin panel
- Deployment: Gunicorn for running the Django application, and Heroku for hosting

## Usage 

Booking a Table: Navigate to the booking page, fill in the details (number of guests, date, and time), and submit the form.
View Bookings: After logging in, users can view their upcoming reservations.
Cancel Booking: Users can cancel reservations from their reservation list.

## Admin Features
Admin Panel: Go to /admin, log in as the superuser, and manage reservations.
Rich Text Editor: The admin panel includes Django Summernote for managing special requests in reservations with rich text editing.

![Responsice Mockup Mobile](https://github.com/pooja-par/satvik_food/satvik/static/satvik/images/output.png)

## Testing

I have manually tested this project by doing the following: -passed code through a PEP8 linter and confirmed there are no problems -Tested in my local terminal and Code Instite Heroku terminal -Check has been made by giving different numbers and also with empty field and random characters. With empty space and random characters, code return error and ask user to reenter the count again. -Where necessary, by print values are checked in terminal.

## Deployment
This project was deployed using Code Institute's mock terminal for Heroku.

Steps for deployment: 
- Login to heroku and enter your detail
- Fork or clone this repository
- Create a new heroku app
- Create config-var : DATABASE_URL, DISABLE_COLLECTSTATIC, SECRET_KEY,
- Select github for the deployment within deployment tab
- Select manual deploy option
- link heroku app to the repository -Click on Deploy branch.

## Validator Testing
-HTML
No errors were returned when passing through the official W3C validator
-CSS
No errors were found when passing through the official (Jigsaw) validator

## Unfixed Bugs

W2C shows couple of errors related to django. I guess it is not an error but may be django syntex is not identified. 

## Credits

### Medida & Content
All images are taken from following links:
- <https://www.djangoproject.com/start/>
- <https://getbootstrap.com/docs/4.6/getting-started/introduction/>
- <https://cdnjs.com/libraries/font-awesome>
- All pictures are directly searched and links are attached. 
- following plateform was used as a reference to develop the code.
- <https://www.w3schools.com/bootstrap/bootstrap_ref_all_classes.asp> : reference to develop the code





