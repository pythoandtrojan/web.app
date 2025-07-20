<?php
session_start();
require '../php/config.php';
require '../php/admin_auth.php';

if (!isset($_SESSION['admin_loggedin']) || $_SESSION['admin_loggedin'] !== true) {
    header("Location: /admin");
    exit;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Painel de Admin</title>
    <link rel="stylesheet" href="../static/styles.css">
</head>
<body>
    <div class="container">
        <h1>Painel de Admin</h1>
        <p>Bem-vindo, Admin!</p>
        <a href="/logout" class="btn">Sair</a>
    </div>
    <script src="../static/scripts.js"></script>
</body>
</html>
