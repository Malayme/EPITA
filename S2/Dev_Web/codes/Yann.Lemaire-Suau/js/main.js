operations = (action, nombre1, nombre2) => {
    if (action === "addition") {
        return nombre1 + nombre2;
    } else if (action === "soustraction") {
        return nombre1 - nombre2;
    } else if (action === "multiplication") {
        return nombre1 * nombre2;
    } else if (action === "division") {
        return nombre1 / nombre2;
    }
}

function afficherResultat(action, nombre1, nombre2) {
    const resultat = operations(action, nombre1, nombre2);
    document.getElementById('resultat').innerText = `Le résultat est : ${resultat}`;
}

function calculer() {
    const nombre1 = parseFloat(document.getElementById('nombre1').value);
    const nombre2 = parseFloat(document.getElementById('nombre2').value);
    const action = document.getElementById('operation').value;
    afficherResultat(action, nombre1, nombre2);
}

//Java script pour le questionnaire

let reponses = [];
let questionIndex = 0;

const questionnaire = [
    {
        question: 'Quand le premier Monster Hunter est sorti ?',
        reponses: [
            { id: 1, reponse: '2004'},
            { id: 2, reponse: '2005'},
            { id: 3, reponse: '2006'},
            { id: 4, reponse: '2007'}
        ]
    },
    {
        question: 'Combien y\'a t-il d\'armes différentes dans le dernier opus ?',
        reponses: [
            { id: 1, reponse: '9'},
            { id: 2, reponse: '10'},
            { id: 3, reponse: '14'},
            { id: 4, reponse: '12'},
        ]
    },
    {
        question: 'Combien de vente Monster Hunter World a eu ?',
        reponses: [
            { id: 1, reponse: '12 millions'},
            { id: 2, reponse: '18 millions'},
            { id: 3, reponse: '24 millions'},
            { id: 4, reponse: '30 millions'},
        ]
    }
    //Ajouter questions
];

function afficherQuestion() {
    const questionContainer = document.getElementById('question-container');
    const questionData = questionnaire[questionIndex];

    questionContainer.innerHTML = `<h2>${questionData.question}</h2>`;

    questionData.reponses.forEach(rep => {
        const button = document.createElement('button');
        button.innerText = rep.reponse;
        button.onclick = () => enregistrerReponse(rep.id);
        questionContainer.appendChild(button);
    });
}

function enregistrerReponse(reponseId) {
    reponses.push(reponseId);
    questionIndex++;

    if (questionIndex < questionnaire.length) {
        afficherQuestion();
    } else {
        afficherResultats();
    }
}

function afficherResultats() {
    const questionContainer = document.getElementById('question-container');
    questionContainer.innerHTML = `<h2>Merci d'avoir répondu !`;
}

