
<?php
        $servername = "localhost";
        $username = "Tegveer";
        $password = "**********";
        $dbname = "population_tracker";

        // Create connection
        $conn = new mysqli($servername, $username, $password, $dbname);

        // Check connection
        if ($conn->connect_error) {
                die("Connection failed: " . $conn->connect_error);
        } else {
                echo "<body style = 'background: grey; font-family: calibri;'><br>";
                echo "<h1 style='font-size: 3em; margin-left: 10px; padding: none'>Population Tracking System</h1>";
        }

        $sql = "SELECT * FROM sensor_data";
        $result = $conn->query($sql);

        echo("<h2 style='margin-left: 10px; padding: none;'>Current Occupancy</h2><br>");
        echo("<h1 style='margin-left: 10px; font-size: 2em; padding: none;'>".$result->num_rows."</h1>");
        if ($result->num_rows > 0) {
                echo "<table style='background: white; border: solid 1pt black; padding: 2px; margin: 10px 10px 10px 10px; margin-collapse: collapse;'>";
                echo "<tr><th>ID</th><th>Distance from Sensor</th><th>Time entered</th></tr>";
                // output data of each row
                while($row = $result->fetch_assoc()) {
                        echo "<tr><td style='text-align: center;'>".$row["id"]."</td><td style='text-align: center;'>".$row["distance"]."</td><td style='text-align: center'>".$row["time_passed"]."</td></tr>";
                }
                echo "</table></body>";
        } else  {
                echo "0 results";
        }
        $conn->close();

?>
