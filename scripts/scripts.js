const api = 'http://127.0.0.1:5000';
const formEng = document.querySelector('#formEng');
const formPyg = document.querySelector('#formPyg');

formEng.addEventListener('submit', function(e){
    e.preventDefault();
    let data = {str: e.target.elements.inputEng.value};
    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data),
    };
    fetch(api + "/convert-to", options)
    .then(function (response) {
        if (response.ok) {
            return response.json();
        }
        return Promise.reject(response);
    }).then(function (data) {
        document.querySelector("#inputPyg").value = data["str"]
    }).catch(function (error) {
        console.warn('Something went wrong.', error)
    })
})

formPyg.addEventListener('submit', function(e){
    e.preventDefault();
    let data = {str: e.target.elements.inputPyg.value};
    let options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data),
    };
    fetch(api + "/convert-from", options)
    .then(function (response) {
        if (response.ok) {
            return response.json();
        }
        return Promise.reject(response);
    }).then(function (data) {
        document.querySelector("#inputEng").value = data["str"]
    }).catch(function (error) {
        console.warn('Something went wrong.', error)
    })
})