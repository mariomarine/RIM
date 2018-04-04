# RIM
GPS Rental Inventory Management

This project uses Django to manage a basic customer-rental system

# Documentation
## Starting the project

### Prerequisets
- Install Python
- Network Access

### Steps to Build
- `git clone https://github.com/mariomarine/rim.git`
- `cd rim`
- `pip install -r requirements.txt`
- `python manage.py runserver 0.0.0.0:8000`

## Using the project
- From the computer running the server, run ipconfig (windows) or ifconfig (unix) to get the IP address
- There are two urls you will use:
    - http://<server_ip_address>:8000/rentals/new_customer.html
        - This url is for a new Customer to enter his/her information into the database
        - Only New Customers should be using this functionality. To alter an existing person, do so through the Admin
    - http://<server_ip_address>:8000/admin
        - This is where you have a lot of control over the data in the database.
        - New Package:
            - Click on Package Values
            - Click "Add Package Value +" in the upper-right
            - Fill information
            - Save
        - Alter Package
            - Find desired Package and click
            - Alter information
            - Save
        - New Rental:
            - Click on Package Rentals
            - Click "Add Package Rental +" (Note: Customer must exist in the database before starting this process)
            - Choose Package and Quantity
            - Click the "+" button next to Rental
            - Select Customer
            - Fill in Start/End Dates (using Date picker is recommended to get correct formatting (yyyy-mm-dd))
            - Ask the customer if they agree to Terms and Conditions, then check "Agree to TC"
            - Save
            - Fill out Gear information
            - Save
        - Return Rental
            - Click on Rentals
            - Find the rental that is being returned (Note: There is power in sorting by return date and using the filter on the right)
            - Check the Returned checkbox
            

