// stylesheet links
const dark = `<link href="/static/poetica/dark_mode.css" rel="stylesheet"></link>`;  
const light = `<link href="/static/poetica/styles.css" rel="stylesheet"></link>`;
let darkmode;

window.addEventListener('load', AOS.refresh); // reference to fix divs from disapearring on reload: https://github.com/michalsnik/aos/issues/239

document.addEventListener("DOMContentLoaded", function() {
    // mobile navigation toggle
    let headerNav = document.querySelector("header nav"); 
    headerNav.classList.add("collapsed"); 
    headerNav.addEventListener("click", function() {
        headerNav.classList.toggle("collapsed"); 
    });


    darkmode = document.getElementById("switch_color");  // accesses/stores darkmode switch
    if (!localStorage.getItem("darkmode")) {             // if darkmode state isn't stored, sets it to false by default
        localStorage.setItem("darkmode", "False");    
    }

    currentMode();
});

function currentMode() {
    // checks darkmode state — set the theme when page loads
    if (localStorage.getItem("darkmode") == "False") {
        darkmode.checked = true;
        document.getElementById("logo").src = "/static/poetica/assets/light_logo.svg";  // changes to white logo
        document.getElementById("style_color").innerHTML = dark;                       // changes to darkmode stylesheet (replaces the link in html)
    } else {
        darkmode.checked = false;
        document.getElementById("logo").src = "/static/poetica/assets/dark_logo.svg";  // changes to darker logo
        document.getElementById("style_color").innerHTML = light;    // changes to lightmode stylesheet
    }
}

function changeColor() {
    // changes the theme when switch is toggled — stores state in localStorage
    if (localStorage.getItem("darkmode") == "True") {
        localStorage.setItem("darkmode", "False");
        document.getElementById("logo").src = "/static/poetica/assets/light_logo.svg";
        document.getElementById("style_color").innerHTML = dark;
    } else {
        localStorage.setItem("darkmode", "True");
        document.getElementById("logo").src = "/static/poetica/assets/dark_logo.svg";
        document.getElementById("style_color").innerHTML = light;
    }
}


function likePoem(poem_id) {
    let likes_count;
    // query for current like count for poem
    fetch("/poetica/like_poem/" + poem_id) 
        .then(response => response.json())  
        .then(data => {
            likes_count = data["likes_count"];
            console.log(likes_count);
            // toggles the like/unlike buttons
            document.getElementById("like_div_" + poem_id).style.display = "none";
            document.getElementById("like_div_" + poem_id).style.visibility = "hidden";
            document.getElementById("unlike_div_" + poem_id).style.display = "inline-block";
            document.getElementById("unlike_div_" + poem_id).style.visibility = "visible";
            document.getElementById("like_count_" + poem_id).innerHTML = likes_count;  // updates the number of likes on the page
        }).catch(e => {
            console.log(e);
        });
}

function unlikePoem(poem_id) {
    let likes_count;
    // query for current like count for poem
    fetch("/poetica/unlike_poem/" + poem_id)
        .then(response => response.json())
        .then(data => {
            likes_count = data["likes_count"];
            console.log(likes_count);
            // toggles the like/unlike buttons
            document.getElementById("unlike_div_" + poem_id).style.display = "none";
            document.getElementById("unlike_div_" + poem_id).style.visibility = "hidden";
            document.getElementById("like_div_" + poem_id).style.display = "inline-block";
            document.getElementById("like_div_" + poem_id).style.visibility = "visible";
            document.getElementById("like_count_" + poem_id).innerHTML = likes_count; // updates the number of likes on the page
        }).catch(e => {
            console.log(e);
        });
}