$(document).ready(function()
{
       // Safely inject CSS3 and give the search results a shadow
       var cssObj = { 'box-shadow' : '#888 5px 10px 10px', // Added when CSS3 is standard
               '-webkit-box-shadow' : '#888 5px 10px 10px', // Safari
               '-moz-box-shadow' : '#888 5px 10px 10px'}; // Firefox 3.5+
       $("#suggestions").css(cssObj);

       // Fade out the suggestions box when not active
        $("input").blur(function(){
               $('#suggestions').fadeOut();
        });
});

function lookup(inputString) {
       if(inputString.length == 0) {
               $('#suggestions').fadeOut(); // Hide the suggestions box
	       $('#photobox').html('<img src="/images/blank_user_image.jpg" width="120" height="150"/>');
       } else {
               $.post("/all/js/ldap.php", {queryString: ""+inputString+""}, function(data)
{ // Do an AJAX call
                       $('#suggestions').fadeIn(); // Show the suggestions box
                       $('#suggestions').html(data); // Fill the suggestions box
               });
       }
}
//RTB Code
function updateForm(username,photo) {
	document.getElementById('inputString').value = username; // Fill in the username
	$('#photobox').html('<img src="'+ photo  +'" alt="" width="120" height="150" />'); // Show the photo	
}
