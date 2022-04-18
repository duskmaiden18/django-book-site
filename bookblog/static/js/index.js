document.querySelectorAll(".carousel").forEach(carousel => {
	const items = carousel.querySelectorAll(".carousel_item");
	const buttonHtml = Array.from(items, () => {
		return `<span class="carousel_button"></span>`;

	})

	carousel.insertAdjacentHTML("beforeend", `
		<div class="carousel_nav">
			${ buttonHtml.join("")}
		</div>
		`);

	const buttons = carousel.querySelectorAll(".carousel_button");

	buttons.forEach((button, i) => {
		button.addEventListener("click", () => {
			items.forEach(item => item.classList.remove("carousel_item--selected"));
			buttons.forEach(button => button.classList.remove("carousel_button--selected"));

			items[i].classList.add("carousel_item--selected");
			button.classList.add("carousel_button--selected");

		})
	})
	console.log(buttons);
	items[0].classList.add("carousel_item--selected");
	buttons[0].classList.add("carousel_button--selected");
})