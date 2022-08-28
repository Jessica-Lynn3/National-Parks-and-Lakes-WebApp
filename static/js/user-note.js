"use strict";

//for user note
// use fetch POST request

document.querySelector('#save-park-note').addEventListener('click', (evt) => {
    evt.preventDefault();
    alert('Victory!');

  // ajax call-> find the script in textbox and assign it to a variable. 
  // ajax call -> will send that variable, to route on the backend. 
  // whatever is returned in your server route -> will be returned to your ajax call
// document.queryselector. (whatever the div is) .inner text == response. 
    const park_code= document.querySelector('#park-code').value;

    const formInput = {
        note: document.querySelector('#park-note').value        
    };
    console.log(park_code);
    fetch(`/save-note/${park_code}`, {
        method: 'POST',
        body: JSON.stringify(formInput),
        headers: {
            'Content-Type': 'application/json',
        },
    })
        .then((response) => response.json())
        .then((responseJson) => {
            // responseJson is the response-- gives me back returned object from this route: jsonify(note_from_db.note)
            document.querySelector('#noteDisplay').innerText = responseJson;
        });
});



