"use strict";

// making the park code a global variable 
const PARK_CODE = document.querySelector('#park-code').value;

// when window loads call the fetchUserParkNotes function
window.onload = fetchUserParkNotes; 

function fetchUserParkNotes() {
  fetch(`/show-all-notes/${PARK_CODE}`)
  .then((response) => response.json()) 
  .then((responseJson) => {
    const userNotes = responseJson.data.reduce((result, note) => {
      result += `<li>${note}</li>`;
      return result;
    }, '');
    document.querySelector('#noteDisplay').innerHTML = userNotes;
  })
};

//for user note
// use fetch POST request

document.querySelector('#save-park-note').addEventListener('click', saveNote)

function saveNote() {
//   alert('Victory!');
  // ajax call-> find the script in textbox and assign it to a variable. 
  // ajax call -> will send that variable, to route on the backend. 
  // whatever is returned in your server route -> will be returned to your ajax call
  // document.queryselector. (whatever the div is) .inner text == response. 

  const formInput = {
      note: document.querySelector('#park-note').value        
  };

  fetch(`/save-note/${PARK_CODE}`, {
      method: 'POST',
      body: JSON.stringify(formInput),
      headers: {
          'Content-Type': 'application/json',
      },
  })
  .then((response) => response.json())
  .then((responseJson) => console.log(responseJson))
};