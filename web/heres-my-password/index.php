<?php
define("USERNAME", "Wolverine");
define("PASSWORD", "lightswitchon_and_offLOL26");
define("FLAG", "jctf{c0NGR@T2_y0U_p@22wORd_SPR@y3D!}");
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Login</title>
</head>

<body>
    <form action="" method="post">
        Username: <input type="text" name="username">
        <br>
        Password: <input type="password" name="password">
        <br>
        <input type="submit" value="Login" name="submit">
    </form>
    <?php
    if (isset($_POST["submit"])) {
        if ($_POST["username"] === USERNAME && $_POST["password"] === PASSWORD) { ?>
            <script>
                alert("<?php echo FLAG ?>");
            </script>
        <?php } else { ?>
            <script>
                alert("Invalid login");
            </script>
    <?php }
    } ?>
</body>

</html>