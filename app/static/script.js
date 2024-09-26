let timeout = null;
        
function submitForm() {
   clearTimeout(timeout); 
   timeout = setTimeout(() => {
      document.getElementById('ncol-form').submit();
   }, 500);
}
   