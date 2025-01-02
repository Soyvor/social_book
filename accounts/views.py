<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="{% static 'css/main.css' %}">
</head>
<body>
    <div class="login-container">
        <form method="POST">
            {% csrf_token %}
            <h2>Login</h2>
            <label for="username">Username</label>
            <input type="text" id="username" name="username" required><br><br>

            <label for="password">Password</label>
            <input type="password" id="password" name="password" required><br><br>

            <button type="submit" class="btn">Login</button>
        </form>
        <p>Don't have an account? <a href="{% url 'register' %}">Register here</a></p>
    </div>
</body>
</html>
