### REQUIREMENTS:

- Django
- Django Rest Framework ( Rest API )
- Djoser ( Authetication )
- etc..

### ROUTES:

<details>
  <summary>Customer ( /api/v1/user )</summary>
  
  ### Login ( token/login/ )
  Method: `POST`
  
  * Requests body
  ```json
  {
    "email": "example@email.com",
    "password": "example123"
  }
  ```
  * Response body
  ```json
  {
    "token": "Token authetication.."
  }
  ```
  Status success: `200 (success)`

  Status exception:
  ```
    400 (bad requests)
    401 (unauthorization)
  ```

  ### Detail ( token/login/ )
  
  Method: `GET`
  
  Headers:
  - Authorization: Token token...

  Response body:
  ```json
  {
    "id": uuid4,
    "email": "example@email.com",
    "username": "example123",
    "first_name": "foo",
    "last_name": "bar",
    "is_superuser": bool,
    "is_staff": bool,
    ...
  }
  ```

  * Status success `200 (success)`

  * Status exception
  ```
    404 (not found)
    401 (unauthorization)
  ```
</details>
<details>
  <summary>Menu ( /api/v1/menu/ )</summary>
  
  ### MENU INDEX ( / )
  Method: `[GET, POST]`
  Headers:
  - Authorization: Token token...
  - Content-type: multipart/form-data
  
  Requests body:
  ```json
  {
    "name": "foo",
    "description": "lorem ipsum",
    "price": "1.3",
    "stock": 3,
    "thumbnail": (image file),
    "uploaded_images": [image files, ...],
  }
  ```
  
  Response body: 
  ```json
  {
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
    {
      "url": "http://127.0.0.1:8000/api/v1/menu/{uuid4}/",
      "id": uuid4,
      "name": "foo",
      "price": "1.3",
      "thumbnail": "http://127.0.0.1:8000/media/coffee_images/foo.jpg",
      "description": "lorem ipsum",
      ...
    },
  }
  ```
  Status success: 
  ```
    200 (success)
    201 (created)
  ```

  Status exception:
  ```
    400 (bad requests)
    401 (unauthorization)
  ```

  ### Detail ( /\<uuid:pk\> )
  
  Method: `[GET, PUT, DELETE]`
  
  Headers:
  - Authorization: Token token...
  - Content-type: multipart/form-data
  
  Requests body:
  ```json
  {
    "name": "bar",
    "description": "lorem ipsum",
    "price": "1.3",
    "stock": 3,
    "thumbnail": (image file),
    "uploaded_images": [image files, ...],
    "categories": [primarykey id, ...]
  }
  ```

  Response body:
  ```json
  {
    "id": uuid4,
    "email": "example@email.com",
    "username": "example123",
    "first_name": "foo",
    "last_name": "bar",
    "is_superuser": bool,
    "is_staff": bool,
    ...
  }
  ```

  Status success: 
  ```
    200 (success)
    204 (no content)
  ```

  Status exception:
  ```
    404 (not found)
    401 (unauthorization)
  ```
</details>

<details>
  <summary>CART ( /api/v1/cart/ )</summary>
  
  ### CART INDEX ( / ):
  
  Method: `[GET, POST]`
  
  Headers:
  - Authorization: Token token...
  - Content-type: application/json
  
  Requests body:
  ```json
  {
    "quantity": "1",
    "note": "lorem ipsum",
    "item": (primarykey id)
  }
  ```
  
  Response body: 
  ```json
  {
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
    {
      "quantity": "1",
      "note": "lorem ipsum",
      "item": (primarykey id)
    },
    ...
  }
  ```
  Status success: 
  ```
    200 (success)
    201 (created)
  ```

  Status exception:
  ```
    400 (bad requests)
    401 (unauthorization)
  ```

  ### Detail ( /\<uuid:pk\>/ )
  
  Method: `GET`
  
  Headers:
  - Authorization: Token token...
  - Content-type: application/json

  Response body:
  ```json
  {
    "quantity": "1",
    "note": "lorem ipsum",
    "item": (primarykey id)
  },
  ```

  Status success: 
  ```
    200 (success)
    204 (no content)
  ```

  Status exception:
  ```
    404 (not found)
    401 (unauthorization)
  ```
</details>

<details>
  <summary>Categories ( /api/v1/category/ )</summary>

  ### Detail ( /\<str:name\>/ )
  
  Method: `[GET, PUT, DELETE]`
  
  Headers:
  - Authorization: Token token...
  - Content-type: application/json

  Response body:
  ```json
  {
    "name": "foo",
    "item": (primarykey id)
  },
  ```

  Status success: 
  ```
    200 (success)
    204 (no content)
  ```

  Status exception:
  ```
    404 (not found)
    401 (unauthorization)
  ```
</details>

### INSTALLATION:

1. Clone the repo
   ```
   git clone https://github.com/stev029/GulfCoffee.git
   ```
2. Create and then activate your virtual environment.
If both of these steps are completed properly, you should see your command line start with your virtual environemnt (i.e. `(myvirtenv)`)
   ```
   python3 -m venv venv
   
   ## For Mac / Linux users
   source venv/bin/activate
   
   ## For Windows users
   venv\Scripts\activate
   ```
3. Make sure to change directory into the repository
   ```
   cd GulfCoffee
   ```
4. Install all of the required libraries
   ```
   pip install -r requirements.txt
   ```
5. Set environment variables by creating a `.env` file in the top level directory and add the environment variables. You will need to contact a project administrator to obtain the variables. WARNING: You cannot properly run this project without the environment variables.
   You're `.env` file should look like this
   ```
   SECRET_KEY=[secret key here]
   DEBUG=[debug value here]
   ```
6. Setup the database schema
   ```
   python manage.py migrate
   ```
7. Populate the database with sample data
   ```
   python manage.py loaddata menu/fixtures/coffee.json
   python manage.py loaddata customer/fixtures/users.json
   ```
8. Create a super user to access the admin dashboard
   ```
   python manage.py createsuperuser
   ```
9. Run the server and then login to the admin dashboard at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) with your newly created super user
   ```
   python manage.py runserver
   ```

## CONTACT
[Instagram](https://instagram.com/misigoput?igshid=MzNlNGNkZWQ4Mg==)

abyy1144@gmail.com