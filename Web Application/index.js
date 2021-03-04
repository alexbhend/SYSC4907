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
    
    //Are the passwords the same? 
    if(password == confirmPassword){
        passwordCheck = true;
    }
    else{
        passwordCheck = false;
    } 
    
    //Does the password have 1 upper case character? 
    if(password.length <12 && password.length >=8){
        passwordCheck = true;
    }
    else{
        passwordCheck = false;
    }
    //Does the password contain any special characters? 
    
    
    
    console.log(passwordCheck);
   
}