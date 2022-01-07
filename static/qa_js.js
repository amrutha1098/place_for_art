function artist(){
 // var name = document.getElementById("myform").elements["name_artist"] ;
 // var name = document.getElementsByName("name_artist")[0].value;
 // document.getElementsByName("searchTxt")[0].value
 // var name = $('#name_artist').val();
 console.log(name);
 var server_data = [{
 "name" : $('#name_artist').val(),
 "art_style" : $('#art_style').val(),
 "location" : $('#location').val(),
 "age" : $('#experience').val(),
 "experience" :  $('#age').val()

}];
console.log(server_data);
$.ajax({
  type: "POST",
  url: "/artists",
  data: JSON.stringify(server_data),
  contentType: "application/json",
  dataType: 'json',
  success: function(result) {
 	 console.log("Result:");
 	 console.log(result);
  }
});
}
