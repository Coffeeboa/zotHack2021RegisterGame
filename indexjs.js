
async function sendDifficulty(event) {
    event.preventDefault();

    const formData = new FormData();

var select = document.getElementById('difficulty');
var value = select.options[select.selectedIndex].value;

    formData.append("difficulty",value)

    await fetch("http://127.0.0.1:5000/update_difficulty", {
        method: 'POST',
        body: formData
    }).then(response => response.text())
    .then(data => {
        if (data === "200") {
            console.log("success");
        } else {
            console.log("try again")
        }
    });

    return;
}

async function addMoney(event,denomination) {
    event.preventDefault();

    const formData = new FormData();
    formData.append("dollarAmount",denomination)

    await fetch("http://127.0.0.1:5000/picked_more_money", {
        method: 'POST',
        body: formData
    }).then(response => response.text())
    .then(data => {
        if (data === "200") {
            console.log("success");
        } else {
            console.log("try again")
        }
    });
    returnCashUpdate()
    return;
}

async function returnCash(event) {
    event.preventDefault();

    await fetch("http://127.0.0.1:5000/submit_and_clear", {
        method: 'POST',
    }).then(response => response.text())
    .then(data => {
        returnCashUpdate()
    });

    return;
}

async function returnCashUpdate() {
    // instead of being static it should call python flask server
    await fetch("http://127.0.0.1:5000/return_current_money_picked", {
        method: 'POST',
    }).then(response => response.text())
    .then(data => {
       document.getElementById("moneyReturnAmount").innerHTML = data;
    });



    return;
}

async function alertTest() {
    alert("alert test")



    return;
}