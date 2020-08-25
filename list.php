<?php

session_start();
require_once "util.php";

$stmt = $pdo->query("SELECT name, picture FROM Countries" );
$rows = $stmt->fetchAll(PDO::FETCH_ASSOC);

include('header.html');
?>

<div class="list_box">
    <ul class="list_of_countries">
        <?php
        foreach ($rows as $row) {
            echo "<li class=\"country_item\">";
            echo "<p class=\"country\">".$row['name']."</p>";
            echo "<img class=\"flag\" src=\"".$row['picture']."\"  \
            alt=\"something went wrong... check your internet connection\">";
            echo "</li>";
        }
        ?>
    </ul>
</div>

<?php
include('footer.html')
?>