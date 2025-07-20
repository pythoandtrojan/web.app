<?php
session_start();
require 'admin_auth.php';

admin_logout();
header("Location: /admin");
exit;
?>
