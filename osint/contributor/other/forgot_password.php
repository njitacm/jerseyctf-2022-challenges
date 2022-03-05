<?php
define("USERNAME", "DRodgers");
define("FLAG", "jctf{b3_CAR3fu1_wh@t_yOU_put_on_the_WEB}");
$questions = [
    "q1" => [
        "q" => "What was your first job's company name?",
        "a" => "Bank Heist Security 101"
    ],
    "q2" => [
        "q" => "What city was your high school located in?",
        "a" => "Rahway",
    ],
    "q3" => [
        "q" => "What is your favorite sport?",
        "a" => "Arm wrestling"
    ]
];

function showFirstForm()
{
?>
    <form action="" method="post">
        <label>Username
            <input type="text" name="username">
        </label>
        <input type="submit" value="Continue" name="submit">
    </form>
<?php
}

function showSecondForm()
{
    global $questions;
?>
    <h2>Security Questions</h2>
    <form action="" method="post">
        <?php
        foreach ($questions as $question_id => $question) { ?>
            <label><?php echo $question["q"]; ?>
                <input type="text" name="<?php echo $question_id; ?>">
            </label>
            <br>
        <?php } ?>
        <input type="submit" value="Reset Password" name="submit">
    </form>
<?php
}

function scriptAlert($msg)
{
?>
    <script>
        alert("<?php echo $msg; ?>");
    </script>
    <noscript>
        <p>
            <?php echo $msg; ?>
        </p>
    </noscript>
<?php
}
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Forgot Password</title>
</head>

<body>
    <h1>Forgot Password</h1>

    <?php
    if (isset($_POST["submit"])) {
        // 1st "public" layer of form
        if (isset($_POST["username"])) {
            if ($_POST["username"] === USERNAME) {
                showSecondForm();
            } else if ($_POST["username"] === "Wolverine") {
            	showFirstForm();
                scriptAlert("Nice try! Find another user.");
            } else {
                showFirstForm();
            }
        }
        // 2nd form is "secret", know by checking the form input names
        else if (count(array_intersect_key($questions, $_POST)) === count($questions)) {
            $missed_question = null;
            foreach ($questions as $question_id => $question) {
                if ($_POST[$question_id] !== $question["a"]) {
                    $missed_question = $question;
                    break;
                }
            }
            if ($missed_question === null) {
                showFirstForm();
                scriptAlert(FLAG);
            } else {
                showSecondForm();
                scriptAlert("Incorrect Answer(s)");
            }
        }
    } else {
        showFirstForm();
    } ?>
</body>

</html>
