const api = '127.0.0.1:5000'

// let btn1 = document.querySelector()

document.querySelector('#formEng').addEventListener('submit', function(e){
    e.preventDefault();
    let data = e.target.elements.inputEng.value
    console.log(data);
    console.log(JSON.stringify(data));
    // let options = {
    //     method: 'GET',
    //     headers: {
    //         'Content-Type': 'application/json'
    //     },
    //     body: JSON.stringify(data),
    // };

    // fetch(api, options);
})

document.querySelector('#formPyg').addEventListener('submit', function(e){
    e.preventDefault();
    let data = e.target.elements.inputPyg.value
    console.log(data)
})