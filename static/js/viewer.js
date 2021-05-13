var viewer = document.getElementById('viewer');
var viewerClose = document.getElementById('viewer-close');
var gallery = document.getElementById('gallery');
var mainContainer = document.getElementById('main-container');
var navbarContainer = document.getElementById('navbar-container');

viewerClose.addEventListener('click', function(e) {
    viewer.style.display = 'none';
    mainContainer.classList.remove('blur');
    navbarContainer.classList.remove('blur');
});

gallery.childNodes.forEach(photo => {
    photo.addEventListener('click', function(e) {
        viewer.style.display = 'block';
        mainContainer.classList.add('blur');
    navbarContainer.classList.add('blur');
    });
});