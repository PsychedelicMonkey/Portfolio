var viewer = document.getElementById('viewer');
var viewerClose = document.getElementById('viewer-close');
var gallery = document.getElementById('gallery');
var mainContainer = document.getElementById('main-container');
var navbarContainer = document.getElementById('navbar-container');
var viewerImg = document.getElementById('viewer-img');
var containers = document.querySelectorAll('.container');

viewerClose.addEventListener('click', function(e) {
    viewer.style.display = 'none';
    removeBlur();
});

gallery.childNodes.forEach(photo => {
    photo.addEventListener('click', function(e) {
        loadViewer(this.dataset.url);
    });
});

function loadViewer(url) {
    viewerImg.setAttribute('src', '');
    fetch(url)
    .then(response => response.json())
    .then(data => {
        viewerImg.setAttribute('src', data.url);
    });
    viewer.style.display = 'block';
    addBlur();
}

function addBlur() {
    containers.forEach(cont => {
        cont.classList.add('blur');
    });
}

function removeBlur() {
    containers.forEach(cont => {
        cont.classList.remove('blur');
    });
}