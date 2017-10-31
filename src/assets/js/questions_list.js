$(function() {

	// var BASE_URL = "http://localhost:5000/api/admin/";
	var BASE_URL = "https://test-survey-flask.herokuapp.com/api/admin/";

	$("#addChoice").on("click", function(e) {
		e.preventDefault();
		$("#addQuestion").append('<div class="form-group"><label>Choice ' + '</label><input type="text" class="form-control form-box" name="choice_list"></div>');
	});

	$("#submitForm").on("click", function(e) {
		e.preventDefault();
		var data = getFormData($("#addQuestion").serializeArray());
		console.log("data", data);

		$.ajax({
			url: BASE_URL + "create_question/",
			type: "POST",
			data: JSON.stringify(data),
			contentType: "application/json",
			dataType: "json",
			success: function success(response) {
				console.log("response", response);
				location.reload();
			}
		});
	});

	function getFormData(form) {

		var result = {};
		form.forEach(function(each) {
			if (result.hasOwnProperty(each.name)) {
				if (Array.isArray(result[each.name])) {
					result[each.name].push(each.value);
				} else {
					result[each.name] = Array(result[each.name]);
					result[each.name].push(each.value);
				}
			} else {
				result[each.name] = each.value;
			}
		});

		return result;
	}

	$("#editChoicesButton").on("click", function(e) {
		e.preventDefault();
		toggleFade();
	});

	function toggleFade() {
		$("#viewChoices").fadeToggle();
		$("#editChoices").fadeToggle();
	}

	$("#saveChoices").on("click", function(e) {
		e.preventDefault();
		var data = getFormData($("#editChoiceForm").serializeArray());
		console.log("data", data);

		$.ajax({
			url: BASE_URL + "edit_choices/",
			type: "POST",
			data: JSON.stringify(data),
			contentType: "application/json",
			dataType: "json",
			success: function(response) {
				console.log("edit response", response);
				toggleFade();
			}
		});
	});

});
