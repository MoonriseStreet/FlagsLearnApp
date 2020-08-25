<?php

session_start();
require_once "util.php";

if (!isset($_SESSION['level'])) {
    $_SESSION['level'] = 'easy';
}

if (!isset($_SESSION['progress'])) {
    $_SESSION['progress'] = 0;
    $_SESSION['positive_progress'] = 0;
}

if (!isset($_SESSION['positive_progress'])) {
    $_SESSION['positive_progress'] = 0;
}

if (!isset($_SESSION['state'])) {
    $_SESSION['state'] = 'Q';
}

include('header.html');

if ($_SESSION['state'] == 'Q') {
    if (!isset($_SESSION['question'])) {
        $_SESSION['progress'] += 1;
        if ($_SESSION['progress'] == 11) {
            $_SESSION['state'] = 'R';
            header("Location: country_quiz.php");
            return;
        }
        newCountryQuestion($pdo, $_SESSION['level']);
        while (
            in_array($_SESSION['question'][0], $_SESSION['archive']) ||
            in_array($_SESSION['question'][1], $_SESSION['archive']) ||
            in_array($_SESSION['question'][2], $_SESSION['archive']) ||
            in_array($_SESSION['question'][3], $_SESSION['archive'])
        ) {
            newCountryQuestion($pdo, $_SESSION['level']);
        }
        array_push($_SESSION['archive'], $_SESSION['question']['right']);
    }

    $flags = $_SESSION['question']['flags'];
    $name = $_SESSION['question']['name'];

    if (isset($_POST['flag'])) {
        $_SESSION['answer'] = $_POST['flag'];
        $_SESSION['state'] = 'A';
        header('Location: country_quiz.php');
        return;
    }
    include('country_quiz_template.php');
} elseif ($_SESSION['state'] == 'A') {

    if ($_SESSION['question']['right'] == $_SESSION['answer']) {
        $result = 'right';
        $_SESSION['positive_progress'] += 1;
    } else {
        $result = 'wrong';
    }

    if ($result == 'wrong') {
        $answer = $_SESSION['question']['right'];
    }

    unset($_SESSION['question']);
    unset($_SESSION['answer']);
    $_SESSION['state'] = 'Q';

    include('country_result_template.php');
} elseif ($_SESSION['state'] == 'R') {
    $result = $_SESSION['positive_progress'];
    include('result_template.php');
}
include('footer.html');
?>


