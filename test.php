
<?php

$link = mysqli_connect("endpoint", "root", "root1234", "demo");
if ($link === false) {
    die("ERROR: Could not connect. " . mysqli_connect_error());
}

if (count($_POST) > 0){

$first_name = $_POST["first_name"]; 
$last_name = $_POST["last_name"];
$email = $_POST["email"];

$sql = "INSERT INTO persons (first_name, last_name, email) VALUES ('$first_name', '$last_name', '$email')";
if (mysqli_query($link, $sql)) {
    echo "Records added successfully.";
} else {
    echo "ERROR: Could not able to execute $sql. " . mysqli_error($link);
}

}

?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Add Record Form</title>
</head>

<body>
    <h1>Enter to insert data</h1>
    <form action="test.php" method="post">
        <p> <label for="firstName">First Name:</label> <input type="text" name="first_name" id="firstName" required> </p>
        <p> <label for="lastName">Last Name:</label> <input type="text" name="last_name" id="lastName" required> </p>
        <p> <label for="emailAddress">Email Address:</label> <input type="text" name="email" id="emailAddress" required> </p>
        <input type="submit" value="Submit" name="btn">
    </form>
    <h1>Inserted Data's</h1>

    <?php $sql = "SELECT * FROM persons";
    $result = mysqli_query($link, $sql);

    if (mysqli_num_rows($result) > 0) {
        while ($row = mysqli_fetch_assoc($result)) {
            echo "First Name: " . $row["first_name"] . " Last Name: " . $row["last_name"] . " Email: " . $row["email"] . "<br>";
        }
    } else {
        echo "0 results";
    }
    ?>
</body>

</html>
