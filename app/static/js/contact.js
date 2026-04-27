document.getElementById("admissionForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    const data = {
                    student_name: document.getElementById("name").value,
        email: document.getElementById("email").value,
              phone: document.getElementById("phone").value,

        board: document.getElementById("board").value,
        location: document.getElementById("location").value,
        message: document.getElementById("message").value
    };

    try {
        const response = await fetch("/api/admission", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        document.getElementById("responseMsg").innerText =
            result.message || result.error;

    } 
    catch (error) {
        document.getElementById("responseMsg").innerText = "Submission failed";
    }

    
});