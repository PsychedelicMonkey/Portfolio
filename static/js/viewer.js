var viewer = document.getElementById('viewer');
var viewerClose = document.getElementById('viewer-close');
var gallery = document.getElementById('gallery');
var mainContainer = document.getElementById('main-container');
var navbarContainer = document.getElementById('navbar-container');
var viewerImg = document.getElementById('viewer-img');
var containers = document.querySelectorAll('.container');

var galleryItems = document.querySelectorAll('.gallery-item');
var leftBtn = document.getElementById('left-btn');
var rightBtn = document.getElementById('right-btn');

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
    setButtons(url);

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

function setButtons(url) {
    var self = document.querySelector(`[data-url="${url}"]`);
    var next = self.nextSibling.nextSibling;
    var prev = self.previousSibling.previousSibling;

    if (prev != null) {
        leftBtn.setAttribute('data-prevurl', prev.dataset.url);
        leftBtn.style.display = 'block';
    }
    else {
        leftBtn.style.display = 'none';
    }

    if (next != null) {
        rightBtn.setAttribute('data-nexturl', next.dataset.url);
        rightBtn.style.display = 'block';
    }
    else {
        rightBtn.style.display = 'none';
    }
}

leftBtn.addEventListener('click', function(e) {
    if (this.dataset.prevurl)
        loadViewer(this.dataset.prevurl);
});

rightBtn.addEventListener('click', function(e) {
    if (this.dataset.nexturl)
        loadViewer(this.dataset.nexturl);
});

window.onclick = function(e) {
    if (e.target == viewer) {
        viewer.style.display = 'none';
        removeBlur();
    }
}