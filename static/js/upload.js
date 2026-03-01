// Upload functionality
const fileInput = document.getElementById('fileInput');
const imagePreview = document.getElementById('imagePreview');
const previewImg = document.getElementById('previewImg');
const removeImageBtn = document.getElementById('removeImage');
const analyzeBtn = document.getElementById('analyzeBtn');
const fileName = document.getElementById('fileName');
const uploadArea = document.getElementById('uploadArea');
const uploadIcon = document.getElementById('uploadIcon');
const uploadForm = document.getElementById('uploadForm');
const uploadSection = document.getElementById('uploadSection');

// File input change event
if (fileInput) {
    fileInput.addEventListener('change', function(e) {
        const file = e.target.files[0];
        console.log('File selected:', file);
        if (file) {
            handleFileSelect(file);
        }
    });

    // Drag and drop functionality
    if (uploadArea) {
        uploadArea.addEventListener('dragover', function(e) {
            e.preventDefault();
            uploadArea.classList.add('drag-over');
        });

        uploadArea.addEventListener('dragleave', function(e) {
            e.preventDefault();
            uploadArea.classList.remove('drag-over');
        });

        uploadArea.addEventListener('drop', function(e) {
            e.preventDefault();
            uploadArea.classList.remove('drag-over');
            
            const file = e.dataTransfer.files[0];
            if (file && file.type.startsWith('image/')) {
                fileInput.files = e.dataTransfer.files;
                handleFileSelect(file);
            }
        });
    }

    // Remove image button
    if (removeImageBtn) {
        removeImageBtn.addEventListener('click', function(e) {
            e.preventDefault();
            resetUpload();
        });
    }

    // Form submit - show loading state
    if (uploadForm) {
        uploadForm.addEventListener('submit', function(e) {
            if (analyzeBtn) {
                analyzeBtn.disabled = true;
                analyzeBtn.innerHTML = `
                    <span>Analyzing...</span>
                    <div class="spinner"></div>
                `;
            }
        });
    }
}

function handleFileSelect(file) {
    console.log('Handling file:', file.name, 'Type:', file.type, 'Size:', file.size);
    
    // Validate file type
    if (!file.type.startsWith('image/')) {
        alert('Please select an image file (PNG, JPG, JPEG)');
        return;
    }

    // Validate file size (max 10MB)
    if (file.size > 10 * 1024 * 1024) {
        alert('File size must be less than 10MB');
        return;
    }

    // Show file name
    if (fileName) {
        fileName.textContent = file.name;
        fileName.style.display = 'block';
    }

    // Read and display image
    const reader = new FileReader();
    reader.onload = function(e) {
        console.log('Image loaded successfully');
        if (previewImg) {
            previewImg.src = e.target.result;
        }
        if (imagePreview) {
            imagePreview.style.display = 'flex';
        }
        if (uploadIcon) {
            uploadIcon.style.display = 'none';
        }
        if (analyzeBtn) {
            analyzeBtn.disabled = false;
            analyzeBtn.classList.add('active');
            console.log('Analyze button enabled');
        }
    };
    reader.onerror = function(error) {
        console.error('Error reading file:', error);
        alert('Error reading file. Please try again.');
    };
    reader.readAsDataURL(file);
}

function resetUpload() {
    fileInput.value = '';
    if (imagePreview) {
        imagePreview.style.display = 'none';
    }
    if (uploadIcon) {
        uploadIcon.style.display = 'block';
    }
    if (fileName) {
        fileName.textContent = '';
        fileName.style.display = 'none';
    }
    if (analyzeBtn) {
        analyzeBtn.disabled = true;
        analyzeBtn.classList.remove('active');
    }
}
