var offset = 0;

function clearCalendar() {
    const calendar = document.querySelector(".week");
    while(calendar.lastElementChild != null) {
        calendar.removeChild(calendar.lastElementChild);
    }
}

function genCalendar()
{   
    const curUser = document.querySelector('#userDATA').innerText;
    const curUserId = Number(curUser);
    let date = new Date();
    date.setDate(date.getDate() - date.getDay() + 1 + offset); // Set date to the start of the week
    let dates = [];
    for(let i = 0; i < 5; i++) 
    {
        let date = new Date();
        date.setDate(date.getDate() - date.getDay() + 1 + offset); 
        let dates = [];
        for(let i = 0; i < 5; i++) 
        {
            let newDate = new Date(date);
            newDate.setDate(newDate.getDate() + i);
            dates.push(newDate.toISOString().slice(0,10));
        }
        let dateRange = `od ${dates[0]} do ${dates[6]}`;
        const week = document.createElement("tr");
        for(let i = 0; i<5;i++)
        {
            console.log("123");
            const day = document.createElement("td");
            const date = document.createElement("p");
            const content = document.createElement("p");
            fetch('/api/team-member')
                .then(response => response.json())
                .then(data => {
                    data.forEach(teamMember =>{
                        if(curUserId == teamMember.id_user)
                        {
                            console.log("jest w teamie");
                            fetch('/api/meeting/')
                            .then(response => response.json())
                            .then(data => {
                            data.forEach(meeting => {
                
                                if(meeting.meeting_date == date.textContent){
                                    content.textContent = meeting.meeting_name;
                                }
                            });
                        })
                        }
                    })
                })
                .catch(error => console.error('Error:', error));;


            




            content.textContent = "brak wydarzenia";
            date.textContent = dates[i];
            day.appendChild(date);
            day.appendChild(content);
            week.appendChild(day);
            document.querySelector(".week").appendChild(week);
        }
        
        
    }
    
}

genCalendar();
    
    function nextWeek(){
        offset +=7;
        clearCalendar();
        genCalendar();
    }
    
    function prevWeek(){
        offset -=7;
        clearCalendar();
        genCalendar();
    }
    document.querySelector("#showCalendarButton").addEventListener('click',showCalendarForm);
    function showCalendarForm()
    {
        
        const requestForm = document.querySelector("#calendarRequestForm");
        if(requestForm.style.display != 'none')
        {
            requestForm.style.display = 'none';
            
        }
        else
        {
            requestForm.style.display = 'block';
            
        }
    }

