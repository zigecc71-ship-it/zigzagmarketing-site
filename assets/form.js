(function(){
  var f=document.getElementById("contact-form");
  if(!f)return;
  var err=document.getElementById("f-err"),btn=document.getElementById("f-btn"),label=btn.textContent;
  f.addEventListener("submit",function(e){
    e.preventDefault();err.textContent="";
    var bad=[];
    f.querySelectorAll("[required]").forEach(function(el){
      var v=(el.value||"").trim();
      var ok=el.type==="checkbox"?el.checked:(v!==""&&(el.type!=="email"||/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v)));
      el.classList.toggle("invalid",!ok);if(!ok)bad.push(el);
    });
    if(bad.length){err.textContent=f.getAttribute("data-msg-required");bad[0].focus();return;}
    btn.disabled=true;btn.textContent=f.getAttribute("data-msg-sending");
    fetch(f.action,{method:"POST",body:new FormData(f),headers:{"Accept":"application/json"}})
      .then(function(r){return r.json().catch(function(){return{ok:r.ok}})})
      .then(function(d){
        if(!d||!d.ok)throw new Error();
        f.hidden=true;document.getElementById("f-ok").hidden=false;
      })
      .catch(function(){
        err.textContent=f.getAttribute("data-msg-failed");
        btn.disabled=false;btn.textContent=label;
      });
  });
})();
