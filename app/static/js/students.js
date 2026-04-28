// GLOBAL DATA
let studentsData = [];
let editId = null;

/* ---------------- MODAL ---------------- */

function openModal(isEdit = false) {
    if (!isEdit) {
        editId = null;
        clearForm();
    }
    document.getElementById("modal").style.display = "block";
}

function closeModal() {
    document.getElementById("modal").style.display = "none";
}

/* ---------------- LOAD DATA ---------------- */

async function loadStudents() {
    try {
        const res = await fetch("/admin/api/students");

        if (!res.ok) {
            console.log("API error");
            return;
        }

        const data = await res.json();

        studentsData = data;   // store globally
        renderTable(data);

    } catch (err) {
        console.log("Error:", err);
    }
}

/* ---------------- RENDER TABLE ---------------- */

function renderTable(data) {
    let rows = "";

    data.forEach(s => {
        rows += `
        <tr>
            <td>${s.id}</td>
            <td>${s.name}</td>
            <td>${s.age}</td>
            <td>${s.gender}</td>
            <td>${s.class}</td>
            <td>${s.batch}</td>
            <td>${s.email}</td>
            <td>${s.phone}</td>
            <td>${s.address}</td>
            <td>${s.parent}</td>
            <td>
                <button onclick="edit(${s.id})">Edit</button>
                <button onclick="del(${s.id})">Delete</button>
            </td>
        </tr>`;
    });

    document.getElementById("studentTable").innerHTML = rows;
}

/* ---------------- SAVE (CREATE / UPDATE) ---------------- */

async function saveStudent() {
    const data = {
        name: document.getElementById("name").value,
        age: document.getElementById("age").value,
        gender: document.getElementById("gender").value,
        class: document.getElementById("class_name").value,
        batch: document.getElementById("batch").value,
        email: document.getElementById("email").value,
        phone: document.getElementById("phone").value,
        address: document.getElementById("address").value,
        parent: document.getElementById("parent").value
    };

    if (editId) {
        // UPDATE
        await fetch(`/admin/api/students/${editId}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });

        editId = null;
    } else {
        // CREATE
        await fetch("/admin/api/students", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });
    }

    clearForm();
    closeModal();
    loadStudents();
}

/* ---------------- DELETE ---------------- */

async function del(id) {
    if (confirm("Delete student?")) {
        await fetch(`/admin/api/students/${id}`, {
            method: "DELETE"
        });
        loadStudents();
    }
}

/* ---------------- EDIT ---------------- */

async function edit(id) {
    editId = id;

    const res = await fetch(`/admin/api/students/${id}`);
    const data = await res.json();

    document.getElementById("name").value = data.name || "";
    document.getElementById("age").value = data.age || "";
    document.getElementById("gender").value = data.gender || "";
    document.getElementById("class_name").value = data.class || "";
    document.getElementById("batch").value = data.batch || "";
    document.getElementById("email").value = data.email || "";
    document.getElementById("phone").value = data.phone || "";
    document.getElementById("address").value = data.address || "";
    document.getElementById("parent").value = data.parent || "";

    openModal(true); // important
}

/* ---------------- CLEAR FORM ---------------- */

function clearForm() {
    document.getElementById("name").value = "";
    document.getElementById("age").value = "";
    document.getElementById("gender").value = "";
    document.getElementById("class_name").value = "";
    document.getElementById("batch").value = "";
    document.getElementById("email").value = "";
    document.getElementById("phone").value = "";
    document.getElementById("address").value = "";
    document.getElementById("parent").value = "";
}

/* ---------------- SEARCH ---------------- */

document.addEventListener("DOMContentLoaded", function () {

    document.getElementById("search").addEventListener("keyup", function () {
        const value = this.value.toLowerCase();

        const filtered = studentsData.filter(s =>
            (s.name || "").toLowerCase().includes(value) ||
            (s.class || "").toLowerCase().includes(value) ||
            (s.id || "").toString().includes(value)
        );

        renderTable(filtered);
    });

});

/* ---------------- INIT ---------------- */

window.onload = loadStudents;