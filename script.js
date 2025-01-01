document.addEventListener("DOMContentLoaded", () => {
    listProcesses();
});

function listProcesses() {
    fetch("/list_processes")
        .then(response => response.json())
        .then(data => {
            const processList = document.getElementById("process-list");
            processList.innerHTML = "<h2>Processes:</h2>";
            data.forEach(proc => {
                processList.innerHTML += `<p>${proc[0]}: ${proc[1]}</p>`;
            });
        });
}

function runCommand() {
    const commandInput = document.getElementById("command-input");
    const command = commandInput.value;
    fetch("/run_command", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ command })
    })
    .then(response => response.json())
    .then(data => {
        const commandOutput = document.getElementById("command-output");
        commandOutput.textContent = data.output;
        listProcesses();
    });
}
