$('.message a').click(function(){
   $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
});



$("#reg_form").on("submit",function(){
   var values = $(this).serializeArray();
   
   var udata = {"name":values[0]["value"],"password":values[1]["value"],"email":values[2]["value"],}
  
   $.ajax({
      url:"http://localhost:5000/create_user",
      type:"POST",
      data:JSON.stringify(udata),
      dataType:"JSON",
      contentType: "application/json; charset=utf-8",
      success:function(data){
         alert("user created!")
         console.log(data)
        
      }
      

      
   })


})

$("#login_form").on("submit",function(){
   var values = $(this).serializeArray();
   var udata = {"name":values[0]["value"],"password":values[1]["value"]}
   $.ajax({
      url:"http://localhost:5000/login_user",
      type:"POST",
      data:JSON.stringify(udata),
      dataType:"JSON",
      contentType: "application/json; charset=utf-8",
      success:function(data){
         alert(data["status"])
         
        
      }
      

      
   })
})