<!DOCTYPE HTML>

<html>

<head>

<meta http-equiv="refresh" content="30; url=clock.php">

<style>

body{
   margin:0px;
}

.clock{
   width:290px;
   background-color:black; 
   -webkit-border-radius: 20px; 
   -moz-border-radius: 20px; 
   border-radius: 20px; 
   border:3px solid silver;
   text-align:center;
}

</style>

</head>


<body bgcolor="#000000">
<div class="clock">
<span style="font-size:72px;  color:white"><?php echo date('H:i'); ?></span>
</div>

</body>

</html>
