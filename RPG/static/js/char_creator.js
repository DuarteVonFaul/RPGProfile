const cardSlider = document.querySelector('.cardSlider')
const cards = document.querySelector('.cardSlider .cards')
const card = document.querySelector('.cardItem')
const controlButtons = document.querySelectorAll('.prevButton, .nextButton')

//botao prev
controlButtons[0].addEventListener('click', () => {
    if (!sliderPrevent()) return
    cards.style.top = `${cards.offsetTop + card.getBoundingClientRect().height}px`;

    setTimeout(boundCards, 200)
    setTimeout(setupButtons, 250)
})

//botao next
controlButtons[1].addEventListener('click', () => {
    if (!sliderPrevent()) return
    if (!checkIndexValues()) {
        //throw error
        return
    }
    cards.style.top = `${cards.offsetTop - card.getBoundingClientRect().height}px`

    setTimeout(boundCards, 200)
    setTimeout(setupButtons, 251)
})

//impede que os botoes sejam pressionados repetidamente e quebrem o layout
function sliderPrevent() {
    if (cards.classList.contains('running')) return false
    cards.classList.add('running')
    setTimeout(() => { cards.classList.remove('running') }, 250)
    return true
}

//remove os botoes prev/next dependendo da secao 
function setupButtons() {
    if (parseInt(cards.style.top) == 0 || cards.offsetTop == 0) {
        controlButtons[0].classList.add('hideButton')
    } else {
        controlButtons[0].classList.remove('hideButton')
    }
}

//limita o trafego pela pagina usando botoes
function boundCards() {
    const cardSliderRect = cardSlider.getBoundingClientRect()
    const cardsRect = cards.getBoundingClientRect()

    if (parseInt(cards.style.top) > 0) {
        cards.style.top = 0;
    } else if (cardsRect.bottom < cardSliderRect.bottom) {
        cards.style.top = `${cardSliderRect.height - cardsRect.height}px`
    }
}

//informa o numero da secao atual
function sectionPosition() {
    let sectionPosition
    sectionPosition = parseInt(cards.style.top) / 812 ? parseInt(cards.style.top) / 812 : parseInt(cards.offsetTop) / 812
    sectionPosition = sectionPosition < 0 ? -sectionPosition : sectionPosition
    return sectionPosition
}

//todos os metodos de verificao dos valores nos inputs
const sectionValidations = {
    0: () => {
        const inputName = document.querySelector('#nameSection input[type= "text"]')
        return inputName.value
    },
    1: () => {
        const selectedRace = document.querySelector('#raceSection .slider [type="radio"]:checked')
        return selectedRace
    },
    2: () => {
        return true
    },
    3: () => {
        return true
    }
}

//verificando o opcao escolhida pelo usuario
function checkIndexValues() {
    return sectionValidations[sectionPosition()]() ? true : false
}

//setando os possiveis historicos de acordo com a raca escolhida
function showHistorical(){
    
}

//campo referente a logica de preenchimento do campo de racas
const raceOptions = document.querySelectorAll('#raceSection .slider [type="radio"]')

for (let i = 0; i < raceOptions.length; i++) {
    raceOptions[i].addEventListener('click', racesInfos)
}

function racesInfos() {
    const races = {
        'human': () => { showRaceInfos('humano') },
        'elf': () => { showRaceInfos('elfo') },
        'dwarf': () => { showRaceInfos('Anão') },
        'qunari': () => { showRaceInfos('Qunari') }
    }
    const selectedRace = document.querySelector('#raceSection .slider [type="radio"]:checked')
    races[selectedRace.dataset.race]()
}

function showRaceInfos(info) {
    document.querySelector("#raceSection .sliderDescription").classList.remove('showSlider')
    //criando elemento filho e preenchendo com as caracteristicas da raca
    let infos = document.createElement('div')
    let title = document.createElement('h3')
    let text = document.createElement('p')

    title.textContent = info
    text.textContent = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'

    infos.append(title, text)

    setTimeout(() => {
        document.querySelector("#raceSection .sliderDescription").replaceChildren(infos)
        document.querySelector("#raceSection .sliderDescription").classList.add('showSlider')
    }, 250);
}

//setando algumas tratativas no inico do load da pagina
function init() {
    setupButtons()
    racesInfos()
}

window.onload = init