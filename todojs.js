let input=document.querySelector("input");
let btn=document.querySelector("button");
let ull=document.querySelector("ul");

  btn.addEventListener("click", function (){
    let i=document.createElement("li");
    i.innerText=input.value;
     let del=document.createElement("button");
     del.innerText="delete";
     del.classList.add("delete");
         i.appendChild(del);
        
          ull.appendChild(i);
          input.value=" ";
  })
  //let dell=document.querySelectorAll(".delete");
  // for(btns of dell){
  //   btns.addEventListener("click",function(){
  //     let par=this.parentElement;
  //     par.remove();
  //   })  
  // }
  ull.addEventListener("click",function(event){
    if(event.target.nodeName=="BUTTON"){
      let ff=event.target.parentElement;
      ff.remove();
    }
  })