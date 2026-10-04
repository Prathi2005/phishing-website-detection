async function scanURL() {

    const url = document.getElementById("urlInput").value.trim();
    const pattern = /^(https?:\/\/)(www\.)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(\/.*)?$/;

    if (!pattern.test(url)) {
        alert("Please enter a valid URL.");
        return;
    }

    // Empty input
    if (url === "") {
        alert("Please enter a URL");
        return;
    }

    const scanBar = document.getElementById("scanBar");
    scanBar.style.display = "block";
    scanBar.classList.add("scanning");

    const resultEl = document.getElementById("result");

    resultEl.className = "";
    resultEl.innerHTML = "🔍 Analyzing Website...";

    try {

        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                url: url
            })
        });

        const data = await response.json();

        scanBar.classList.remove("scanning");
        scanBar.style.display = "none";


        document.getElementById("scoreText").innerHTML =
            "Detection Confidence: " + data.confidence + "%";

        const meter = document.getElementById("meterFill");

        meter.style.width = data.confidence + "%";

        const isLegit =
            data.prediction.includes("Legitimate");

        if (isLegit) {

            meter.style.background =
                "linear-gradient(90deg,#00ff99,#00d4ff)";
        }
        else {

            meter.style.background =
                "linear-gradient(90deg,#ff4d4d,#ff0000)";
        }

        resultEl.className =
            "status " + (isLegit ? "safe" : "danger");

        resultEl.innerHTML =
            (isLegit ? "✅ " : "⚠️ ") + data.prediction;

    }

    catch (error) {

        scanBar.classList.remove("scanning");
        scanBar.style.display = "none";

        alert("Error connecting to server");
    }
}