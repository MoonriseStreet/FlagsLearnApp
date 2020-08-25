<?php
session_start();
require_once "util.php";

if (! isset($_SESSION['level'])) {
    $_SESSION['level'] = 'easy';
}

if ( isset($_POST['0'])) {
    $_SESSION['level'] = 'easy';
    header( "Location: settings.php");
    return;
}
if ( isset($_POST['1'])) {
    $_SESSION['level'] = 'medium';
    header( "Location: settings.php");
    return;
}
if ( isset($_POST['2'])) {
    $_SESSION['level'] = 'hard';
    header( "Location: settings.php");
    return;
}

include ('header.html');
?>

<div class="box">
    <div class="central_message">
        <form method="POST">
            <p class="country_title">Current level: <?=$_SESSION['level']?>. Choose level</p>
            <ul class="levels">
                <li class="level">
                    <input class="orange_button" type="submit" name="0"
                           value="Easy">
                </li>
                <li class="level">
                    <input class="orange_button" type="submit" name="1"
                           value="Medium">
                </li>
                <li class="level">
                    <input class="orange_button" type="submit" name="2"
                           value="Hard">
                </li>
            </ul>
        </form>
        <div class="big_button">
            <a class="orange_button" href="index.php">Home</a>
        </div>
    </div>
</div>

<?php
include ('footer.html');
?>