function updateSize() {
    var projectTile = document.querySelectorAll("#projects .tile.is-child");
    projectTile.forEach( function(tile, index) {
        if (window.innerWidth > 768) {
            tile.style.height = getComputedStyle(tile).width;
        } else {
            tile.style.height = null;
        }
    })
}


window.onload = updateSize;
window.onresize = updateSize;
