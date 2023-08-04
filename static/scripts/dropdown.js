window.onload = function () {
    let dropdownAnchors = document.getElementsByClassName("dropdown-anchor");

    for (let i = 0; i < dropdownAnchors.length; i++) {
        let id = dropdownAnchors[i].getAttribute("data-id");
        let dropdownContent = document.getElementById(id);
        dropdownContent.style.maxHeight = "0px";
        dropdownAnchors[i].addEventListener("click", function () {
            if (dropdownContent.style.maxHeight !== "0px") {
                dropdownContent.style.maxHeight = "0px";
            } else {
                dropdownContent.style.maxHeight = dropdownContent.scrollHeight + "px";
            }
        });
    }
}