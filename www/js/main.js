/*
var image1 = document.getElementById("img#image1");
image1.addEventListener("click", function(){
  alert("Clicked " + this.target.id);
});

var image2 = document.getElementById("img#image2");
image2.addEventListener("click", function(){
  alert("Clicked " + this.target.id);
});
*/

var dinner1img=document.getElementById("dinner1");
var dinner2img=document.getElementById("dinner2");
var wrong1=document.getElementById("wrong1");
var wrong2=document.getElementById("wrong2");
var wright1=document.getElementById("wright1");
var wright2=document.getElementById("wright2");
$("div#image1, div#image2").click(function(){
console.log(this.id);
  if(this.id=='image1'){
      wright1.style.opacity = "0.8";
      wrong1.style.opacity = "0";
      wright2.style.opacity = "0";
      wrong2.style.opacity = "0.8";
     // alert("clicked dinner1");
      //setMealimages();
  }else{
      //alert("clicked dinner2");
      wright1.style.opacity = "0";
      wrong1.style.opacity = "0.8";
      wright2.style.opacity = "0.8";
      wrong2.style.opacity = "0";
      //setMealimages();
  }
  setTimeout("location.reload(true);",2000);
});

function setMealimages(){
    dinner1img.src="images/dinner1.jpg"
    dinner2img.src="images/dinner2.jpg"
}



