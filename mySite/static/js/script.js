function updateSize(){
	var projectTile = document.querySelector("#projects .tile.is-child");
    if (window.innerWidth > 768) {
        projectTile.style.height = getComputedStyle(projectTile).width;
    } else {
        projectTile.style.height = null;
    }
}

window.onload = updateSize;
window.onresize = updateSize;
