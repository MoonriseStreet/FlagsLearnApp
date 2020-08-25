<div class="quiz_block">
    <div class="progress_bar" style="width: <?= $_SESSION['progress'] * 10 ?>%">hoho</div>
    <p class="level_note">level: <?= $_SESSION['level'] ?></p>
    <form method='POST'>
        <p class="question_title">What flag does <?=$name?> have?</p>
        <ol class="answer_block">
            <div class="answer_row">
                <div class="answer">
                    <input class="flag_button" type='submit' value="<?=$flags[0]?>" name='flag'
                           style="background-image: url(<?=$flags[0]?>);"/>
                </div>
                <div class="answer">
                    <input class="flag_button" type='submit' value="<?=$flags[1]?>" name='flag'
                           style="background-image: url(<?=$flags[1]?>);"/>
                </div>
            </div>
            <div class="answer_row">
                <div class="answer">
                    <input class="flag_button" type='submit' value="<?=$flags[2]?>" name='flag'
                           style="background-image: url(<?=$flags[2]?>);"/>
                </div>
                <div class="answer">
                    <input class="flag_button" type='submit' value="<?=$flags[3]?>" name='flag'
                           style="background-image: url(<?=$flags[3]?>);"/>
                </div>
            </div>
        </ol>
    </form>
</div>