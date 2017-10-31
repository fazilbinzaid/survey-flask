$(function() {

  // var BASE_URL = "http://localhost:5000/api/"
  var BASE_URL = "https://test-survey-flask.herokuapp.com/api/";

  $.ajax({
    url: BASE_URL + "questions",
    type: "GET",
    contentType: "application/json",
    dataType: "json",
    success: function(response) {
      console.log("response", response);
      renderQuestions(response.data);
    }
  });

  function renderQuestions(data) {

    var li = '';

    data.forEach(function(each) {
      var h3 = '<div class="form-group"><h3>' + each.question.text + '</h3></div>';

      each.choices.forEach(function(choice, index) {
        var div = '<div><input type="radio" name="  ' + each.question.id + '" id="question-' + each.question.id + '-answers-' + index + '" value="' + choice.id + '" /><label for="question-' + each.question.id + '-answers-' + index + '">' + index + ') ' + choice.text + '</label></div>';
        h3 += div;
      });

      console.log("h3", h3);

      li += '<div class="form-group"><li>' + h3 + '</li></div>';

    });

    var $li = $(li).appendTo('#orderedList');
  }

  $("#quiz").submit(function(e) {
    e.preventDefault();
    var data = $(this).serializeArray();
    console.log("data", data);

    var postData = [];
    data.forEach(function(each) {
      postData.push({
        question: each.name,
        choice: each.value
      });
    });

    $.ajax({
      url: BASE_URL + "make_selections/",
      type: "POST",
      data: JSON.stringify(postData),
      contentType: "application/json",
      dataType: "json",
      success: function(response) {
        console.log("response postData", response);
      }
    });

  });

});


// <script>
// document.write('<style>#chat_box{position: fixed;bottom: 0px;right: 40px;width: 350px;border-right: 1px solid #ccc;border-left: 1px solid #ccc;border-radius: 5px 5px 0 0;box-sizing: border-box;z-index: 9999;}#chat_box_head , #chat_box_body{width: 350px;cursor: pointer;}#chat_box_head{background-color: #c00;color: white;padding: 10px;border-radius: 5px 5px 0 0;}#chat_box_body{height: 0;}.height{height: 300px!important;}iframe{height:290px;border: 0;}.chat_div_class{height: 300px;overflow-y: scroll;overflow-x: hidden;}</style><div id="chat_box" onclick="toggle()"><div id="chat_box_head">Survey</div><div id="chat_box_body"><iframe src="http://localhost:5000/api/make_selections/" width="98%" ></iframe></div></div><script>function toggle(){var element=document.getElementById("chat_box");element.classList.toggle("chat_div_class");}<\/script>');
// </script>
