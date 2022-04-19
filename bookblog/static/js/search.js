const icon = document.querySelector(".icon");
const search = document.querySelector(".search");
const search_input = document.querySelector(".input");
icon.onclick = function(){
	search.classList.toggle('active');
	search_input.classList.toggle('input-active');
}
