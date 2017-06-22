 <html>
 <head>
 <title>DOOR</title>
 </head>
         <body>
         Dope Door Opener:
	<form method="get" action="index.php">
                 <input type="submit" value="ON" name="on">
                 <input type="submit" value="OFF" name="off">
         </form>
         <?php
         if(isset($_GET['on'])){
                 exec('sudo python /home/pi/my_python/test1.py');
                 echo "Door Opened";
         }
         else if(isset($_GET['off'])){
                 exec('sudo python /home/pi/my_python/test.py');
                 echo "Door Closed";
         }
         ?>
         </body>
 </html>
