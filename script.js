async function search() {
    let query = document.getElementById("query").value;

    let response = await fetch(`http://127.0.0.1:8000/search?query=${query}`);
    let data = await response.json();

    let resultsDiv = document.getElementById("results");
    resultsDiv.innerHTML = "";

    data.results.forEach(caseItem => {
        let div = document.createElement("div");
        div.className = "result-card";

        div.innerHTML = `
            <h3>${caseItem.title}</h3>
            <p><b>Details:</b> ${caseItem.text}</p>
            <p><b>Court:</b> ${caseItem.court}</p>
            <p><b>Year:</b> ${caseItem.year}</p>
        `;

        resultsDiv.appendChild(div);
    });
}