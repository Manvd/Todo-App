# 📝 Todo App with JWT Authentication

A full-stack Todo application with secure user authentication using JSON Web Tokens (JWT). This project demonstrates REST API design, authentication, and CRUD operations.

---

## 🚀 Features

* 🔐 User Authentication (Signup/Login with JWT)
* 🔒 Protected Routes (Only authenticated users can access todos)
* ✅ Create, Read, Update, Delete Todos
* ⚠️ Error Handling & Validation
* 🔑 Password hashing for security

---

## 🛠️ Tech Stack

* Backend: Node.js, Express.js
* Database: MongoDB (Mongoose)
* Authentication: JSON Web Tokens (JWT), bcrypt

---

## 📁 Project Structure

```
/todo-app
 ├── controllers/
 ├── routes/
 ├── models/
 ├── middleware/
 ├── config/
 ├── .env.example
 ├── server.js
 └── README.md
```

---

## ⚙️ Installation & Setup

1. Clone the repository:

```
git clone https://github.com/your-username/todo-app.git
cd todo-app
```

2. Install dependencies:

```
npm install
```

3. Create a `.env` file:

```
PORT=5000
MONGO_URI=your_mongodb_uri
JWT_SECRET=your_secret_key
```

4. Run the server:

```
npm start
```

---

## 📡 API Endpoints

### Auth Routes

* POST `/api/auth/register` → Register user
* POST `/api/auth/login` → Login user

### Todo Routes (Protected)

* GET `/api/todos` → Get all todos
* POST `/api/todos` → Create todo
* PUT `/api/todos/:id` → Update todo
* DELETE `/api/todos/:id` → Delete todo

---

## 🔐 Authentication

* Uses JWT for secure authentication
* Token must be sent in headers:

```
Authorization: Bearer <token>
```

---

## 🌟 Future Improvements

* Refresh Tokens
* Pagination & Filtering
* Role-based access control
* Deployment (Render / Railway / AWS)

---

## 📌 Learning Outcomes

* REST API design
* Authentication & Authorization
* Middleware usage
* Secure password handling

---

## 🤝 Contributing

Feel free to fork and improve the project!

---

## 📄 License

This project is open-source and available under the MIT License.
