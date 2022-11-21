const retrieveData = () => {
    const xmlHttp = new XMLHttpRequest();
    const url ='http://localhost:4201/retrievedata';
    xmlHttp.open("GET", url);

    xmlHttp.send();

    xmlHttp.onreadystatechange = (e) => {
        console.log(xmlHttp.responseText)
    }
}

const newEntry = () => {
    let name = document.getElementById("name").value;
    let task = document.getElementById("task").value;
    let date = document.getElementById("date").value;

    if (name != "" && task != "" && date != "") {
        const request = new XMLHttpRequest();
        const url = 'http://localhost:4201/newentry';
        var params = 
        request.open("POST", url, true);
        request.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

        request.onreadystatechange = (e) => {
            console.log(request.responseText)
        }

        request.send("name="+name+"&task="+task+"&date="+date)
    }
    
}