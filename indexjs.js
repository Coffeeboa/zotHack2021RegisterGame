async function sendDifficulty(event) {
    event.preventDefault();

    console.log("test")

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
            alert("success");
        } else {
            alert("try again")
        }
    });

    return;
}
