const retrieveData = () => {
    const xmlHttp = new XMLHttpRequest();
    const url ='http://localhost:4201/retrievedata';
    xmlHttp.open("GET", url);

    xmlHttp.send();

    xmlHttp.onreadystatechange = (e) => {
        console.log(xmlHttp.responseText)
    }
}