<div class="quiz_block">
    <div class="progress_bar" style="width: <?=$_SESSION['progress']*10?>%">hoho</div>
    <p class="level_note">level: <?= $_SESSION['level'] ?></p>
    <div class="result_message">
        <p class="<?= $result ?>">You're <?= $result ?>!</p>
        <?php
        if ($result == 'wrong') {
            echo "<p class='correction'>Right answer is " . $answer . "</p>";
        }
        ?>
        <div class="next_button">
            <a class="orange_button" href="flag_quiz.php">Next</a>
        </div>
    </div>
</div>
