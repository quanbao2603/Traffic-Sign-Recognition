/* ===== SWITCH TAB ===== */
function switchTab(tab) {
    document.querySelectorAll(".tab").forEach(t => t.classList.remove("active"));
    document.getElementById(`tab-${tab}`).classList.add("active");

    document.querySelectorAll(".sidebar li").forEach(li => li.classList.remove("active"));
    event.target.classList.add("active");
}

/* ===== UPLOAD ===== */
function triggerInput() {
    document.getElementById("upload-input").click();
}

function previewImage() {
    let file = document.getElementById("upload-input").files[0];
    let preview = document.getElementById("preview");

    preview.src = URL.createObjectURL(file);
    preview.style.display = "block";

    document.getElementById("upload-content").style.display = "none";
}

async function sendToAPI() {
    let file = document.getElementById("upload-input").files[0];
    if (!file) return alert("Vui lòng chọn ảnh!");

    document.getElementById("result-text").innerText = "⏳ Đang xử lý...";

    let form = new FormData();
    form.append("file", file);

    try {
        let res = await fetch("http://localhost:8000/api/predict", {
            method: "POST",
            body: form
        });

        let data = await res.json();
        document.getElementById("result-text").innerText =
            `${data.label} — ${(data.confidence * 100).toFixed(1)}%`;

    } catch {
        document.getElementById("result-text").innerText = "❌ Backend không phản hồi";
    }
}

/* ===== CAMERA ===== */
let stream = null;

async function startCamera() {
    stream = await navigator.mediaDevices.getUserMedia({ video: true });
    document.getElementById("camera").srcObject = stream;
}

function stopCamera() {
    if (!stream) return;
    stream.getTracks().forEach(t => t.stop());
}


/* ===== DARK MODE ===== */
function toggleTheme() {
    const body = document.body;

    if (body.classList.contains("dark")) {
        body.classList.remove("dark");
        body.classList.add("light");
        localStorage.setItem("theme", "light");
    } else {
        body.classList.remove("light");
        body.classList.add("dark");
        localStorage.setItem("theme", "dark");
    }
}

window.onload = () => {
    const saved = localStorage.getItem("theme") || "dark";
    document.body.classList.remove("dark", "light");
    document.body.classList.add(saved);
};
