const retrieveData = () => {
    const xmlHttp = new XMLHttpRequest();
    const url ='http://localhost:4201/retrievedata';
    xmlHttp.open("GET", url);

    xmlHttp.send();

    xmlHttp.onreadystatechange = (e) => {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
            let json = JSON.parse(xmlHttp.responseText)
            let div = document.getElementById("data")
            for (i = 0; i< json.lTareas.length; i++) {
                agregarDatos(json.lTareas[i].name, json.lTareas[i].task, json.lTareas[i].date)
            }
        }
    }
}

const agregarDatos = (name, task, date) => {
    div = document.getElementById("data")
    const node = document.createElement("li");
    const textnode = document.createTextNode(name + ", " + task+ ", " + date);
    node.appendChild(textnode)
    div.appendChild(node)
}

const newEntry = () => {
    let name = document.getElementById("name").value;
    let task = document.getElementById("task").value;
    let date = document.getElementById("date").value;

    if (name != "" && task != "" && date != "") {
        const request = new XMLHttpRequest();
        const url = 'http://localhost:4201/newentry';
        request.open("POST", url, true);
        request.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

        request.onreadystatechange = (e) => {
            if (request.readyState == 4 && request.status == 200) {
                agregarDatos(name, task, date)
                alert("Success")
            }
        }

        request.send("name="+name+"&task="+task+"&date="+date)
    }
    
}