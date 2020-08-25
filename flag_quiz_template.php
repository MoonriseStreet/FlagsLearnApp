<div class="quiz_block">
    <div class="progress_bar" style="width: <?=$_SESSION['progress']*10?>%">hoho</div>
    <p class="level_note">level: <?= $_SESSION['level'] ?></p>
    <form method='POST'>
        <p class="question_title">What country does this flag belong to?</p>
        <img class="flag" src='<?=$flag?>' alt="something went wrong... check your internet connection">
        <ol class="answer_block">
            <div class="answer_row">
                <div class="answer">
                    <input class="orange_button" type='submit' value="<?=$names[0]?>" name='country'>
                </div>
                <div class="answer">
                    <input class="orange_button" type='submit' value="<?=$names[1]?>" name='country'>
                </div>
            </div>
            <div class="answer_row">
                <div class="answer">
                    <input class="orange_button" type='submit' value="<?=$names[2]?>" name='country'>
                </div>
                <div class="answer">
                    <input class="orange_button" type='submit' value="<?=$names[3]?>" name='country'>
                </div>
            </div>
        </ol>
    </form>
</div>
