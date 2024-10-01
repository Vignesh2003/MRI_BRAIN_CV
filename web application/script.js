document.getElementById('fileInput').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById('imagePreview').src = e.target.result;
            document.getElementById('imagePreview').style.display = 'block';
        };
        reader.readAsDataURL(file);
    }
});

document.getElementById('processButton').addEventListener('click', function() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    
    if (!file) {
        alert("Please upload a .tif image file before processing.");
        return;
    }

    // Create FormData to send the image to the backend
    const formData = new FormData();
    formData.append('file', file);

    // Replace 'http://localhost:8000/process' with your actual backend endpoint
    fetch('http://localhost:8000/process', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Assuming the response has a key 'mask_url' which contains the predicted mask image URL
        const maskUrl = data.mask_url;

       
