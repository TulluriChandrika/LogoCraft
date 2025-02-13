async function generateLogo() {
    const description = document.getElementById("description").value;
    if (!description) {
        alert("Please enter a description.");
        return;
    }

    document.getElementById("loading").style.display = "block";
    document.getElementById("logoContainer").style.display = "none";

    const response = await fetch('http://localhost:5000/generate_logo', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ description: description })
    });

    const data = await response.json();

    if (data.success) {
        const logoUrl = data.logo_url;
        document.getElementById("generatedLogo").src = logoUrl;
        document.getElementById("logoContainer").style.display = "block";
    } else {
        alert("Error generating logo.");
    }

    document.getElementById("loading").style.display = "none";
}