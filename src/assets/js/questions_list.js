 $(function(){

 		var BASE_URL = "http://localhost:5000/api/"

		function setHeight(){
			$(".response").each(function(index,element){
				var target = $(element);
				target.removeClass("fixed-height");
				var height = target.innerHeight();
				target.attr("data-height", height)
					  .addClass("fixed-height");
			});
		};

		$("input[name=question]").on("change", function(){
			$("p.response").removeAttr("style");

			var target = $(this).next().next();
			target.height(target.attr("data-height"));
		});

		$("#showForm").on("click", function(){
			$("#question_form_div").fadeIn();
			$("#submitForm").fadeIn();
			$("#showForm").hide();
		});

		$("#submitForm").on("click", function(e) {
			e.preventDefault();
			submitForm();
		});

		$("#addChoice").on("click", function(e) {
			e.preventDefault();
			$("#question_form_div").append('<div class="col-md-3"><label>Choice 1</label>' +
						'<input type="text" name="choice_text" class="form-control form-box new"></div>');
		});

		// function objectifyForm(formArray) {//serialize data function

		// 	var returnArray = {};
		// 	for (var i = 0; i < formArray.length; i++){
		// 		if (returnArray[formArray[i]['name']]) {
		// 			if (Array.isArray(returnArray[formArray[i]['name']])) {
		// 				returnArray[formArray[i]['name']].push(formArray[i]['value']);
		// 			} else {
		// 				var temp = returnArray[formArray[i]['name']];
		// 				returnArray[formArray[i]['name']] = [];
		// 				returnArray[formArray[i]['name']].push(temp);
		// 			}
		// 		} else{
		// 			returnArray[formArray[i]['name']] = formArray[i]['value'];
		// 		}
		// 	}
		// 	return returnArray;
		// }



		function submitForm(){
			var form = $("#question_form").serializeArray();
			var formData = objectifyForm(form);
			console.log(formData);

			$.ajax({
				url: BASE_URL + "create_question/",
				type: "POST",
				data: JSON.stringify({
					question_text: formData.question_text,
					choices: formData.choice_text
				}),
				contentType: "application/json",
				dataType: "json"
			}, function(data) {
				console.log("response", data);
			});
		}

		setHeight();
	});
