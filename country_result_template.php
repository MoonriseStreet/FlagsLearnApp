<div class="quiz_block">
    <div class="progress_bar" style="width: <?= $_SESSION['progress'] * 10 ?>%">hoho</div>
    <p class="level_note">level: <?= $_SESSION['level'] ?></p>
    <div class=<?php if ($result == 'right') {
        echo("result_message");
    } else {
        echo("flag_result_message");
    } ?>>
        <p class="<?= $result ?>">You're <?= $result ?>!</p>
        <?php if ($result == 'wrong') {
            echo("<p class='correction'>Right answer is </p>
            <img class='flag_answer' src='" . $answer . "' alt='something went wrong... check your internet connection'>");
        }
        ?>
        <div class="next_button">
            <a class="orange_button" href="country_quiz.php">Next!</a>
        </div>
    </div>
</div>
