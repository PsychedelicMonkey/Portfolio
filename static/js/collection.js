var collections = document.querySelectorAll('.collection');

collections.forEach(collection => {
    var images = collection.childNodes[3];

    fetch(collection.dataset.icons)
        .then(response => response.json())
        .then(data => {
            data.forEach(img => {
                var icon = document.createElement('div');
                icon.style.backgroundImage = 'url(' + img.url + ')';
                images.appendChild(icon);
            });
        });

    collection.addEventListener('click', function (e) {
        window.location = this.dataset.url;
    });
});