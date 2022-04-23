var default_text_color = null




function validateLogin(url) {
    if (validatePassWord(password.value) && validateUserName(username.value)) {
        let xhr = new XMLHttpRequest();
        xhr.open("POST", url);
        xhr.setRequestHeader('X-CSRFToken', csrftoken)
        xhr.setRequestHeader("Accept", "application/json");
        xhr.setRequestHeader("Content-Type", "application/json");

        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4) {
                console.log(xhr.status);
                //console.log(xhr.responseText);
                document.body.innerHTML = xhr.responseText
            }
        };

        let data = JSON.stringify({
            'username': username.value,
            'passwrd': password.value
        });

        xhr.send(data);
    }
}

function validateUserName(name) {
    return /^(([[A-Z]([a-z]+))( |$))+$/.test(name)
}

function validatePassWord(pass) {
    return /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$/.test(pass)
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