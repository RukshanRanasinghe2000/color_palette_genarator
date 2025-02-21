const btnUpload = document.getElementById('btn-upload');

        document.getElementById('fileInput').addEventListener('change', function(event) {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    document.getElementById("image-preview").innerHTML = `<img src="${e.target.result}" class="max-w-md h-250 max-h-250 mt-2">`;
                };
                reader.readAsDataURL(file);
                btnUpload.classList.remove('invisible');
            }
        });

        function handleUpload(event) {
            event.preventDefault();
            const formData = new FormData();
            const fileInput = document.getElementById('fileInput');
            if (fileInput.files.length === 0) return;
            formData.append("file", fileInput.files[0]);

            fetch("http://127.0.0.1:8000/api/image_upload/", {
                method: "POST",
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                displayColors(data);
            })
            .catch(error => console.error("Error uploading image:", error));
        }

        function displayColors(colorData) {
            const colorGrid = document.getElementById('color-grid');
            colorGrid.innerHTML = '';
            Object.keys(colorData).forEach(key => {
                const hex = colorData[key].Hex;
                const colorBox = document.createElement("div");
                colorBox.className = "color-box";
                colorBox.style.backgroundColor = hex;
                colorBox.textContent = hex;
                colorGrid.appendChild(colorBox);
            });
        }