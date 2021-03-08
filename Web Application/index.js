 //Function checks whether or not the password meets the password policy set for the site
function validatePassword(){
    var firstName = document.getElementById('fname').value;
    var lastName = document.getElementById('lname').value;
    var email = document.getElementById('inputEmail').value;
    var confirmEmail = document.getElementById('inputCEmail').value;
    
    var password = document.getElementById('inputPassword').value;
    var confirmPassword = document.getElementById('inputCPassword').value;
    
    var passwordCheck = true;
    
//Check if the password satisfies the policy
// Password should include at least 1 uppercase, 1 lowercase, 1 number,
// 1 special character and at least 8 characters
    
    //Are the passwords the same? 
    if(password == confirmPassword){
        passwordCheck = true;
    }
    else{
        passwordCheck = false;
        alert("Password does not match. Please try again");
    } 
 
    //Does the password have at least 8 characters?
    if(password.length >= 8){
        passwordCheck = true;
    }
    else{
        passwordCheck = false;
		      alert("Password needs at least 8 characters");
    }
 
    //Does the password have at least 1 lowercase character
	   var lowerCase = /[a-z]/;
	
	   if(password.match(lowerCase)){
		      passwordCheck = true;
   	}
	   else{
		      passwordCheck = false;
		      alert("Password needs at least 1 lowercase letter");
	   }
 
    //Does the password have 1 upper case character? 
    var upperCase = /[A-Z]/;
	
	   if(password.match(upperCase)){
		       passwordCheck = true;
	   }
	   else{
		       passwordCheck = false;
		       alert("Password needs at least 1 uppercase letter");
	   }
   
    //Does the password contain at least one number?
    var numbers = /[0-9]/;
	
	   if(password.match(numbers)){
		      passwordCheck = true;
	   } 
    else{
		      passwordCheck = false;
		      alert("Password needs at least 1 number");
	   }
	
	   //Does the password contain any special characters? 
    var specialChar = /[!@#$%^&*]/;
	
	   if(password.match(specialChar)){
		       passwordCheck = true;
	   }
	   else{
		       passwordCheck = false;
		       alert("Password needs at least 1 special character out of the following:(!@#$%^&*)");
   	}
	
	   //Do the emails match one another?
	   if(email == confirmEmail){
		       emailCheck = true;
	   } 
    else {
		       emailCheck = false;
		       alert("Email does not match");
	   }
	
	   //Is the email and password confirmed?
   	if(passwordCheck == emailCheck){
		       return true;
	   } 
    else {
		       return false;
		       alert("Form incomplete!");
	   }
   
}
