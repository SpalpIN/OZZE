let wishHeart = document.querySelector(`#wishheart`);
console.log(wishHeart);
clickaccfun = function (event){
	this.classList.toggle("fas");
	this.classList.toggle("far");
	this.classList.toggle("active");
	}
wishHeart.onclick = clickaccfun;