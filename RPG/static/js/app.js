const init = () => {
    const inputEmail = document.querySelector('#inputEmail')
    const inputPassword = document.querySelector('#inputPassword')
    const submitButton = document.querySelector('input[type= "button"]')

    window.addEventListener('input', validateInput)

    if (submitButton) {
        submitButton.addEventListener('click', (e) => {
            e.preventDefault()
            fetch('/api/v1/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    'email_login': inputEmail.value,
                    'password_login': inputPassword.value
                })
            }).then((response) => {
                if (response.ok) {
                    response.json().then((data) => {
                        //verificacao do status retornado
                        if (data.status == 200) {
                            var date = new Date();
                            date.setDate(date.getDate() + 1)// adiciona um dia
                            document.cookie= `idToke= ${data.info.idToken}; expire=Thu, ${date}; SameSite=None; Secure; path='/home.html`
                            window.location.href= "home"
                        } else {
                            document.querySelector('.errorMessage').classList.add('showErrorMessage')
                            throw Error('Email/Senha informados são invalidos.')
                        }
                    })
                } else {
                    throw Error('Comportamento inesperado na aplicação.')
                }
            }).catch((error) => {
                console.log(error)
                //document.querySelector('.errorMessage').classList.add('showErrorMessage')
            })
        })
    }
}

const validateInput = () => {
    document.querySelector('input[type= "button"]').disabled = validateInputEmail() || validateInputPassword()
    if (document.querySelector('.errorMessage').classList.contains('showErrorMessage')) {
        document.querySelector('.errorMessage').classList.remove('showErrorMessage')
    }
}

const validateInputEmail = () => {
    const emailEl = document.querySelector('#inputEmail')
    return (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(emailEl.value)) ? false : true
}

const validateInputPassword = () => {
    const passwordEl = document.querySelector('#inputPassword')
    return (passwordEl.value.length >= 8) ? false : true
}

window.onload = init