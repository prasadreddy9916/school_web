// GLOBAL
let facultyData = [];
let editId = null;

/* ---------------- MODAL ---------------- */

function openModal(isEdit = false) {
    if (!isEdit) {
        editId = null;
        clearForm();
    }
    document.getElementById("modal").style.display = "flex";
    
}

function closeModal() {
    document.getElementById("modal").style.display = "none";
}

/* ---------------- LOAD ---------------- */

async function loadFaculty() {
    try {
        const res = await fetch("/admin/api/faculty");

        if (!res.ok) {
            console.log("API error");
            return;
        }

        const data = await res.json();

        facultyData = data;
        renderTable(data);

    } catch (err) {
        console.log("Error:", err);
    }
}

/* ---------------- RENDER ---------------- */

function renderTable(data) {
    let rows = "";

    data.forEach(f => {
        rows += `
        <tr>
            <td>${f.name}</td>
            <td>${f.phone}</td>
            <td>${f.location}</td>
            <td>${f.subject}</td>
            <td>
                ${f.class1}<br>
                ${f.class2}<br>
                ${f.class3}<br>
                ${f.class4}<br>
                ${f.class5}<br>
                ${f.class6}
            </td>
            <td>
                <button onclick="editFaculty(${f.id})">Edit</button>
                <button onclick="deleteFaculty(${f.id})">Delete</button>
            </td>
        </tr>`;
    });

    document.getElementById("facultyTable").innerHTML = rows;
}

/* ---------------- SAVE ---------------- */

async function saveFaculty() {
    const data = {
        name: document.getElementById("name").value,
        phone: document.getElementById("phone").value,
        location: document.getElementById("location").value,
        subject: document.getElementById("subject").value,

        class1: document.getElementById("class1").value,
        class2: document.getElementById("class2").value,
        class3: document.getElementById("class3").value,
        class4: document.getElementById("class4").value,
        class5: document.getElementById("class5").value,
        class6: document.getElementById("class6").value
    };

    if (editId) {
        // UPDATE
        await fetch(`/admin/api/faculty/${editId}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });

        editId = null;
    } else {
        // CREATE
        await fetch("/admin/api/faculty", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });
    }

    clearForm();
    closeModal();
    loadFaculty();
}

/* ---------------- DELETE ---------------- */

async function deleteFaculty(id) {
    if (!confirm("Delete faculty?")) return;

    await fetch(`/admin/api/faculty/${id}`, {
        method: "DELETE"
    });

    loadFaculty();
}

/* ---------------- EDIT ---------------- */

async function editFaculty(id) {
    editId = id;

    const res = await fetch(`/admin/api/faculty/${id}`);
    const f = await res.json();

    document.getElementById("name").value = f.name || "";
    document.getElementById("phone").value = f.phone || "";
    document.getElementById("location").value = f.location || "";
    document.getElementById("subject").value = f.subject || "";

    document.getElementById("class1").value = f.class1 || "";
    document.getElementById("class2").value = f.class2 || "";
    document.getElementById("class3").value = f.class3 || "";
    document.getElementById("class4").value = f.class4 || "";
    document.getElementById("class5").value = f.class5 || "";
    document.getElementById("class6").value = f.class6 || "";

    openModal(true);
}

/* ---------------- CLEAR ---------------- */

function clearForm() {
    document.getElementById("name").value = "";
    document.getElementById("phone").value = "";
    document.getElementById("location").value = "";
    document.getElementById("subject").value = "";

    document.getElementById("class1").value = "";
    document.getElementById("class2").value = "";
    document.getElementById("class3").value = "";
    document.getElementById("class4").value = "";
    document.getElementById("class5").value = "";
    document.getElementById("class6").value = "";
}

/* ---------------- SEARCH ---------------- */

document.addEventListener("DOMContentLoaded", function () {

    const searchInput = document.querySelector(".top-bar input");

    searchInput.addEventListener("keyup", function () {
        const value = this.value.toLowerCase();

        const filtered = facultyData.filter(f =>
            (f.name || "").toLowerCase().includes(value) ||
            (f.subject || "").toLowerCase().includes(value) ||
            (f.location || "").toLowerCase().includes(value)
        );

        renderTable(filtered);
    });

});

/* ---------------- INIT ---------------- */

window.onload = loadFaculty;