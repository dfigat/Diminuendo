function genProjects(){
    fetch('/api/project/')
    .then(response => response.json())
    .then(data => {
        data.forEach(project => {
            const card = document.createElement('div');
            const name = document.createElement('h3');
            const leader = document.createElement('p');
            const nextEvent = document.createElement('p');
            const deadLine = document.createElement('p');
            if(project.pend == null){
                name.textContent = project.pname;
                card.appendChild(name);
                deadLine.textContent = project.pdeadline;
                fetch(`/api/team/${project.id_team}`)
                .then(response => response.json())
                .then(data => { 
                    fetch(`/api/user/${data.id_leader}`)
                    .then(response => response.json())
                    .then(data => {
                        leader.textContent = `${data.fname} ${data.lname}`;
                    })
                })
                card.appendChild(leader);
                card.appendChild(nextEvent);
                card.appendChild(deadLine);
                document.querySelector('div').appendChild(card);
            }
        })
    })
}
genProjects();
