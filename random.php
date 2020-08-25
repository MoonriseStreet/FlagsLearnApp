<?php

session_start();

if (isset($_SESSION['previous'])) {
    if (basename($_SERVER['PHP_SELF']) != $_SESSION['previous']) {
        $update = True;
    } else {
        $update = False;
    }
}

require_once "util.php";

if (!isset($_SESSION['rand']) || isset($_POST['random']) || $update) {
    newCountry($pdo);
    header('Location: random.php');
    return;
}

include('header.html');
?>
    <div class="box">
        <p class="country_title"><?= $_SESSION['rand']['name'] ?></p>
        <img class="flag" src="<?= $_SESSION['rand']['picture'] ?>"
             alt="something went wrong... check your internet connection">
        <div class="big_button">
            <form method="POST">
                <input type="submit" class="orange_button" name="random" value="Another country">
            </form>
        </div>
        <div class="big_button">
            <a class="orange_button" href="index.php">Home</a>
        </div>
    </div>
<?php
include('footer.html');
