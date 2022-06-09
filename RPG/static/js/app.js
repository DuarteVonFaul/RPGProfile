/* || Funcao de execucao dos metodos POST dentro da pagina de login */
const initLogin = () => {
    const inputEmail = document.querySelector('#inputEmail')
    const inputPassword = document.querySelector('#inputPassword')
    const submitButton = document.querySelector('input.button')

    window.addEventListener('input', turnOfErrorMessage)

    if (submitButton) {
        submitButton.addEventListener('click', async (e) => {
            e.preventDefault()
            try {
                //trativas de erro sobre os inputs
                if (!(inputEmail.value && inputPassword.value)) {
                    throw Error('Campo email/senha vazio.')
                } else if (!(validateInputEmail() && validateInputPassword())) {
                    throw Error('Formato de entrada email/senha invalida.')
                }

                let response = await fetchUserSend('/api/v1/login', 'POST', {
                    'email_login': inputEmail.value,
                    'password_login': inputPassword.value
                })

                console.log(response)

            } catch (error) {
                showErrorMessage(error)
            }
        })
    }
}

/* || Funcao de execucao dos metodos POST dentro da pagina de cadastro */
const initRegister = () => {
    const inputEmail = document.querySelector('#inputEmail')
    const inputPassword = document.querySelector('#inputPassword')
    const submitButton = document.querySelector('input.button')

    window.addEventListener('input', turnOfErrorMessage)

    if (submitButton) {
        submitButton.addEventListener('click', (e) => {
            e.preventDefault()
            try {
                //trativas de erro sobre os inputs
                if (!(inputEmail.value && inputPassword.value)) {
                    throw Error('Campo email/senha vazio.')
                } else if (!(validateInputEmail() && validateInputPassword())) {
                    throw Error('Formato de entrada email/senha invalida.')
                }

                fetch('/api/v1/register', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        'email_register': inputEmail.value,
                        'password_register': inputPassword.value
                    })
                }).then((response) => {
                    if (response.ok) {
                        response.json().then((data) => {
                            if (data.status == 200) {
                                console.log('cadastro realizado com sucesso')
                            } else {
                                throw Error('Email/senha informados são invalidos.')
                            }
                        }).catch((error) => {
                            showErrorMessage(error)
                        })
                    } else {
                        throw Error('Comportamento inesperado na aplicação.')
                    }
                }).catch((error) => {
                    showErrorMessage(error)
                })
            } catch (error) {
                showErrorMessage(error)
            }
        })
    }
}

/* || */
const fetchUserSend = async (url, method, data) => {
    let dataReturn
    let init = {
        method: method,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    }

    await fetch(url, init)
        .then(response => response.json())
        .then(dataResponse => dataReturn = dataResponse)

    return dataReturn
}

/* || Funcoes de uso geral */
const showErrorMessage = (error) => {
    const errorMessage = document.querySelector('.errorMessage')
    errorMessage.textContent = String(error).replace('Error:', '')
    errorMessage.classList.add('showErrorMessage')
}

const turnOfErrorMessage = () => {
    const errorMessage = document.querySelector('.errorMessage')
    if (errorMessage.classList.contains('showErrorMessage')) errorMessage.classList.remove('showErrorMessage')
}

const validateInputEmail = () => {
    return (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(inputEmail.value)) ? true : false
}

const validateInputPassword = () => {
    return (inputPassword.value.length >= 8) ? true : false
}

/* || Literal object initialization */
const initialization = {
    'login': () => { initLogin() },
    'signup': () => { initRegister() }
}

/* || Chamada especifica segundo body.id da pagina atual */
window.onload = initialization[document.body.id]