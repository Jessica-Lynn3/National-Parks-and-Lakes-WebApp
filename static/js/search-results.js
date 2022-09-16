"use strict";
console.log('js is loading');

// const ACCESSIBILITY_INFO = document.querySelectorAll('#accessibility-info-hidden').value;
// console.log(ACCESSIBILITY_INFO);
// window.onload = document.querySelector('#park-accessibility-info').innerHTML = ACCESSIBILITY_INFO;fet


const searchParks = (evt) => {
    evt.preventDefault();
    const stateValue = document.querySelector('#user-selected-state').value;
    const petValue = document.querySelector('#pet-filter').checked;
    const accessValue = document.querySelector('#wh-access-filter').checked;
    
    const url = `/search-results?state=${stateValue}&pet=${petValue}&accessibility=${accessValue}`;

    fetch(url)
    .then((response) => response.json())
    .then((data) => {
        console.log(data.data);
        document.querySelector('#search-results').innerHTML = data.data.map((park) => {
            let accessibilityInfo = park.accessibilityInformation;
            const tempDiv = document.createElement("div");
            tempDiv.innerHTML = accessibilityInfo;
            accessibilityInfo = tempDiv.textContent || tempDiv.innerText;
            return (
                `<div class = "park-card">
                    <label for="park-card"></label>
                    <div class="card-body">
                        <h4>${park.title}</h4>
                        <ul>
                            <img src=${park.images[0].url || "static/images/National-Park-Service-Logo.png"} class="park-image">
                            <li> <b>Trail Webpage:</b>  <a href=${park.url}>Visit park activity website</a></li>
                            <li> <b>Trail Description:</b> ${park.shortDescription}</li>
                            <li> <b>Accessibility Information:</b>  ${accessibilityInfo}</li>
                            <li> <b>Pets Permitted:</b> ${park.arePetsPermitted}</li>
                        </ul>
                    </div>
                </div>`
            )
        })
    })
    
    // select for the all filter values
    // send a fetch request to the server with the filter values
    // get the response from the server and display in div with id of search-results
}

document.querySelector('#submit-search').addEventListener('click', searchParks)