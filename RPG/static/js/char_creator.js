const cardsEl = document.querySelector('.cards')
const cardEl = document.querySelector('.cards > .card')
const buttonsEl = document.querySelectorAll('.changeButton > button')



buttonsEl[0].addEventListener('click', (e) => {
    if (cardsEl.classList.contains('running'))  return
    cardsEl.classList.add('running')
    setTimeout(() => {
        cardsEl.classList.remove('running')
    }, 351)
    cardsEl.style.left = `${cardsEl.offsetLeft + cardEl.offsetWidth + 20}px`
})

buttonsEl[1].addEventListener('click', (e) => {
    if (cardsEl.classList.contains('running'))  return
    cardsEl.classList.add('running')
    setTimeout(() => {
        cardsEl.classList.remove('running')
    }, 351)
    cardsEl.style.left = `${cardsEl.offsetLeft - cardEl.offsetWidth - 20}px`
})

console.log(cardsEl.offsetWidth, cardsEl.offsetHeight, cardsEl.offsetLeft)