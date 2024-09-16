**Overview**
The Satvik Restaurant Table Reservation App is a Django-based web application designed to allow users to book tables at the Satvik restaurant. The app provides a user-friendly interface for customers to reserve tables, view reservations, and make special requests. It also includes an admin panel with rich text editing capabilities for managing reservations using Django Summernote.

**Features**
- Table Reservation: Users can book tables by specifying the number of guests, the date, and the time.
- View Reservations: Users can view their upcoming and past reservations.
- Cancel Reservations: Users can cancel their reservations directly from the application.
- Special Requests: Customers can include special requests for their reservations using rich text editing.
- Admin Management: Admins can manage reservations via the Django Admin interface with rich text capabilities provided by Django Summernote.
- Responsive Design: The application is fully responsive and optimized for desktop and mobile devices.

**Technologies Used**
- Backend: Django 4.2.16 (Python-based web framework)
- Frontend: HTML, CSS, JavaScript, Django templates
- Database: PostgreSQL (or SQLite in development)
- Rich Text Editor: Django Summernote for rich text editing in the admin panel
- Deployment: Gunicorn for running the Django application, and possibly Heroku for hosting

**Usage**
**Customer Features**
Booking a Table: Navigate to the booking page, fill in the details (number of guests, date, time, and special requests), and submit the form.
View Bookings: After logging in, users can view their upcoming reservations.
Cancel Booking: Users can cancel reservations from their reservation list.
**Admin Features**
Admin Panel: Go to /admin, log in as the superuser, and manage reservations.
Rich Text Editor: The admin panel includes Django Summernote for managing special requests in reservations with rich text editing.

