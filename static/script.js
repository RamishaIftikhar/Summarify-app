// Summarize Text function
async function summarizeText() {
    const text = document.getElementById("inputText").value;
    if (!text.trim()) {
        alert("Please enter some text!");
        return;
    }
    const response = await fetch("/summarize", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: text })
    });

    const data = await response.json();
    document.getElementById("summary").innerText = data.summary || "Error: " + data.error;
}

function readSummary() {
    const summary = document.getElementById("summary").innerText;
    if (!summary.trim()) {
        alert("No summary to read!");
        return;
    }
    const utterance = new SpeechSynthesisUtterance(summary);
    window.speechSynthesis.speak(utterance);
}

// Download Summary function
function downloadSummary() {
    const summary = document.getElementById("summary").innerText;
    if (!summary.trim()) {
        alert("No summary to download!");
        return;
    }
    const blob = new Blob([summary], { type: "text/plain;charset=utf-8" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "summary.txt";
    link.click();
}


function clearText() {
    document.getElementById("inputText").value = '';  
    document.getElementById("summary").innerText = ''; 
}
