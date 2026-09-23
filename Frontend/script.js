const fileInput = document.getElementById("imageInput");
const detectBtn = document.getElementById("detectBtn");
const resultDiv = document.getElementById("result");

fileInput.addEventListener("change", function () {
    if (fileInput.files.length > 0) {
        resultDiv.innerHTML = "Image selected successfully.";
    } else {
        resultDiv.innerHTML = "";
    }
});

detectBtn.addEventListener("click", function () {
    if (fileInput.files.length === 0) {
        resultDiv.innerHTML = "Please select a road image first.";
        return;
    }

    resultDiv.innerHTML = "Image selected. Ready for detection.";
});
