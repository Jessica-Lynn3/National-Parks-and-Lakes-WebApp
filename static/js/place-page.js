"use strict";
console.log('js is loading');


const searchActivities = (evt) => {
    evt.preventDefault();
    
    const url = `/place-page`;

    fetch(url) 
    .then((response) => response.json())
    .then((data) => {
        console.log(data.data);
        document.querySelector('#trail-activity-info').innerHTML = data.data.map((activity) => {

            let accessibilityInfo = activity.accessibilityInformation;
            const tempDivAc = document.createElement("div");
            tempDivAc.innerHTML = accessibilityInfo;
            accessibilityInfo = tempDivAc.textContent || tempDivAc.innerText;

            let petInfo = activity.petsDescription;
            const tempDivPets = document.createElement("div");
            tempDivPets.innerHTML = petInfo;
            petInfo = tempDivPets.textContent || tempDivPets.innerText;

            return (
                `<div class = "park-card">
                    <label for="park-card"></label>
                    <div class="card-body">
                        <h4>${activity.title}</h4>
                        <ul>
                            <img src=${activity.images[0].url || "static/images/National-Park-Service-Logo.png"} class="park-image">
                            <li> <b>Trail/Activity Webpage:</b>  <a href=${activity.url}>Find more information on park's activity website</a></li>
                            <li> <b>Trail/Activity Description:</b> ${activity.shortDescription}</li>
  
                            <li> <b>Do fees apply?</b> ${activity.doFeesApply|title }</li>
                            <li> <b>Is a reservation required?</b> ${ activity.isReservationRequired|title }</li>
                            <li> <b>Are pets permitted?</b>  ${ activity.arePetsPermitted|title }</li>

                            <li> <b>Information about Pets:</b> ${ activity.petInfo}</li>
                            <li> <b>Accessibility Information:</b>  ${ activity.accessibilityInfo}</li> 
                        </ul>
                    </div>
                </div>`
            )
        })
    })

}

document.querySelector('#trail-info-card').addEventListener('click', searchActivities)  //there isn't really an event- just want info to be there
                                                                                        //call function without event listener?