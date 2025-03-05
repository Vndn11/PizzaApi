# **🍕 Pizza API - Django REST Framework**  

## **📌 Overview**  
The **Pizza API** is a **Django-based RESTful API** designed to manage a pizza ordering system. It allows users to **view, create, update, and delete** pizza orders while storing data in a **MongoDB** database. The API supports different pizza sizes, types, and toppings, providing a flexible structure for pizza customization.  

---

## **🚀 Features**  

✔ **CRUD Operations** – Create, Read, Update, Delete pizzas  
✔ **Django REST Framework (DRF) API** – Built using Django's powerful API framework  
✔ **MongoDB Integration** – Uses MongoDB as the database for efficient data storage  
✔ **RESTful Endpoints** – Allows seamless interaction with the pizza database  
✔ **Scalability** – Structured to support future enhancements like order tracking and user authentication  

---

## **🛠 Tech Stack**  

| Technology         | Purpose |
|-------------------|------------------------------|
| **Django**       | Backend web framework |
| **Django REST Framework (DRF)** | API development |
| **MongoDB**      | NoSQL database for storing pizza data |
| **Python**       | Core programming language |
| **Visual Studio Code (VS Code)** | Development environment |

---

## **📂 Installation & Setup**  

### **1️⃣ Download & Install Required Software**  
Ensure you have the following installed on your system:  
✔ **[Python 3.9+](https://www.python.org/downloads/release/python-395/)**  
✔ **[MongoDB Community Server](https://www.mongodb.com/try/download/community)**  
✔ **[Visual Studio Code](https://code.visualstudio.com/download)**  

---

### **2️⃣ Install Required Python Packages**  
Navigate to the project folder where `requirements.txt` is located and install dependencies:  

```bash
pip install -r requirements.txt
```

---

### **3️⃣ Set Up MongoDB Database**  
- Open **MongoDB Compass**  
- Create a new database named **Pizza**  
- Ensure MongoDB is running before executing the API  

---

### **4️⃣ Run Database Migrations**  
```bash
python manage.py makemigrations
python manage.py migrate
```

---

### **5️⃣ Start the Development Server**  
```bash
python manage.py runserver
```
The server will start at **http://127.0.0.1:8000/**.

---

## **🔗 API Endpoints**  

### **📌 Retrieve Pizza Data**  
| Method | Endpoint | Description |
|--------|----------|-------------|
| **GET** | `/api/` | Lists all stored pizzas with size, type, and toppings |
| **GET** | `/api/<size_id>/` | Lists all pizzas of a given size |
| **GET** | `/api/<type_id>/` | Lists all pizzas of a given type |

### **📌 Create & Modify Pizzas**  
| Method | Endpoint | Description |
|--------|----------|-------------|
| **POST** | `/api/create/` | Creates a new pizza entry in the database |
| **PUT** | `/api/edit/<pizza_id>/` | Updates an existing pizza entry |
| **DELETE** | `/api/delete/<pizza_id>/` | Deletes a pizza from the database |

---

## **📌 Example API Requests**  

### **1️⃣ Create a Pizza**  
**Endpoint:** `POST /api/create/`  
**Request Body (JSON):**  
```json
{
  "name": "Pepperoni Pizza",
  "size": "Large",
  "type": "Non-Veg",
  "toppings": ["Pepperoni", "Cheese", "Tomato Sauce"]
}
```

**Response:**  
```json
{
  "id": 1,
  "name": "Pepperoni Pizza",
  "size": "Large",
  "type": "Non-Veg",
  "toppings": ["Pepperoni", "Cheese", "Tomato Sauce"]
}
```

---

### **2️⃣ Retrieve All Pizzas**  
**Endpoint:** `GET /api/`  
**Response:**  
```json
[
  {
    "id": 1,
    "name": "Margherita",
    "size": "Medium",
    "type": "Veg",
    "toppings": ["Cheese", "Tomato Sauce", "Basil"]
  },
  {
    "id": 2,
    "name": "BBQ Chicken",
    "size": "Large",
    "type": "Non-Veg",
    "toppings": ["BBQ Sauce", "Chicken", "Cheese"]
  }
]
```

---

### **3️⃣ Update an Existing Pizza**  
**Endpoint:** `PUT /api/edit/1/`  
**Request Body (JSON):**  
```json
{
  "name": "BBQ Chicken Deluxe",
  "size": "Large",
  "type": "Non-Veg",
  "toppings": ["BBQ Sauce", "Grilled Chicken", "Onions", "Cheese"]
}
```

**Response:**  
```json
{
  "message": "Pizza updated successfully!"
}
```

---

### **4️⃣ Delete a Pizza**  
**Endpoint:** `DELETE /api/delete/1/`  
**Response:**  
```json
{
  "message": "Pizza deleted successfully!"
}
```

---

## **🚀 Future Enhancements**  

✅ Add **User Authentication** to allow users to manage personal orders  
✅ Integrate **Frontend (React or Vue.js)** for an interactive UI  
✅ Implement **Order Tracking & Payment Integration**  
✅ Extend API to support **multiple categories, custom orders, and discounts**  
