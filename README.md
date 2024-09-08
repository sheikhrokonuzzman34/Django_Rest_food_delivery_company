# FoodieBackend System

This Django-based API manages Food Delivery.

## Git clone
   ```bash
   git clone https://github.com/sheikhrokonuzzman34/Django_Rest_food_delivery_company.git

   ``` 


## How to Run

1. virtual environment Crete : `python -m venv env`
2. virtual environment active : `. env/Scripts/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. file directory change : `cd CRUD-API-Endpoints-for-Order-Management-django-rest_api/`
5. Apply makemigrations: `python manage.py makemigrations`
6. Apply migrations: `python manage.py migrate`
7. Run the server: `python manage.py runserver`

## Testing

Run the test suite:

```bash
python manage.py test
```   


## Base URL
- All endpoints are relative to the base URL: `https://example.com/`

## Authentication simplejwt
- The API requires authentication using [Token Authentication](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html).

---

##  Super user
-
  ```text
  useremail : 'admin@gamil.com'
  password : '123456'
  ```


## Authentication Endpoints

### Token Authentication
- **URL:** `POST /userapp/register/`
- **Description:** Create a new user account.
- **Body:**  useremail and password
  ```json
  {
  "email": "sumon@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "role": "employee",  
    "password": "password123"
  }
- **Response:**
  - Status Code: 200 OK


- **URL:** `POST /userapp/login/`
- **Description:** Log in with email and password to receive access and refresh tokens.
- **Body:**  useremail and password
  ```json
  {
  "email": "user@example.com",
  "password": "password123",
  }
- **Response:**
  - Status Code: 200 OK


## Restaurant Management Endpoints
  
### Create Restaurant
- **URL:** `POST /restaurant/restaurants`
- **Description:** Create a new restaurant.
- **Authentication:** Required (Bearer token)
- **Headers:** Authorization Bearer token
- **Body:** 
  ```json
  {
  "name": "Pizza House",
  "location": "123 Main St, City"
  }
  ```

- **Response:**
  - Status Code: 201 Created
  - Content: restaurant data.

## Menu Management Endpoints

### Create Category
- **URL:** `POST /restaurant/categories/`
- **Description:** Create a new category for a restaurant.
- **Authentication:** Required (Bearer token)
- **Headers:** Authorization Bearer token
- **Body:** 
  ```json
  {
  "name": "Main Course",
  "restaurant": 1
  }

  ```

- **Response:**
  - Status Code: 201 Created
  - Content: Category  data.


## Create Menu Item

### Create Category
- **URL:** `POST /restaurant/menu-items/`
- **Description:** Add a menu item to a category.
- **Authentication:** Required (Bearer token)
- **Headers:** Authorization Bearer token
- **Body:** 
  ```json
  {
  "name": "Margherita Pizza",
  "price": 9.99,
  "category": 1
  }

## Order Management Endpoints

### Create Category
- **URL:** `POST /restaurant/orders/`
- **Description:** Place a new order.
- **Authentication:** Required (Bearer token)
- **Headers:** Authorization Bearer token
- **Body:** 
  ```json
  {
  "payment_info": "Dummy payment info",
  "total_amount": "250.32",
  "items": [
    {
      "product": 3,
      "quantity": 3
    }
  ]
  }

  ```

- **Response:**
  - Status Code: 201 Created
  - Content: Category  data.


---



## Error Responses
- The API may return the following error responses:
  - Status Code: 400 Bad Request - Invalid request parameters.
  - Status Code: 401 Unauthorized - Authentication failure.
  - Status Code: 403 Forbidden - Insufficient permissions.
  - Status Code: 404 Not Found - Resource not found.
  - Status Code: 500 Internal Server Error - Unexpected server error.

---

## Versioning
- 
This `README.md` provides a clear structure for API documentation in a GitHub format, covering user authentication, restaurant management, menu management, and order management, as well as error responses.


---

