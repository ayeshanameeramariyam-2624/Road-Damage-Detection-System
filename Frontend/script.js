document.querySelector("button").addEventListener("click", function () {
    const fileInput = document.querySelector('input[type="file"]');

    if (fileInput.files.length === 0) {
        alert("Please upload a road image first.");
    } else {
        alert("Image uploaded successfully! Damage detection will be connected soon.");
    }
});
