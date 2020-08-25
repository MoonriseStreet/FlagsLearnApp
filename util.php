<?php
$pdo = new PDO('mysql:host=localhost;port=3306;dbname=misc',
    'ira', '123456789');
// See the "errors" folder for details...
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

if (isset($_SESSION['previous'])) {
    if (basename($_SERVER['PHP_SELF']) != $_SESSION['previous']) {
        unset($_SESSION['progress']);
        unset($_SESSION['positive_progress']);
        unset($_SESSION['question']);
        unset($_SESSION['answer']);
        unset($_SESSION['state']);
        unset($_SESSION['archive']);
    }
}
$_SESSION['previous'] = basename($_SERVER['PHP_SELF']);

function newFlagQuestion($pdo, $level) {
    if ($level == 'hard')
        $stmt = $pdo->prepare('SELECT name, picture FROM Countries, Complexity WHERE Countries.country_id = Complexity.country_id AND Complexity.level = 1 ORDER BY RAND() LIMIT 4');
    elseif ($level == 'medium')
        $stmt = $pdo->prepare('SELECT name, picture FROM Countries ORDER BY RAND() LIMIT 4');
    else
        $stmt = $pdo->prepare('SELECT name, picture FROM Countries, Complexity WHERE Countries.country_id = Complexity.country_id AND Complexity.level = 0 ORDER BY RAND() LIMIT 4');
    $stmt->execute(array());
    $countries = $stmt->fetchAll(PDO::FETCH_ASSOC);
    $right = rand(0, 3);
    $_SESSION['question'] = array(
        'flag' => $countries[$right]['picture'],
        'names' => array(
            $countries[0]['name'],
            $countries[1]['name'],
            $countries[2]['name'],
            $countries[3]['name']
        ),
        'right' => $countries[$right]['name']
    );
}

function newCountryQuestion($pdo, $level) {
    if ($level == 'hard')
        $stmt = $pdo->prepare('SELECT name, picture FROM Countries, Complexity WHERE Countries.country_id = Complexity.country_id AND Complexity.level = 1 ORDER BY RAND() LIMIT 4');
    elseif ($level == 'medium')
        $stmt = $pdo->prepare('SELECT name, picture FROM Countries ORDER BY RAND() LIMIT 4');
    else
        $stmt = $pdo->prepare('SELECT name, picture FROM Countries, Complexity WHERE Countries.country_id = Complexity.country_id AND Complexity.level = 0 ORDER BY RAND() LIMIT 4');
    $stmt->execute(array());
    $countries = $stmt->fetchAll(PDO::FETCH_ASSOC);
    $right = rand(0, 3);
    $_SESSION['question'] = array(
        'name' => $countries[$right]['name'],
        'flags' => array(
            $countries[0]['picture'],
            $countries[1]['picture'],
            $countries[2]['picture'],
            $countries[3]['picture']
        ),
        'right' => $countries[$right]['picture']
    );
}

function newCountry($pdo) {
    $stmt = $pdo->query("SELECT name, picture FROM Countries ORDER BY RAND() LIMIT 1");
    $row = $stmt->fetch(PDO::FETCH_ASSOC);
    $_SESSION['rand'] = $row;
}