var diff;
var offset = 0;
function genCalendar()
    {
        let date = new Date();
        let day = date.getDay();
        diff = (date.getDate() - day + (day == 0 ? -6:1)-offset); 
        let dates = [];
        for(let i = 0; i < 7; i++) 
        {
            let newDate = new Date(date.setDate(diff+i));
            dates.push(newDate.toISOString().slice(0,10));
        }
        let dateRange = `od ${dates[0]} do ${dates[6]}`;
        console.log(dates);
        const week = document.createElement("tr");
        for(let i = 0; i<7;i++)
        {
            const day = document.createElement("td");
            const date = document.createElement("p");
            const content = document.createElement("p");
            fetch('/api/meeting/')
                .then(response => response.json())
                .then(data => {
                data.forEach(meeting => {

                    if(meeting.meeting_date == date.textContent){
                        content.textContent = meeting.meeting_name;
                    }
                });
            })
            content.textContent = "brak wydarzenia";
            date.textContent = dates[i];
            day.appendChild(date);
            day.appendChild(content);
            week.appendChild(day);
        }
        console.log(week);
        document.querySelector(".week").appendChild(week);
    }
    genCalendar(0);

    function nextWeek(){
        offset +=7;
        genCalendar(offset);
    }
    function prevWeek(){
        offset -=7;
        genCalendar(offset);
    }