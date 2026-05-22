async function detectScam() {
  const msgInput = document.getElementById("message");
  const msg = msgInput.value;

  const resultBox = document.getElementById("result");
  const scanner = document.getElementById("scanningLine");

  if (!msg.trim()) {
    alert("Please enter a message to check!");
    return;
  }

  scanner.style.display = 'block';
  resultBox.classList.add("hidden");

  try {
    // Try REAL API CALL
    let data;
    try {
      const response = await fetch("http://127.0.0.1:8000/detect", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_id: 1, message: msg })
      });
      data = await response.json();
    } catch (apiError) {
      console.warn("Backend not reachable, using demo logic.");
      // DEMO FALLBACK
      await new Promise(resolve => setTimeout(resolve, 1500));
      const scamIndicators = ["urgent", "win", "lottery", "prize", "account blocked", "click this link", "otp", "refund"];
      const matches = scamIndicators.filter(ind => msg.toLowerCase().includes(ind));
      const isScam = matches.length > 0;
      data = {
        is_scam: isScam,
        risk_level: isScam ? "High" : "Low",
        reason: isScam ? `Suspicious indicators: ${matches.join(", ")}` : "No suspicious pattern detected.",
        confidence: matches.length * 20,
        suggested_action: isScam ? "⚠️ Ignore and report" : "✅ Safe message",
        timestamp: new Date().toLocaleString()
      };
    }

    resultBox.classList.remove("hidden");
    resultBox.innerHTML = `
      <div class="flex items-center justify-between mb-4">
        <div class="${data.is_scam ? 'text-red-400' : 'text-green-400'}">
          <strong>${data.is_scam ? 'Potential Scam Detected' : 'Message Appears Safe'}</strong>
        </div>
        <span class="text-sm text-gray-400">${data.timestamp}</span>
      </div>
      <div class="mb-4"><strong>Risk Level:</strong> ${data.risk_level} (${data.confidence}%)</div>
      <div class="mb-4">${data.reason}</div>
      <div class="mb-4"><strong>Action:</strong> ${data.suggested_action}</div>
    `;
  } catch (error) {
    console.error(error);
    alert("Error connecting to Rakshak AI Engine.");
  } finally {
    scanner.style.display = 'none';
  }
}

