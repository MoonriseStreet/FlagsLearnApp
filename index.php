<?php

session_start();
require_once "util.php";

?>

<?php include('header.html'); ?>
<div class="box">
    <div class="central_message">
        <div class="big_button">
            <a class="orange_button" href="flag_quiz.php">Flag quiz</a>
        </div>
        <div class="big_button">
            <a class="orange_button" href="country_quiz.php">Country quiz</a>
        </div>
        <div class="big_button">
            <a class="orange_button" href="list.php">List of countries</a>
        </div>
        <div class="big_button">
            <a class="orange_button" href="random.php">Random country</a>
        </div>
    </div>
</div>
<?php include ('footer.html');
