$(function() {

  var BASE_URL = "http://localhost:5000/api/"
  // var $div = $('<div><h1>Hello</h1></div>').appendTo('body');

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
      var h3 = '<h3>' + each.question.text + '</h3>';

      each.choices.forEach(function(choice, index) {
        var div = '<div><input type="radio" name="  ' + each.question.id + '" id="question-' + each.question.id + '-answers-' + index + '" value="' + choice.id + '" /><label for="question-' + each.question.id + '-answers-' + index + '">' + index + ') ' + choice.text + '</label></div>';
        h3 += div;
      });

      console.log("h3", h3);

      li += '<li>' + h3 + '</li>';

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
      contentType: "application/json",
      dataType: "json",
      success: function(response) {
        console.log("response postData", response);
      }
    })

  });

});
