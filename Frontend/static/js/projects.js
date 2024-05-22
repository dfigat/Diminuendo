function genProjects(){
    const card = document.createElement('div');
    const name = document.createElement('h3');
    const leader = document.createElement('p');
    const nextEvent = document.createElement('p');
    const deadLine = document.createElement('p');

    fetch('/api/project/')
    .then(response => response.json())
    .then(data => {
        data.forEach(project => {
            name.textContent = project.pname;
            deadLine.textContent = project.pdeadline;
            let date = new Date();
            let difference = project.pdeadLine - date;
            
            fetch(`/api/meeting/`)
            .then(response => response.json())
            .then(data => {
                console.log(data.id);
                    while(data.id != null){
                        console.log('qwerty')
                        if(date < data.meeting_date){
                            console.log('kckckckc')
                            if(data.meeting_date - date < difference){
                                difference = data.meeting_date - date;
                                nextEvent.textContent = `${data.meeting_date} ${data.meeting_time}`;
                                console.log('57567854674')
                            }
                        }
                    }
                
            })


            fetch(`/api/team/${project.id_team}`)
            .then(response => response.json())
            .then(data => { 
                    fetch(`/api/user/${data.id_leader}`)
                    .then(response => response.json())
                    .then(data => {
                            leader.textContent = `${data.fname} ${data.lname}`;
                        })
                    })
                })
            })
        
    

    card.appendChild(name);
    card.appendChild(leader);
    card.appendChild(nextEvent);
    card.appendChild(deadLine);
    document.querySelector('div').appendChild(card);
}

genProjects();

// truncate meeting
// migracje(doadanie id_meeting)
// naprawić funkję(petlę)