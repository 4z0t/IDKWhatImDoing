
var default_text_color = null

function validateLogin() {
    if (default_text_color === null) default_text_color =  document.getElementById("username").style.color
    var usernameStr = document.getElementById("username").value;
    var passwordStr = document.getElementById("password").value;
    console.log(usernameStr, passwordStr)
    if (/^(([[A-Z]([a-z]+))( |$))+$/.test(usernameStr)) {
        alert('success')
    }
    else
    {
        console.log("no")
        document.getElementById("username").style.color = "#ff0000"
    }
}

username.onfocus = function(event) {
    if (default_text_color !== null)
    username.style.color = default_text_color
};