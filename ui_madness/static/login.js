var default_text_color = null

function validateLogin() {

}

function validateUserName(name) {
    return /^(([[A-Z]([a-z]+))( |$))+$/.test(name)
}

function validatePassWord(password) {
    return /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$/.test(password)
}

username.addEventListener('focus', (event) => {
  if (default_text_color === null)
        default_text_color = username.style.color
    else
        username.style.color = default_text_color
});

username.addEventListener('blur', (event) => {
  if (validateUserName(username.value)) {
        username.style.color = default_text_color
    } else {
        username.style.color = "#ff0000"
    }
});

password.addEventListener('focus', (event) => {
  if (default_text_color === null)
        default_text_color = password.style.color
    else
        password.style.color = default_text_color
});

password.addEventListener('blur', (event) => {
  if (validatePassWord(password.value)) {
        password.style.color = default_text_color
    } else {
        password.style.color = "#ff0000"
    }
});